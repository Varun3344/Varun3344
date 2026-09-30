#!/usr/bin/env python3
"""Build assets/core-stack.svg, the Core Stack card shown in the profile README.

Edit GROUPS below, then run:  python3 scripts/build_core_stack.py
Icons are fetched once from public CDNs and cached in ICON_CACHE (default: a temp dir).
"""
import html, os, re, subprocess, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "core-stack.svg")
CACHE = os.environ.get("ICON_CACHE", os.path.join(tempfile.gettempdir(), "core-stack-icons"))

SOURCES = {
    "si": "https://cdn.jsdelivr.net/npm/simple-icons@latest/icons/{}.svg",
    "si11": "https://cdn.jsdelivr.net/npm/simple-icons@11.0.0/icons/{}.svg",
    "lobe": "https://cdn.jsdelivr.net/npm/@lobehub/icons-static-svg@latest/icons/{}.svg",
    "lucide": "https://cdn.jsdelivr.net/npm/lucide-static@latest/icons/{}.svg",
}

WHITE = "#E6EDF3"
# (label, icon source, icon name, colour). Use "|" in a label to force a line break.
GROUPS = {
    "Languages": [
        ("TypeScript", "si", "typescript", "#3B8FE0"), ("JavaScript", "si", "javascript", "#F7DF1E"),
        ("Python", "si", "python", "#4B9CD3"), ("Core Java", "si", "openjdk", "#ED8B00"),
        ("HTML5", "si", "html5", "#E34F26"), ("CSS3", "si", "css", "#8B6CE0"),
    ],
    "Frontend": [
        ("React.js", "si", "react", "#61DAFB"), ("Next.js", "si", "nextdotjs", WHITE),
        ("Tailwind CSS", "si", "tailwindcss", "#06B6D4"),
    ],
    "Mobile": [
        ("React Native", "si", "react", "#61DAFB"), ("Expo", "si", "expo", WHITE),
        ("React|Navigation", "lucide", "navigation", "#A78BFA"), ("Firebase", "si", "firebase", "#FFCA28"),
        ("FCM Push|Notifications", "lucide", "bell-ring", "#FF9100"),
    ],
    "Backend & Data": [
        ("Node.js", "si", "nodedotjs", "#5FA04E"), ("Express.js", "si", "express", WHITE),
        ("REST APIs", "lucide", "braces", "#4C9AFF"), ("Microservices", "lucide", "boxes", "#FF6B6B"),
        ("Socket.IO", "si", "socketdotio", WHITE), ("MongoDB", "si", "mongodb", "#47A248"),
        ("Mongoose", "si", "mongoose", "#F04D35"), ("Cloudflare R2", "si", "cloudflare", "#F38020"),
        ("Cloudinary", "si", "cloudinary", "#5C7CFA"),
    ],
    "Generative AI": [
        ("OpenAI GPT", "si11", "openai", "#19C37D"), ("Codex", "lobe", "codex", WHITE),
        ("Anthropic Claude", "si", "claude", "#D97757"), ("Google Gemini", "si", "googlegemini", "#8E9BFF"),
        ("Google Antigravity", "lobe", "antigravity", "#4C8DF6"), ("MiniMax", "si", "minimax", "#F23F5D"),
        ("Google Flow / Veo", "lucide", "clapperboard", "#34A853"), ("HeyGen", "lucide", "circle-user-round", "#8B7BFF"),
        ("ElevenLabs", "si", "elevenlabs", WHITE), ("NotebookLM", "si", "notebooklm", WHITE),
        ("Prompt Engineering", "lucide", "message-square-code", "#19C37D"),
        ("AI Video & Content|Pipelines", "lucide", "workflow", "#FF8A3D"),
    ],
    "Automation, CRM & SEO": [
        ("Playwright", "lucide", "drama", "#2EAD33"), ("Chrome Extensions|(MV3)", "si", "googlechrome", "#4C8DF6"),
        ("FFmpeg", "si", "ffmpeg", "#3FB950"), ("Vitest", "si", "vitest", "#FCC72B"),
        ("Zoho CRM", "si", "zoho", "#F0483E"), ("Razorpay", "si", "razorpay", "#3395FF"),
        ("Technical SEO", "si", "googlesearchconsole", "#458CF5"),
    ],
    "Tools": [
        ("Git", "si", "git", "#F05032"), ("GitHub", "si", "github", WHITE),
        ("GitHub Actions", "si", "githubactions", "#2088FF"), ("Kubernetes", "si", "kubernetes", "#5C8DF6"),
        ("VS Code", "si11", "visualstudiocode", "#3AA0F3"),
    ],
}
# Each entry is one band of the card; two names in a band sit side by side.
BANDS = [["Languages"], ["Frontend", "Mobile"], ["Backend & Data"], ["Generative AI"],
         ["Automation, CRM & SEO"], ["Tools"]]
MAX_PER_ROW = 8

W, PAD, GAP, GROUP_GAP = 900, 26, 10, 24
TILE_H, HEAD_H, BAND_GAP, ICON = 84, 30, 16, 28
BG, BORDER, TILE_BG, TEXT, ACCENT, RULE = "#1a1b27", "#2f334d", "#1f2335", "#c0caf5", "#7aa2f7", "#2f334d"


def fetch(kind, name):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, f"{kind}-{name}.svg")
    if not os.path.exists(path):
        # curl uses the system certificate store; some Python installs ship without one.
        subprocess.run(["curl", "-fsSL", "--max-time", "30", "-o", path, SOURCES[kind].format(name)], check=True)
    return open(path, encoding="utf-8").read()


def icon(kind, name, color, x, y, size):
    raw = fetch(kind, name)
    root = re.search(r"<svg[^>]*>", raw, re.S).group(0)
    inner = re.search(r"<svg[^>]*>(.*)</svg>", raw, re.S).group(1)
    inner = re.sub(r"<title>.*?</title>", "", inner, flags=re.S).strip()
    inner = re.sub(r"<!--.*?-->", "", inner, flags=re.S)
    vb = re.search(r'viewBox="([^"]+)"', root).group(1)
    if kind == "lucide":
        paint = f'fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
    else:
        paint = f'fill="{color}" color="{color}"'
        if "evenodd" in root:
            paint += ' fill-rule="evenodd"'
    return f'<svg x="{x:.1f}" y="{y:.1f}" width="{size}" height="{size}" viewBox="{vb}" {paint}>{inner}</svg>'


def split_rows(items):
    if len(items) <= MAX_PER_ROW:
        return [items]
    first = (len(items) + 1) // 2
    return [items[:first], items[first:]]


def build():
    defs, body, n = [], [], 0
    inner_w = W - 2 * PAD
    y = PAD
    for band in BANDS:
        if len(band) == 1:
            spans = [(band[0], PAD, inner_w)]
        else:
            counts = [len(GROUPS[g]) for g in band]
            tile_w = (inner_w - GROUP_GAP * (len(band) - 1) - GAP * (sum(counts) - len(band))) / sum(counts)
            spans, x = [], PAD
            for g, c in zip(band, counts):
                gw = c * tile_w + (c - 1) * GAP
                spans.append((g, x, gw))
                x += gw + GROUP_GAP
        band_bottom = y
        for g, gx, gw in spans:
            label = html.escape(g.upper())
            text_w = len(g) * 9.4 + 10
            body.append(f'<text x="{gx:.1f}" y="{y + 14}" class="h">{label}</text>')
            body.append(f'<line x1="{gx + text_w:.1f}" y1="{y + 10}" x2="{gx + gw:.1f}" y2="{y + 10}" stroke="{RULE}" stroke-width="1"/>')
            ty = y + HEAD_H
            for row in split_rows(GROUPS[g]):
                tw = (gw - GAP * (len(row) - 1)) / len(row)
                for i, (lab, kind, name, color) in enumerate(row):
                    tx = gx + i * (tw + GAP)
                    n += 1
                    defs.append(f'<linearGradient id="t{n}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{color}" stop-opacity="{0.13 if color == WHITE else 0.24}"/><stop offset="1" stop-color="{color}" stop-opacity="0.04"/></linearGradient>')
                    lines = lab.split("|")
                    fs = 12.5
                    widest = max(len(l) for l in lines) * fs * 0.58
                    if widest > tw - 16:
                        fs = max(10.5, fs * (tw - 16) / widest)
                    two = len(lines) == 2
                    iy = ty + (9 if two else 14)
                    g_out = [f'<g class="t" style="animation-delay:{n * 0.025:.3f}s">',
                             f'<rect x="{tx:.1f}" y="{ty}" width="{tw:.1f}" height="{TILE_H}" rx="12" fill="{TILE_BG}"/>',
                             f'<rect x="{tx:.1f}" y="{ty}" width="{tw:.1f}" height="{TILE_H}" rx="12" fill="url(#t{n})" stroke="{color}" stroke-opacity="{0.28 if color == WHITE else 0.5}"/>',
                             icon(kind, name, color, tx + tw / 2 - ICON / 2, iy, ICON)]
                    base = ty + (52 if two else 64)
                    for k, l in enumerate(lines):
                        g_out.append(f'<text x="{tx + tw / 2:.1f}" y="{base + k * 15}" class="l" font-size="{fs:.1f}">{html.escape(l)}</text>')
                    g_out.append("</g>")
                    body.append("".join(g_out))
                ty += TILE_H + GAP
            band_bottom = max(band_bottom, ty - GAP)
        y = band_bottom + BAND_GAP
    H = y - BAND_GAP + PAD
    names = "; ".join(f"{g}: " + ", ".join(l.replace("|", " ") for l, *_ in items) for g, items in GROUPS.items())
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{html.escape(names)}">
<title>Core stack</title>
<style>
.h{{font:700 12px -apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;letter-spacing:2px;fill:{ACCENT}}}
.l{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;font-weight:600;fill:{TEXT};text-anchor:middle}}
.t{{animation:rise .5s ease-out both}}
@keyframes rise{{from{{opacity:0;transform:translateY(6px)}}to{{opacity:1;transform:none}}}}
@media (prefers-reduced-motion:reduce){{.t{{animation:none}}}}
</style>
<defs>
<linearGradient id="bar" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7aa2f7"/><stop offset=".5" stop-color="#bb9af7"/><stop offset="1" stop-color="#f7768e"/></linearGradient>
<clipPath id="card"><rect width="{W}" height="{H}" rx="16"/></clipPath>
{"".join(defs)}
</defs>
<rect x=".5" y=".5" width="{W - 1}" height="{H - 1}" rx="16" fill="{BG}" stroke="{BORDER}"/>
<rect width="{W}" height="4" fill="url(#bar)" clip-path="url(#card)"/>
{chr(10).join(body)}
</svg>
'''
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {OUT}  {W}x{H}  tiles={n}  bytes={len(svg)}")
    return names


if __name__ == "__main__":
    build()
