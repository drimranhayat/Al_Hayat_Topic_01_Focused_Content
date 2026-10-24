"""One repeatable build: website, English presentation, Android web bundle."""
from pathlib import Path
import subprocess,sys,shutil,re
R=Path(__file__).resolve().parent.parent
for script in ['build.py','redesign.py','finish_release.py','english_release.py']:
 subprocess.run([sys.executable,str(R/script)],cwd=R,check=True)
subprocess.run([sys.executable,'configure_seo.py','--directory','.', '--base-url','https://drimranhayat.github.io/Al_Hayat_Topic_01_Focused_Content/'],cwd=R,check=True)
# SEO generator predates the English edition; normalize its language metadata too.
subprocess.run([sys.executable,'english_release.py'],cwd=R,check=True)
www=R/'www'
if www.exists():shutil.rmtree(www)
www.mkdir()
for name in ['index.html','library.html','sources.html','privacy.html','404.html']:
 shutil.copy2(R/name,www/name)
for name in ['assets','hadith']:shutil.copytree(R/name,www/name)
# No remote fonts: Android supplies Arabic-capable fallback fonts offline.
for css in (www/'assets').glob('*.css'):
 css.write_text(re.sub(r"@import\s+url\([^;]+;",'',css.read_text()))
# Native bridge only in packaged app, after the lesson scripts.
for p in www.rglob('*.html'):
 prefix='../' if p.parent.name=='hadith' else ''
 s=p.read_text();s=s.replace('</body>',f'<script src="{prefix}assets/native.js" defer></script></body>')
 p.write_text(s)
subprocess.run([str(R/'node_modules/.bin/esbuild'),str(R/'app/native.js'),'--bundle','--format=iife','--outfile='+str(www/'assets/native.js')],cwd=R,check=True)
print('Built website and offline Android assets. No audit/source archives are bundled in the app.')
