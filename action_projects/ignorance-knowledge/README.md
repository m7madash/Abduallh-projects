# Ignorance → Knowledge — Fact-Checking Bot

## Mission
Automated verification of claims on social media using multiple independent sources.

## Today's Action (2026-04-18)
- Researched fact-checking APIs (Google Fact Check, FactCheck.org, Snopes)
- Designed claim extraction pipeline (NLP-based)
- Planned multi-source verification flow

## Architecture
1. **Crawl**: Monitor social media posts for potential claims
2. **Extract**: Identify factual assertions (NLP)
3. **Search**: Query trusted sources (news outlets, NGOs, official reports, academic papers)
4. **Compare**: Cross-reference multiple sources (minimum 3 independent)
5. **Verdict**: Generate verdict with citations (TRUE / FALSE / MISLEADING / UNVERIFIED)
6. **Post**: Share correction with evidence

## Tech Stack
- Backend: Python (FastAPI)
- NLP: spaCy or transformers for claim detection
- Search: Google Fact Check API, NewsAPI, Wikipedia API
- Database: SQLite for tracking claims
- Deployment: Cloud function or small VPS

## Next Actions
- Build claim extractor module
- Integrate search APIs
- Create test suite with known claims
- Deploy demo bot on test account

## How to Contribute
1. Fork this repo
2. Implement a module (extractor, searcher, verdict generator)
3. Submit PR with tests
4. Deploy and share results

🔗 **Parent repo:** https://github.com/m7madash/Abduallh-projects
