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

The portable ZIP intentionally has no canonical URL pointing to the private preview. After GitHub displays the real Pages address, run:

```
python3 configure_seo.py --base-url https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/ --directory .
```

Replace the example with your exact URL, then upload the generated sitemap, robots file and updated HTML. If you prefer, configure these files on your computer before uploading. They are not required for the site to function. No keyword strategy guarantees a specific search ranking.

## Sources and authenticity

All 40 records are labelled **Authentic** by **HadeethEnc.com**. Grade labels are publisher assessments, not a new independent authentication or a claim of specialist approval. Six selections are attributed to Sunan collections; the remainder are attributed to Bukhari or Muslim. The Muslim introduction report is clearly qualified. A hasan candidate was excluded.

Arabic, translations, explanations and benefits are kept as supplied by HadeethEnc. The site displays the complete publisher selection, which can be shorter than the primary collection narration and does not necessarily include a full chain. Primary links can differ slightly in wording or numbering. Editorial titles, ordering and personal notes are separate from source text.

**Publisher**: HadeethEnc.com. **Interface**: API v1. **Snapshot**: 17 October 2026. The API did not supply a separate translation revision number; the retrieval snapshot is not claimed as a publisher edition. Preserve publication information, compare current versions, and follow https://hadeethenc.com/en/home terms when maintaining or reusing content. Translation issues should be reported through the linked source record. Do not silently rewrite translations.

Sunnah.com is used for primary reference links and selected cross-checking, not bulk-scraped content. No affiliation with either publisher is asserted. For legal or disputed applications, consult a qualified scholar with the relevant connected evidence.

## Files and maintenance

- `index.html`: all forty entries in crawlable HTML.
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

The learning bank contains **74 explanatory Q&A and 84 focused MCQs**. Counts vary with the content: one to four explanatory answers and one to five MCQs per hadith. Brief reports have brief question sets. Questions focus on central meanings, necessary context, useful distinctions and practical understanding. They do not impose a fixed quota on every report.

Q&A is written separately from the quizzes. The former explains the main points in connected prose; the latter checks selected learning points. Repeated narrator, grading, and sanad templates, automatically generated benefit/glossary questions, obvious omission questions, and overlapping recall items have been removed. All published benefits and glossary material remain available in the original reading panels. Reporter and reference information remain in Sources and authenticity.

Every retained question has a checked source anchor and expandable supporting passage. Full chains must be checked through the primary collection links. This editorial review does not claim independent specialist approval. Quiz storage uses a new revision key so deleted or reordered questions do not inherit incorrect scores; notes, bookmarks and reading progress keep their original keys.

Entry 28 contains separate reports from Ibn Masud and Ibn Umar. Both are identified; its sources panel also links Bukhari 5025 for the accompanying Ibn Umar report.

Hadith 37 has an explicit narrator correction notice: Arabic, Urdu and Sahih Muslim 1017a identify Jarir ibn Abdullah; the publisher English says Jabir. The source translation is preserved unchanged. Learning questions use Jarir.

Run `node scripts/check-learning.mjs .` for learning interaction checks.


## Content review

See `CONTENT_REVIEW.md` for the scope and results of the thematic review. `focused_qa.py` contains the concise explanatory answers. `thematic_questions.py` contains the 84 retained MCQs, explanations, hints and source anchors. `learning_builder.py` assembles the material and checks source anchors during regeneration. Run `python3 scripts/check_learning_sources.py .` and `node scripts/check-learning.mjs .` for a portable ZIP, or use `dist` for the development checkout.

## Mobile reading update

Dedicated layouts for phones and tablets, including 320–430px screens: wrapping section buttons, stacked search and selectors, single-column study menus, larger text, 44px or larger action controls, wrapped pagination, safe-area spacing, and scrollable dialogs. The phone dock remains clear of the final content and notification messages. Arabic and Urdu keep normal word boundaries. Existing topics, source text, IDs and browser progress keys are preserved. Automated behavior/content checks pass; browser viewport and device visual testing was unavailable in this environment.
