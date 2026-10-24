"""Check complete publication, source closure and preservation of the quotation layer."""
from pathlib import Path
from lxml import html
import json,hashlib,re
R=Path(__file__).resolve().parent.parent
ex=json.loads((R/'explanation-content.json').read_text());sources=json.loads((R/'explanation-sources.json').read_text());rows=json.loads((R/'audit/reader-baseline.json').read_text());classical=json.loads((R/'classical-content.json').read_text())
assert set(ex)=={r['id'] for r in rows}
count=0
for key,source in sources.items():
 assert hashlib.sha256(source['text'].encode()).hexdigest()==source['sha256'],key
 assert re.fullmatch(r'\[.*\]\(https://shamela.ws/book/\d+/\d+\)',source['citation']),key
for row in rows:
 id=row['id'];assert len(ex[id])>=2
 for folder in [R,R/'www',R/'android/app/src/main/assets/public']:
  doc=html.parse(str(folder/'hadith'/(row['slug']+'.html')))
  blocks=doc.xpath('//*[contains(concat(" ",@class," ")," explanation-section ")]')
  assert len(blocks)==len(ex[id]),(id,folder)
  for block,section in zip(blocks,ex[id]):
   assert block.xpath('./h4')[0].text==section['heading']
   assert block.xpath('./p')[0].text.strip()==section['text']
   expected=[re.search(r'\]\((.*)\)',sources[k]['citation']).group(1) for k in section['sourceKeys']]
   assert block.xpath('./p/a/@href')==expected,(id,section['heading'])
   assert expected
  assert doc.xpath('//*[contains(@class,"primary-narration")]')[0].text_content()=='\n\n'.join(q['text'] for q in classical[id]['primary'])
  assert not doc.xpath('//*[@lang="ur"]')
  if id=='3506':
   translation=doc.xpath('//*[@data-translation="en"]')[0].text_content()
   assert 'Jarir ibn Abdullah' in translation and 'Jābir' not in translation
 count+=len(ex[id])
assert len(ex['4801'])==6 and len(ex['3506'])==5
print(f'PASS: all 40 expanded explanations, {count} cited sections, source snapshots/checksums, corrected narrator, and unchanged Arabic narration in website and both Android asset bundles. Citation/structure checks do not establish scholarly authentication.')
