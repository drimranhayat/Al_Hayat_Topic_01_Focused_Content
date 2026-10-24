# Al-Hayat Hadith — Android release preparation

This repository now contains an actual Capacitor Android project, not just a link to a website. The app bundles forty lessons, Arabic source quotations, English translations, classical commentary extracts, search, notes, bookmarks, progress and practice. Internet is only needed to follow external references. There are no ad or analytics SDKs.

## Build

Use Node 22+, Python 3 with `pip install -r requirements.txt`, Android Studio, JDK 21 and Android SDK 36. The generated project targets API 36 and supports API 24+.

```
npm ci
npm run android:sync
npm test
node scripts/check-reader.mjs .
npm run android:open
```

In Android Studio, run on a device, then use **Build > Generate Signed App Bundle / APK > Android App Bundle**. Create and privately retain your upload key. Do not commit signing passwords or keystores. The unsigned release command is `cd android && ./gradlew bundleRelease`; an unsigned bundle cannot be submitted.

The application ID `org.alhayat.hadith` is provisional: confirm ownership and uniqueness before the first Play upload. If changing it, change the Capacitor config, Android namespace/applicationId and Java package consistently.

## Required publisher work before submission

- Replace the release-draft paragraph in `privacy.html` with your real support email and effective date. Identify the same publisher as in your Play listing. Host this policy at a public HTTPS URL and retain its in-app link.
- Verify quotation, translation and digital-edition reuse rights. Source citations and literal-text checks do not establish a reuse license or independent scholarly approval. Have a qualified hadith reviewer review the final lesson text and exercises.
- Make a signed AAB; retain the key and enroll in Play App Signing. Complete developer verification and any account-specific testing requirement.
- Supply actual screenshots from the built app, a 512×512 store icon, 1024×500 feature graphic, support contact and a truthful store listing. No screenshots have been fabricated for this release.
- Complete content rating, target audience, app access, ads and Data safety declarations. Current code has no developer data collection or ads; verify the final dependencies and behaviour before declaring this. Local backups and user-initiated sharing are explained in the privacy draft. No account-deletion flow is needed while there are no accounts.

For personal accounts created after November 13, 2023, Google currently requires at least 12 testers continuously opted in for 14 days before applying for production access. Your Console determines the requirements applicable to your account.

## Device acceptance checks

Test Android 7 and a current Android 16 device/emulator; compact and large screens; portrait/landscape; 200% system text; dark mode; TalkBack; gesture and three-button navigation. Verify no overlap with system bars. Test all four reader tabs, search, saved/read status, notes persistence after restart, quiz restore, JSON backup export/import, external links, native sharing, cancellation and Android Back. Install fresh, enable airplane mode and read every section. Verify Arabic shaping and diacritics on device with the system Arabic font. Run the Play pre-launch report and resolve crashes/ANRs and accessibility issues.

## Validation status

Web build, Capacitor Android generation/sync, quotation checks, simulated navigation and quiz checks were run. Android compilation, signing, emulator/device testing and Play pre-launch review remain outstanding: this environment has Java 17 and no Android SDK, and the Gradle distribution download failed because its network destination was unreachable. Google alone decides acceptance.

## Official references (checked October 24, 2026)

- https://developer.android.com/google/play/requirements/target-sdk
- https://support.google.com/googleplay/android-developer/answer/10787469
- https://support.google.com/googleplay/android-developer/answer/14151465
- https://support.google.com/googleplay/android-developer/answer/10144311
- https://capacitorjs.com/docs/android

## Design reference

Sunnah.com provides direct search and collection browsing; Greentech's Hadith Collection documents bookmarks, last-read progress, adjustable text, dark mode and sharing. This edition uses these familiar reading patterns with its own restrained green design, English interface and Arabic source blocks. It does not import their design assets or claim their affiliation.

- https://sunnah.com/
- https://gtaf.org/apps/hadith/
