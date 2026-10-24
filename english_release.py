"""Apply the English-interface edition after the classical reader build.
Original transcriptions and translation provenance remain in the audit files.
"""
from pathlib import Path
from lxml import html, etree
import json,re
R=Path(__file__).parent
for p in R.rglob('*.html'):
 if set(p.relative_to(R).parts)&{'audit','www','android','node_modules'}: continue
 t=html.parse(str(p)); root=t.getroot();root.set('lang','en')
 for e in list(root.xpath('//*[@lang="ur" or @data-translation="ur" or contains(@class,"course-title-translations") or contains(@class,"lesson-title-ar") or contains(@class,"card-title-ar") or contains(@class,"summary-ur") or contains(@class,"ur-key")]')):
  if e.getparent() is not None:e.drop_tree()
 for e in root.xpath('//*[@id="show-ur"]'):
  e.getparent().drop_tree()
 for e in root.xpath('//*[@id="translation-choice"]'):
  for opt in list(e):
   if opt.get('value') not in ('en','none'):e.remove(opt)
  e.xpath('./option[@value="en"]')[0].set('selected','selected')
 for e in root.xpath('//*[contains(@class,"english-summary")]'):
  e.set('open','open')
  e.xpath('./summary')[0].text='Explanation in English'
 for para in root.xpath('//p'):
  text=para.text_content()
  replacement=None
  if text.startswith('This is Topic 001'):replacement='This is the first Al-Hayat Forty Hadith course: Revelation and Following the Sunnah. Forty lessons are arranged in five learning sections. Consult each lesson for the collection, edition and source wording; no new hadith grading is claimed.'
  if text.startswith('Most selections are attributed'):replacement='The selection draws on al-Bukhari, Muslim and Sunan collections. Collection names alone do not establish one uniform grade for every included narration. See Sources for editorial scope and provenance.'
  if text.startswith('Published Arabic, English'):replacement='Arabic narrations and commentary extracts follow the cited classical digital editions. English translations of the meaning retain their HadeethEnc attribution. Commentary summaries and practice exercises are editorial. Your notes remain separate from the source text.'
  if replacement:
   for child in list(para):para.remove(child)
   para.text=replacement
 for footer in root.xpath('//footer'):

  if not footer.xpath('.//a[contains(@href,"privacy.html")]'):
   prefix='../' if p.parent.name=='hadith' else ''
   link=html.Element('a',href=prefix+'privacy.html');link.text='Privacy';footer.append(link)
 for e in root.xpath('//head'):
  rel='../' if p.parent.name=='hadith' else ''
  if not root.xpath('//link[contains(@href,"english.css")]'):e.append(html.Element('link',rel='stylesheet',href=rel+'assets/english.css'))
 for e in root.xpath('//script[@type="application/ld+json"]'):
  if e.text:
   data=json.loads(e.text)
   def walk(x):
    if isinstance(x,dict):
     for k,v in x.items():
      if k=='inLanguage':x[k]=['en','ar']
      else:walk(v)
    elif isinstance(x,list):
     for v in x:walk(v)
   walk(data);e.text=json.dumps(data,ensure_ascii=False)
 s=html.tostring(root,encoding='unicode',method='html')
 for a,b in [('Arabic, English &amp; Urdu','Arabic hadith · English translation'),('Arabic, Urdu and English','Arabic hadith and English'),('Arabic, English and Urdu','Arabic and English'),('English and Urdu translations','English translations'),('English/Urdu translations','English translations'),('English/Urdu','English'),('Arabic, Urdu, and English','Arabic and English'),('Reveal translations','Reveal translation'),('Choose the languages you want to read. Arabic and translations retain their distinct colors in both themes.','Choose the text you want to see and adjust the reading size.')]:s=s.replace(a,b)
 p.write_text('<!doctype html>'+s)
print('Applied English interface to all public pages; Arabic source quotations preserved.')
