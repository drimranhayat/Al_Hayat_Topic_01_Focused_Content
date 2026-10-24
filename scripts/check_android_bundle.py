from pathlib import Path
from lxml import html,etree
import re
R=Path(__file__).resolve().parent.parent
W=R/'android/app/src/main/assets/public'
assert (W/'assets/native.js').exists()
for p in W.rglob('*.html'):
 t=html.parse(str(p));assert not t.xpath('//*[@lang="ur"]'),p
 for el in t.xpath('//*[@src] | //link[@rel="stylesheet"]'):
  src=el.get('src') or el.get('href');assert not src.startswith(('https:','http:','//')),src
  assert (p.parent/src.split('?')[0]).exists(),(p,src)
for p in W.rglob('*.css'):assert '@import' not in p.read_text(),p
v=(R/'android/variables.gradle').read_text();assert re.search(r'targetSdkVersion\s*=\s*36',v)
m=etree.parse(str(R/'android/app/src/main/AndroidManifest.xml'));ns='{http://schemas.android.com/apk/res/android}'
assert m.find('application').get(ns+'allowBackup')=='false'
assert m.find('application').get(ns+'usesCleartextTraffic')=='false'
assert [e.get(ns+'name') for e in m.findall('uses-permission')]==['android.permission.INTERNET']
assert len(list((W/'hadith').glob('*.html')))==40
assert (W/'privacy.html').exists()
print('PASS: Android bundle has 40 offline readers, local styles/scripts, English interface, privacy page, API 36, no cloud backup and no sensitive manifest permissions. Static checks only.')
