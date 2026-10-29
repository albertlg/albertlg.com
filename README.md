# albertlg.com

Personal website and blog of Albert López Gálvez: https://albertlg.com 🙋🏻‍♂️

Writing in Spanish, Catalan and English about SEO, AI and LLMs, professional judgement, family and everyday life.

[![Screenshot](https://albertlg.com/img/albertlopez-herobanner.jpg)](https://albertlg.com)

## Stack

- 👨‍💻 [Hugo](https://gohugo.io) (extended) with [Hugo Blox](https://hugoblox.com) modules declared in `go.mod`. Configuration lives in `config/_default/`.
- ⬆️ [Netlify](https://www.netlify.com) builds and publishes the site on every push to `master` (`netlify.toml`).
- 🔎 [Pagefind](https://pagefind.app) search, generated at build time.
- 🤖 `llms.txt` for each language, generated on every build (`layouts/home.llms.txt`, editorial text in `data/llms/`).

## Content

- Posts: `content/<lang>/post/YYYY/MM/<slug>.html`, HTML with TOML front matter. Translations share the same `translationKey` across `es`, `ca` and `en`.
- URLs: Spanish at the root (`/<slug>/`), Catalan under `/ca/`, English under `/en/`.
- Images: `static/img/post/` (post body and social cards) and `assets/media/post-images/` (list thumbnails). Use JPG, around 1672×941 px and under 250 KB.
- Interface strings: `i18n/es.yaml`, `i18n/ca.yaml` and `i18n/en.yaml`.

## Local development

Requirements: Hugo extended (version in `netlify.toml`), Go (version in `go.mod`) and Node.js.

```bash
npm ci
./view.sh             # local server, including future-dated posts
hugo --gc --minify    # production build into public/
```

## Automation

- **Build check** (`.github/workflows/build-check.yml`): builds the site on every push with the same versions as Netlify and fails on duplicate URLs, missing key files or broken links in `llms.txt`. It does not deploy.
- **Daily Netlify Scheduled Build** (`.github/workflows/netlify-scheduled-build.yml`): triggers a Netlify build every day at 10:00 UTC so that future-dated posts get published.

## Legacy

`themes/academic/` and the `*.toml.old` files are kept as a reference from the migration away from the Academic theme. The build does not use them.
