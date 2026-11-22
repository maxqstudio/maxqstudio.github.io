---
name: pretio-public-content-updater
description: Maintain Pretio official Catalog Promo links and discounted country Product Highlights with evidence, per-catalog checklists, 12-hour country targets, compact context handoffs, exact existing JSON schemas, and deterministic expiry cleanup.
---

# Pretio Public Content Updater (GitHub Copilot entrypoint)

Follow the canonical skill at:
`.agents/skills/pretio-public-content-updater/SKILL.md`

Read that SKILL.md **in full**, then its linked references and checklist templates **before** processing any Pretio catalog or highlight. All restrictions and gates in the canonical skill are mandatory.

Do not add any JSON field not already supported by Pretio, do not invent discounts to meet the 1-per-country/12h target, prefer evergreen catalog URLs, require a real expiry for rotating catalog links, remove proven-expired highlights, and create a separate compact context after each catalog.

This file is only an agent discovery alias for GitHub Copilot. The canonical rules live in the Codex-compatible `.agents/skills/` location; avoid duplicating or diverging policies.
