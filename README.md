# Varun Kumar C N 👋

**🚀 Full Stack Developer · React & Node · AI Video & Content Pipelines · CRM Lead Scoring · Technical SEO**

*TypeScript · JavaScript · Python · Node.js · Next.js · MongoDB · Playwright · ffmpeg*

📧 [Email](mailto:varungowda485@gmail.com) · 💼 [LinkedIn](https://www.linkedin.com/in/varun-kumar-c-n-015662303)

---

## 💡 What I work on

Full Stack Developer at **Smart AI Technologies and Solutions** with **1.5+ years of professional experience**, building **LawWorld** (lawworld.ai), an AI legal-tech platform for Indian advocates. I own the public marketing site end to end, build backend microservices in a Node.js / TypeScript monorepo, and design the pipelines that turn court judgments into published content — articles, e-Books, 9:16 reels and long-form videos — using OpenAI, Anthropic, Google Flow, HeyGen, ElevenLabs and ffmpeg. I also wired the platform's product signals into Zoho CRM lead scoring. 🎓 BE in Computer Science, 2024 graduate.

---

## 🏗️ What I've built

### 🎬 Reel Maker & Video Maker — judgment PDF → finished marketing video
*LawWorld · Node.js · TypeScript · Playwright · OpenAI · HeyGen · ElevenLabs · ffmpeg · Cloudflare R2 · MongoDB*

An HTTP pipeline service plus an admin UI that takes an Indian court judgment PDF and produces a ~90-second 9:16 reel, or takes several judgments and produces a 16:9 long-form video.

- **Eight resumable stages** — `extract → plan → validate → broll → story → review → intro → compose → publish`. Every stage skips itself when its output already exists, so a failed run costs nothing to resume.
- **AI planning** — OpenAI extracts court, bench, provisions and holding from the PDF, then writes story and B-roll storyboards; a words-per-second fill rule validates every line fits its clip.
- **Split-frame reel** — presenter in the lower half, B-roll in the upper half, a HeyGen avatar with a cloned ElevenLabs voice for the intro (the only part allowed to name judges), an outro card from a reusable library.
- **Human review loop** — jobs pause as `awaiting_review`; admins patch, regenerate, reject or restore individual scenes before approving.
- **Admin feature** — Reel Maker / Video Maker screens in the Next.js admin (jobs table, scene grid, credits bar, provider health banner, publish dialog), sharing one typed API contract with the service.
- Clips are probed, contact-sheeted and uploaded to R2 per attempt; finished media publishes into the site's existing `marketing-shorts` / `marketing-videos` feeds.

### 🤖 Google Flow AI Video Automation Suite
*Node.js · TypeScript · Playwright*

Browser automation that drives Google Flow (`labs.google/flow`) to generate multi-scene AI video unattended.

- Persistent logged-in Chrome profile, so Google sign-in happens once.
- **Five-category prompt sanitizer** that rewrites policy trigger words (real persons, current events, judiciary terms, fake statements, sensitive topics) before submission.
- **Inline error auto-recovery** — watches the DOM for policy error cards, undoes, logs the flagged prompt, resubmits a safe fallback and carries on.
- Dual MP4 downloader (UI download event with a network-stream interception fallback), end-frame continuity between scenes, timeline assembly and export.
- A landscape "explainer" compositor: presenter over B-roll, speech-synced text cards, branded intro and outro.

### 📈 Zoho CRM lead scoring across the platform
*LawWorld · identity, billing, case services · Express gateway · Next.js site · Zoho CRM API*

Zoho was creating a Lead per signup and losing track of it, so nothing could ever be scored. I fixed that and built the signal plumbing.

- Persist the Zoho Lead ID per user, make Leads updatable, and reconcile older users by email so nobody ends up with two Leads.
- Derive Country from the dial code (and fix the silent Mongoose field mismatch that meant no email signup had ever stored one).
- An internal `lead-signals` endpoint, guarded by a shared secret that fails shut, so billing and case services report wallet top-ups, LawChat usage, invoices, cases and activity recency.
- Marketing-site page-visit tracking handed over at signup, and a two-rule scoring design (**Fit** for who they are, **Intent** for what they did) with exact field mappings.

### 🌐 lawworld.ai marketing website
*Next.js (App Router) · TypeScript · Tailwind · MongoDB · hls.js · Razorpay*

Most active contributor on the public site (300+ commits), covering:

- **Pricing & launch offer** — plan comparison table with entitlement dropdowns, pay-as-you-go column driven by backend values, sign-in-gated Razorpay checkout that hands off to the app.
- **Learn hub** — Shorts with live comments, Videos with HLS playback and reactions, e-Books served from the API with generated covers, blog / article / news sourced live with a 30% teaser before the sign-in wall.
- **Help Center** at `/docs`, training workshop pages wired to the live workshops API with booking, Cookie Policy and first-visit notice.
- **Performance & SEO** — lazy-loaded Google Sign-In, route-scoped fonts, layout-shift fixes, a 2 MB SVG logo replaced with an optimizable mark, title-tag and structured-data fixes.

### 🗄️ Marketing media backend (video-learning-service)
*Node.js · TypeScript · Express · MongoDB · Cloudflare R2*

- Public Shorts and Videos APIs with separate collections, comments and reactions, plus admin CRUD.
- Published NotebookLM pipeline videos on the public feed with auto-generated thumbnails stored in MongoDB.
- e-Books feed with PDF upload admin, and a brand-asset endpoint for CRM / email templates.
- Matching admin **Shorts / Videos / e-Books stores** with publish toggles in the Next.js admin.

### 🔍 [ScrapeMASTER](https://github.com/Varun3344/scrapemaster) — Chrome extension for local business leads
*Chrome Manifest V3 · vanilla JavaScript · no build step, no external requests*

- **Quick scrape** deep-paginates one Google Local Finder search to 50 / 100 / 200 leads and exports a clean `Name,Phone,Email` CSV.
- **Batch campaign** walks a whole district area by area for days, deduping into a persistent master database with a live dashboard and 12-column export.
- RFC 4180 CSVs, normalised phone numbers, strict dedupe, and a territory map (`state → district → areas`) with query templates.

### ✍️ [Judgment → article & blog pipeline](https://github.com/Varun3344/pipeline-lawworldblog)
*Next.js · Anthropic SDK · OpenAI · MongoDB · Cloudinary*

Fetches a judgment, plans the piece with AI, pulls keywords, generates the article and blog, renders a cover image with `gpt-image-1` and uploads it to Cloudinary, then saves as draft or published. Ships with a signup gate, dynamic sitemap and an admin generate form.

### 📺 [YouTube multi-channel uploader](https://github.com/Varun3344/youtube-automation)
*Express · googleapis · multer*

One dashboard to upload videos to any connected YouTube channel.

### 🧰 Earlier work
Real-time chat app ([front-end](https://github.com/Varun3344/chat-front-end) · [backend](https://github.com/Varun3344/chat-backend)), a notifications app ([Notify-me](https://github.com/Varun3344/notify-me-front-end)), an [auth backend](https://github.com/Varun3344/auth-backend), and law-firm websites ([Associate-website](https://github.com/Varun3344/Associate-website), [shwetharavishankar](https://github.com/Varun3344/shwetharavishankar), [web-page-best-law](https://github.com/Varun3344/web-page-best-law)).

---

## 🛠️ Stack

- **💻 Languages** — TypeScript · JavaScript · Python · Core Java · HTML5 · CSS3
- **🎨 Frontend & Mobile** — React · Next.js (App Router, SSR / ISR) · Tailwind CSS · Radix / shadcn · TanStack Query · Zustand · React Native
- **⚙️ Backend** — Node.js · Express · REST APIs · microservices monorepo behind a gateway · Socket.IO
- **🗄️ Data & Storage** — MongoDB / Mongoose · Firebase (Firestore / Realtime DB, FCM) · Cloudflare R2 · Cloudinary
- **🤖 AI & Media** — OpenAI · Anthropic Claude · HeyGen · ElevenLabs · Google Flow · NotebookLM · ffmpeg · HLS
- **🧪 Automation & Testing** — Playwright (browser automation and e2e) · Vitest · Chrome extensions (MV3)
- **📊 CRM & Payments** — Zoho CRM (Leads API, scoring rules, journeys) · Razorpay
- **🔍 SEO & Publishing** — Technical SEO · JSON-LD · dynamic sitemaps · Core Web Vitals · OpenGraph
- **🧰 Tools** — Git · GitHub · GitHub Actions · Kubernetes manifests · VS Code

---

## 💪 Strengths & Highlights

- **🎬 AI content pipelines** — Designed and shipped multi-stage, resumable pipelines that turn source documents into publishable video, articles and e-Books, with human review built in.
- **🤖 Browser automation** — Drove a consumer AI product with Playwright at production volume, including policy-error recovery and prompt sanitisation.
- **🌐 Full-stack ownership** — Own a public Next.js site end to end: features, performance, SEO, payments and the APIs behind it.
- **📈 Data into the CRM** — Turned product usage into Zoho lead-scoring signals with secure service-to-service reporting.
- **📱 Cross-platform** — React Native experience with Firebase real-time data and push notifications.

---

## 🌱 Currently exploring

- 🎥 Long-form 16:9 judgment videos: case cards, presenter-over-B-roll composition, voice cloning
- ⚡ Programmatic SEO and content generation at scale
- ☸️ Microservices on Kubernetes (AKS) and CI for a service monorepo

---

## 📌 At a glance

```
role:       Full Stack Developer
company:    Smart AI Technologies and Solutions — building LawWorld (lawworld.ai)
experience: 1.5+ years
focus:      Next.js · Node.js microservices · AI video & content pipelines · CRM lead scoring · SEO
stack:      TypeScript · JavaScript · Python · MongoDB · Playwright · ffmpeg · Cloudflare R2
ai tools:   OpenAI · Anthropic · HeyGen · ElevenLabs · Google Flow · NotebookLM
education:  BE Computer Science, 2024
location:   Bangalore, India
timezone:   IST (UTC+5:30)
contact:    varungowda485@gmail.com
linkedin:   linkedin.com/in/varun-kumar-c-n-015662303
```

---

⭐ *Thanks for visiting — feel free to connect!*
