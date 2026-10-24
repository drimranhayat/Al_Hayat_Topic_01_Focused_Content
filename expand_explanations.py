"""Render the source-linked English explanation for each complete narration."""
from pathlib import Path
from lxml import html, etree
import json,re,hashlib
R=Path(__file__).parent
base=json.loads((R/'audit/reader-baseline.json').read_text())
classical=json.loads((R/'classical-content.json').read_text())
pages=json.loads((R/'classical-pages.json').read_text())
research=json.loads((R/'audit/explanation-research.json').read_text())
for source in research['search']['evidence']['sources']+research['additional']['sources']+json.loads((R/'audit/explanation-abrogation-context.json').read_text())['sources']:
 pages[f"{source['book_id']}:{source['page_id']}"]=source
blocks={};id=None
for line in (R/'explanation-text.txt').read_text().splitlines():
 if not line.strip():continue
 if line.startswith('##'):id=line[2:];blocks[id]=[];continue
 title,text,refs=line.split('|');keys=[]
 for ref in refs.split(','):
  if ref in ['p','c']:keys.extend(q['key'] for q in classical[id]['primary' if ref=='p' else 'commentary'])
  else:keys.append(ref)
 if id=='65285' and 'disagreement' in title:
  text=text.replace("records al-Mazari's concern",'first records a concern')
  keys.insert(0,'122406:413')
 if id=='66304' and 'command' in title.lower():text=text.replace('rise and warn, magnify his Lord, purify his garments and shun defilement','rise and warn, with the cited passage continuing through the command to shun defilement')
 sections=blocks[id];sections.append({'heading':title,'text':text,'sourceKeys':list(dict.fromkeys(keys))})
assert set(blocks)=={d['id'] for d in base}
used={k for sections in blocks.values() for b in sections for k in b['sourceKeys']}
source_data={k:{'text':pages[k]['text'],'citation':pages[k]['citation']['markdown'],'sha256':hashlib.sha256(pages[k]['text'].encode()).hexdigest()} for k in sorted(used)}
(R/'explanation-sources.json').write_text(json.dumps(source_data,ensure_ascii=False,indent=2))
(R/'explanation-content.json').write_text(json.dumps(blocks,ensure_ascii=False,indent=2))
def cite(parent,key):
 label,url=re.fullmatch(r'\[(.*)\]\((.*)\)',source_data[key]['citation']).groups()
 a=etree.SubElement(parent,'a',href=url,target='_blank',rel='noopener',**{'class':'book-cite','lang':'ar','dir':'rtl'})
 a.text=label;a.tail=' '
for d in base:
 id=d['id'];p=R/'hadith'/(d['slug']+'.html');doc=html.parse(str(p))
 target=doc.xpath('//*[contains(@class,"english-summary")]')[0]
 target.clear();target.tag='section';target.set('class','explanation-guide');target.set('aria-labelledby','explanation-title')
 etree.SubElement(target,'h3',id='explanation-title').text='Detailed explanation'
 etree.SubElement(target,'p',**{'class':'explanation-credit'}).text='An English editorial explanation of the narration, with classical commentary identified at each point. This explanation is not a quotation from the Prophet or a literal translation of the commentary.'
 nav=etree.SubElement(target,'nav',**{'class':'explanation-outline','aria-label':'Explanation sections'})
 for i,block in enumerate(blocks[id],1):
  anchor=f'explanation-{i}';etree.SubElement(nav,'a',href='#'+anchor).text=block['heading']
  section=etree.SubElement(target,'section',id=anchor,**{'class':'explanation-section'})
  etree.SubElement(section,'h4').text=block['heading']
  para=etree.SubElement(section,'p');para.text=block['text']+' '
  for key in block['sourceKeys']:cite(para,key)
 # Link additional classical commentary alongside the old excerpt register.
 register=doc.xpath('//*[@id="lesson-sources"]/div')[0]
 details=etree.SubElement(register,'details',**{'class':'explanation-references'});etree.SubElement(details,'summary').text='Sources used in the detailed explanation'
 refs=etree.SubElement(details,'p')
 for key in dict.fromkeys(k for b in blocks[id] for k in b['sourceKeys']):cite(refs,key)
 for desc in doc.xpath('//*[@id="panel-understand"]/p[contains(@class,"reading-description")]'):
  desc.text='Follow the narration from beginning to end. Each explanation section links to the hadith text or the classical commentary that supports it.'
 # Additional source blocks remain explicitly identified quotations, behind one disclosure.
 extracts=doc.xpath('//*[@id="panel-understand"]/section[contains(@class,"source-extract")]')
 if extracts:
  wrapper=html.Element('details',**{'class':'commentary-originals'})
  etree.SubElement(wrapper,'summary').text='Read the quoted Arabic commentary'
  extracts[0].addprevious(wrapper)
  for e in extracts:wrapper.append(e)
 if id=='3506':
  # The copied translation named Jabir; the selected Muslim chain is al-Mundhir from his father Jarir.
  for e in doc.xpath('//*[@data-translation="en"]//p[@lang="en"]'):
   e.text=e.text.replace('Jābir ibn ‘Abdullāh','Jarir ibn Abdullah')
  note=etree.SubElement(register,'p');note.text='Translation correction: the narrator is Jarir ibn Abdullah, as identified by the selected Arabic chain. The earlier copied English record named Jabir; the original remains in the audit archive.'
 p.write_text('<!doctype html>'+html.tostring(doc.getroot(),encoding='unicode',method='html'))
 entry=R/'assets/entries'/(id+'.js');js=entry.read_text()
 marker='\n/* detailed-explanation */';js=js.split(marker)[0]
 patch={'explanation':'\n\n'.join(b['text'] for b in blocks[id]),'explanationSections':blocks[id]}
 if id=='3506':patch['en']=d['en'].replace('Jābir ibn ‘Abdullāh','Jarir ibn Abdullah')
 entry.write_text(js+marker+'\nwindow.HADITH_DATA.forEach(d=>{if(d.id==='+json.dumps(id)+')Object.assign(d,'+json.dumps(patch,ensure_ascii=False).replace('</','<\\/')+');});')
print(f'Expanded all 40 explanations into {sum(map(len,blocks.values()))} source-linked sections, {sum(len(b["text"].split()) for s in blocks.values() for b in s)} words.')
