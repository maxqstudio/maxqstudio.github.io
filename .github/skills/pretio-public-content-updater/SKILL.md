---
name: pretio-public-content-updater
description: Maintain Pretio official Catalog Promo links and discounted country Product Highlights with evidence, per-catalog checklists, 12-hour country targets, compact context handoffs, exact existing JSON schemas, and deterministic expiry cleanup.
---

# Pretio Public Content Updater (GitHub Copilot entrypoint)

Follow the canonical skill at:
`.agents/skills/pretio-public-content-updater/SKILL.md`

Read that SKILL.md **in full**, including its **online-shop-marketplace-rules.md** reference and **ONLINE_SHOP_CHECKLIST.md** template, before processing any Pretio catalog, online shop, marketplace seller, or highlight. Include direct online merchants and permitted marketplace product offers; Google Shopping is authorized discovery only, not price evidence. All restrictions and gates in the canonical skill are mandatory.

Honor the Owner's explicit scope override: **"kerjakan 1 kali saja untuk Indonesia" means one isolated Indonesia-only execution and STOP**, not a global or recurring scan. A product without a dedicated landing page may use a verified official catalog promo landing URL as `source_url` with proof of that exact discount. Omit unknown optional fields; do not invent required data.

Do not add any JSON field not already supported by Pretio, do not invent discounts to meet the 1-per-country/12h target, prefer evergreen catalog URLs, require a real expiry for rotating catalog links, remove proven-expired highlights, and create a separate compact context after each catalog.

This file is only an agent discovery alias for GitHub Copilot. The canonical rules live in the Codex-compatible `.agents/skills/` location; avoid duplicating or diverging policies.
