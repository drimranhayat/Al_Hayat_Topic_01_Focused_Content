# Al-Hayat — Revelation and Following the Sunnah

A static teaching website with 40 hadith lessons, five sections, English interface with Arabic hadith and English translation, bookmarks, personal notes, reading progress and editorial exercises.

## This revision

- Four reader tabs: Read, Understand, Practice and Notes.
- Desktop section sidebar and phone Previous / Contents / Next navigation.
- English headings, navigation, learning exercises and commentary summaries.
- Redesigned homepage and library cards with distinct dark section headings.
- Arabic narrations copied from directly cited classical collections.
- Literal extracts from classical commentaries and detailed English explanations covering the narration in source-linked sections.
- Per-lesson references and a complete book-reference register.
- Existing 104 Q&A, 135 MCQs and stable lesson IDs retained.

## What source checking establishes

`classical-pages.json` retains the retrieved digital page transcriptions and citations. `classical-content.json` identifies each displayed quotation, source key and SHA-256 checksum. The source validator checks that each displayed quotation is an unchanged substring of the retained source page. It does not constitute an independent hadith grading, specialist approval or printed-facsimile comparison. Edition numbering is retained rather than silently reconciled.

Translations of the meaning remain separately attributed to HadeethEnc.com. They may represent shorter or parallel wording and omit chains. The former website explanations are archived, not used as the new classical commentary. The exercise bank is retained editorial material; no new specialist sign-off is claimed. See `sources.html`.

## Deploy

Upload the contents of this folder to the repository root and serve with GitHub Pages or another static HTTPS host. No build is needed to use the supplied HTML.

## Rebuild

Install Python and `pip install -r requirements.txt`, then run:

```
npm ci
npm run android:sync
```

The build uses the configured GitHub Pages URL in scripts/build_release.py; change it if deploying elsewhere. Keep the audit source snapshots when rebuilding. Do not rerun historical source-preservation tests as proof of the new text: they intentionally expect the old publisher explanation layout. The current release checks are:

```
python scripts/check_classical_reader.py
node scripts/check-site.mjs .
node scripts/check-learning.mjs .
node scripts/check-reader.mjs .
python scripts/check_explanations.py
python scripts/check_android_bundle.py
```

The Android project bundles all lesson assets for offline reading and provides native text sharing, backup sharing and Back navigation. Arabic text uses the device's Arabic-capable fonts, with no remote font request. The app has no ads or analytics. Automatic Android cloud backup is disabled; users can export their own study backup.

See [PLAY_STORE_RELEASE.md](PLAY_STORE_RELEASE.md) for build instructions, publisher details still needed, signing, privacy and device checks. This is Android source preparation: no signed APK/AAB or Play acceptance is claimed.

See [EXPLANATION_COVERAGE.md](EXPLANATION_COVERAGE.md) for the topics covered in all forty detailed explanations.
