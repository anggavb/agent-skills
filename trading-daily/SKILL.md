---
name: trading-daily
description: Research and produce an evidence-based pre-market morning brief for the Indonesian stock market (IDX). Use when analyzing fresh market news, overnight macro conditions, commodities, Indonesian companies, catalysts, and daily IDX trading candidates before market open.
version: 1.0.0
metadata:
  hermes:
    tags:
      - trading
      - idx
      - indonesia
      - stocks
      - finance
      - market-research
    category: finance
---

# Trading Daily

Produce an evidence-based morning trading brief for the Indonesian stock market.

Default timezone:

Asia/Jakarta

Default market:

Indonesia Stock Exchange / IDX

The purpose is decision support.

Do not execute trades.
Do not claim guaranteed returns.
Do not fabricate market data, news, prices, sources, or company information.

---

# Required Workflow

For every morning brief:

1. Determine the current date and time in Asia/Jakarta.

2. Determine whether IDX is expected to trade today.

3. Load and follow:

   `skill_view("trading-daily", "references/research-workflow.md")`

4. Apply source verification rules from:

   `skill_view("trading-daily", "references/source-policy.md")`

5. For stocks identified during research, evaluate them using:

   `skill_view("trading-daily", "references/candidate-scoring.md")`

6. Apply final action classification using:

   `skill_view("trading-daily", "references/decision-rules.md")`

7. Format the final response using:

   `skill_view("trading-daily", "templates/telegram-morning-brief.md")`

Do not skip these steps for scheduled morning reports.

---

# Research Principles

Prioritize information from approximately the previous 18 hours.

Older information may be used as context but must not be presented as a new catalyst.

Cluster duplicate articles describing the same event into a single story.

Separate:

FACT
→ INTERPRETATION
→ EXPECTED MARKET IMPACT

Do not confuse media attention with financial importance.

Do not select a stock simply because it appears frequently in news.

Every actionable candidate must have a clear transmission mechanism:

EVENT
→ BUSINESS IMPACT
→ SECTOR IMPACT
→ COMPANY EXPOSURE
→ POSSIBLE MARKET REACTION

Prefer liquid and actively traded Indonesian equities.

Prefer current IDX30, LQ45, sector leaders, and other sufficiently liquid names.

Do not hardcode index membership. Verify current membership when it matters.

---

# Research Failure Rules

If current information cannot be verified:

say so.

If market price data cannot be obtained reliably:

do not invent technical analysis.

If a catalyst cannot be confirmed:

label it UNCONFIRMED and do not classify the stock as CONSIDER BUY.

If evidence is contradictory:

describe the contradiction.

If there are no sufficiently strong opportunities:

return:

"No sufficiently strong candidate today."

This is a valid and preferred result over forcing a recommendation.

---

# Output Limits

Select no more than 3 actionable stocks.

Prefer:

1 strong candidate

over:

3 weak candidates.

The final Telegram brief should normally fit comfortably within a single readable Telegram message.

Do not expose internal reasoning, scoring calculations, or research scratchpad unless explicitly requested.

Present conclusions and evidence only.