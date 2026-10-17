# Al-Hayat Forty Hadith Series — Topic 001

## Revelation and Following the Sunnah

A complete static educational site containing **40 source-authenticated selections**, **five sections of eight**, Arabic text, published English and Urdu translations, source explanations and benefits, 40 individual reading pages, and a full source register.

### Included tools

- Search all 40 records in Arabic, Urdu or English, or by reference.
- Section filters and eight-card pagination.
- Bookmarks, personal notes and reading progress stored in the current browser.
- Export/import study backups, keeping existing notes during import.
- Memorization mode to hide and reveal translations.
- Reading-language switches, adjustable text size, light/dark themes and print styles.
- Crawlable HTML and distinct titles/descriptions for all entry pages.

## Deploy on GitHub Pages

For the downloadable GitHub ZIP, upload the **contents** of its folder to a repository root. `index.html`, `assets/`, `hadith/` and `sources.html` must be at the repository root, not inside another nested folder.

Choose **Settings → Pages → Deploy from a branch → main → /(root) → Save**. No Node installation, database or secret key is needed to deploy the ready-built files.

The development checkout instead keeps publishable files under `dist/`; copy its contents to the repository root if deploying that checkout manually.

### Configure search metadata after choosing your URL

The release includes canonical URLs, social metadata, structured data, robots.txt and a sitemap for the public Al-Hayat site. If hosting this repository at another address, run `python3 configure_seo.py --base-url` followed by your actual HTTPS deployment URL and `--directory .`. Upload the regenerated HTML, sitemap.xml and robots.txt.

## Sources and authenticity

All 40 records are labelled **Authentic** by **HadeethEnc.com**. Grade labels are publisher assessments, not a new independent authentication or a claim of specialist approval. Six selections are attributed to Sunan collections; the remainder are attributed to Bukhari or Muslim. The Muslim introduction report is clearly qualified. A hasan candidate was excluded.

Arabic, translations, explanations and benefits are kept as supplied by HadeethEnc. The site displays the complete publisher selection, which can be shorter than the primary collection narration and does not necessarily include a full chain. Primary links can differ slightly in wording or numbering. Editorial titles, ordering and personal notes are separate from source text.

**Publisher**: HadeethEnc.com. **Interface**: API v1. **Snapshot**: 17 October 2026. The API did not supply a separate translation revision number; the retrieval snapshot is not claimed as a publisher edition. Preserve publication information, compare current versions, and follow https://hadeethenc.com/en/home terms when maintaining or reusing content. Translation issues should be reported through the linked source record. Do not silently rewrite translations.

Sunnah.com is used for primary reference links and selected cross-checking, not bulk-scraped content. No affiliation with either publisher is asserted. For legal or disputed applications, consult a qualified scholar with the relevant connected evidence.

## Files and maintenance

- `index.html`: course home with five learning sections.
- `library.html`: forty compact, linked hadith cards.
- `hadith/`: forty focused reading pages.
- `sources.html`: methodology and complete reference register.
- `assets/`: CSS, JavaScript, complete search data and favicon.
- `content.json`: normalized forty-entry dataset.
- `source-data/`: 80 unmodified publisher API JSON responses, two language responses per entry; the English response also supplies Arabic.
- `content-manifest.json`: source checksums, count and grading provenance.
- `build.py`: deterministic generator using Python standard library only.
- `configure_seo.py`: configure real deployment URLs.
- `scripts/check-site.mjs`: data, static structure and simulated interaction checks using Node built-ins.

For the portable ZIP, regenerate with `python3 build.py`, then run `node scripts/check-site.mjs .`. Reapply `configure_seo.py` after regeneration. The development checkout uses `python3 build.py` followed by `node scripts/check-site.mjs dist`.

To update source material, retain the publisher records and their IDs, compare revised content, confirm the Authentic grade and translation availability, revise the recorded snapshot date, rebuild, and rerun checks before publishing. Do not fill missing records with generated text.

### Fonts and privacy

Arabic uses Amiri. Urdu prefers locally installed Jameel Noori Nastaleeq, with Noto Nastaliq Urdu as the downloadable fallback. Jameel Noori Nastaleeq is not bundled. Fonts load from Google Fonts; fallback fonts keep the site readable if unavailable. Notes are not sent to a server. No account synchronization or custom backend is included.

### Verification performed

Source text and translation equality checks; 40 distinct IDs and Arabic texts; exactly 8 entries per section; primary references; HTML link checks; JS syntax; and simulated filtering, pagination, bookmarks, progress and blocked browser storage. Live browser visual testing was unavailable in the creation environment; review on your target devices before a broad public launch.

## Navigation update

Mobile bottom navigation includes Read, Contents, Saved and Settings. Contents can be searched by title or number. Section and direct-hadith dropdowns appear above the reader. Read checkboxes are visible beneath each narration; the home action changes to Resume after progress is recorded. Focused reading pages have previous/next links above and below the narration. Existing browser progress keys and source texts are preserved.

## Optional content panels

English explanation, Urdu explanation, Arabic explanation/vocabulary, benefits, sources and notes each have a colored native disclosure button with a vector icon. All panels start closed, including on individual reading pages. Collection information is also collapsed. The main Arabic text, translations and primary reference remain visible. Native disclosures work without JavaScript and support keyboard use.

## Learning routes and practice

Each hadith has a four-step route: Read, Explanation, Questions and Answers, and MCQ Practice. Use Back step and Next step within a report, Previous hadith and Next hadith between reports, and Main menu to return to the collection. Optional explanations, answers, hints and practice stay collapsed until opened.

The learning bank contains **104 explanatory Q&A and 135 focused MCQs**. Counts vary with the content: one to seven explanatory answers and one to nine MCQs per hadith. Brief reports have brief question sets. Questions focus on central meanings, necessary context, useful distinctions and practical understanding. They do not impose a fixed quota on every report.

Q&A is written separately from the quizzes. The former explains the main points in connected prose; the latter checks selected learning points. Repeated narrator, grading, and sanad templates, automatically generated benefit/glossary questions, obvious omission questions, and overlapping recall items have been removed. All published benefits and glossary material remain available in the original reading panels. Reporter and reference information remain in Sources and authenticity.

Every retained question has a checked source anchor and expandable supporting passage. Full chains must be checked through the primary collection links. This editorial review does not claim independent specialist approval. Quiz storage uses a new revision key so deleted or reordered questions do not inherit incorrect scores; notes, bookmarks and reading progress keep their original keys.

Entry 28 contains separate reports from Ibn Masud and Ibn Umar. Both are identified; its sources panel also links Bukhari 5025 for the accompanying Ibn Umar report.

Hadith 37 has an explicit narrator correction notice: Arabic, Urdu and Sahih Muslim 1017a identify Jarir ibn Abdullah; the publisher English says Jabir. The source translation is preserved unchanged. Learning questions use Jarir.

Run `node scripts/check-learning.mjs .` for learning interaction checks.


## Content review

See `CONTENT_REVIEW.md` for the scope and results of the thematic review. `focused_qa.py` contains the concise explanatory answers. `thematic_questions.py` contains the original focused MCQs, explanations, hints and source anchors. `learning_builder.py` assembles the material and checks source anchors during regeneration. Run `python3 scripts/check_learning_sources.py .` and `node scripts/check-learning.mjs .` for a portable ZIP, or use `dist` for the development checkout.

## Mobile reading update

Dedicated layouts for phones and tablets, including 320–430px screens: wrapping section buttons, stacked search and selectors, single-column study menus, larger text, 44px or larger action controls, wrapped pagination, safe-area spacing, and scrollable dialogs. The phone dock remains clear of the final content and notification messages. Arabic and Urdu keep normal word boundaries. Existing topics, source text, IDs and browser progress keys are preserved. Automated behavior/content checks pass; browser viewport and device visual testing was unavailable in this environment.

## Final coverage edition

The final bank has **104 explanatory Q&A and 135 MCQs**, with 135 teaching points mapped across all forty selected reports. The core instructions, prohibitions, conditions, promises, warnings, narrative context, important terms and necessary commentary distinctions are covered through connected answers and selected practice. Source, reporter and publisher assessments remain in the dedicated source panels; missing full chains are not reconstructed. A brief report may need only one explanatory answer. A long report receives as many distinct items as its content warrants.

Use **What this study set covers** inside each Q&A panel, or the footer's **Learning coverage and question counts** link. All optional material remains collapsed. The complete audit is supplied as `COVERAGE_AUDIT.md`, `coverage-audit.csv` and `coverage-audit.json`. It maps teaching points to numbered explanations and MCQs. These mappings are editorial judgments, not independent scholarly certification.

`expanded_learning.py` contains the individually written additions. `focused_qa.py` and `thematic_questions.py` retain the original questions and append those additions, preserving the existing question IDs. `coverage_map.py` defines the teaching-point mappings; `coverage_report.py` regenerates the audit and website coverage page. The original pre-revision learning bank and hadith content are retained in `audit/` for comparison.

Quiz attempts start fresh under `alhayat-topic001-v4-coverage-quiz` so the enlarged question bank cannot inherit mismatched scores. Bookmarks, reading progress, settings and notes keep their existing keys. The mobile stylesheet is retained throughout.

Additional final checks:

```sh
python3 scripts/check_coverage.py .
python3 scripts/check_content.py .
```

Use `dist` instead of `.` for the hosted development checkout. Browser and real-device visual testing remain unverified. An independent subject-specialist review remains separate from this editorial and technical audit. Coverage concerns the selected texts and their necessary explanation, not every possible variant, chain, disputed ruling or incidental detail transformed into a quiz.

## Focused reading layout

Start at `index.html`: five section cards, reading progress and Continue Reading. `library.html` contains compact searchable title cards, eight per page with JavaScript. Each title opens its own `hadith/` page with Read → Explanation → Q&A → Practice, expandable section contents, previous/next links, language controls and memorization. The library supports `?section=1`, `?view=saved`, `?view=unread`, `?q=...` and `?page=2`; its URL preserves search and filter state for browser Back. Legacy `index.html#hadith-ID` links open the corresponding focused reader.

All 40 IDs and lightweight navigation metadata remain present so opening one reading page does not drop other bookmarks or progress. `assets/entries/ID.js` supplies only that report's detailed data and exercises. The library loads a separate three-language search index without explanations or quizzes. `assets/data.js` is retained as the complete audit/test dataset but is not loaded by any reading, home or library page. Storage and quiz keys are unchanged by this layout revision.

The homepage and library contain no full report bodies or exercise banks. Each reader's text and all 104 Q&A / 135 MCQs are preserved across the 40 separate pages. The mobile and night-mode styles remain. See `DESIGN_REVIEW.md` for the reference patterns and performance comparison. Run `node scripts/check_layout.mjs .` in the portable repository. Browser and real-device visual checks remain unverified.

## Three-language card titles

Section and hadith cards display English, Arabic and Urdu headings with distinct day/night colors. Arabic uses Amiri and Urdu uses the existing Nastaliq font stack, with RTL direction and generous line spacing. `card_titles.py` supplies editorial translations of headings; these are not quotations or changes to the transmitted text. Arabic and Urdu heading text is included in the library search index. Individual reading pages display the corresponding translated titles.


## Public release
Live site: https://al-hayat-revelation-sunnah.aquaearth3.chatgpt.site/
All 45 Arabic card headings include vowel marks. Urdu uses black ink, including on light panels in dark mode. Source hadith and translations are preserved.
Run `python3 build.py` to regenerate. If moving to a different host, run `python3 configure_seo.py --base-url` followed by the actual HTTPS site URL. Submit that host’s sitemap.xml through your own Google Search Console account. Rankings and indexing are determined by search engines.
