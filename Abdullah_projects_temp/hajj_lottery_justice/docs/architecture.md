# 📐 Architecture: Hajj Lottery Justice

## 🎯 Problem Statement
Design a fair selection system for Hajj that aligns with Islamic principle: "خير الزاد التقوى" while acknowledging that true taqwa is known only to Allah.

## 🔍 Constraints
- Cannot measure actual taqwa (hearts are hidden)
- Must be transparent and auditable
- Must protect the poor and needy (Islamic priority)
- Must avoid discrimination (ethnicity, nationality, etc.)
- Must be resistant to gaming/cheating

## 📊 Proposed Solution: **Taqwa-Proxied Score + Lottery**

### **Scoring Components (100 points total)**

| Component | Weight | Proxy Rationale |
|-----------|--------|-----------------|
| Income (need) | 30% | Poverty indicates higher reliance on Allah; more deserving |
| Age (seniority) | 15% | Older pilgrims have health risks; priority from Sunnah (care for elderly) |
| Health conditions | 15% | Chronic illness/disability increases hardship; Islamic emphasis on easing burdens |
| Hajj count (novelty) | 20% | First-timers have not yet performed Hajj; more deserving than repeaters |
| Community service | 10% | Volunteering reflects social righteousness (proxy for taqwa) |
| Fasting consistency | 10% | Regular fasting indicates.commitment to worship (proxy for taqwa) |

### **Process Flow**

```
1. Applicant submits form with verifiable data
2. Verification: income proof, health certificate, hajj records, service logs, fasting declaration
3. Scoring: automated calculation based on weights
4. Cutoff: select top 50% of scores
5. Lottery: random draw among qualified pool
6. Notification: winners + their score breakdown
7. Appeal: evidence review for errors
```

### **Transparency Features**
- Every applicant sees their exact score and component points.
- Public anonymized list of winners and their scores.
- Open-source algorithm and weights.
- Annual audit by third-party Islamic scholars.

### **Fairness Guarantees**
- **No pure luck:** Poor/ill/first-time applicants have higher baseline scores.
- **No corruption:** Automated scoring, no human bias.
- **No discrimination:** Explicitly forbidden by design.
- **Appealability:** Evidence-based review process.

## 🕌 Islamic Compliance

| Principle | Implementation |
|-----------|----------------|
| خير الزاد التقوى | Proxy-based scoring approximates taqwa without claiming certainty |
| لا ضرر ولا ضرار | Need-based weights protect the vulnerable |
| العدالة | Lottery among qualified ensures equal chance within tiers |
| الشفافية | Full score disclosure, open algorithm |
| عدم التمييز | No ethnic, national, or gender bias (all weights neutral) |

---

## 📈 Example Scoring

```json
{
  "applicant_id": "AHMED_001",
  "income": 15000,         // low → 30 pts
  "age": 68,               // elderly → 15 pts
  "health": "chronic",     // → 15 pts
  "hajj_count": 0,         // first-time → 20 pts
  "community_hours": 120,  // high → 10 pts
  "fasting": "consistent", // → 10 pts
  "total_score": 100,
  "percentage": 100.0,
  "status": "certain_selection"
}
```

---

## 🛠️ Implementation Phases

1. **MVP:** Basic scorer + simple lottery (this repo)
2. **Pilot:** Test with small community (100 applicants)
3. **Scale:** Integrate with official Hajj portals
4. **Audit:** Third-party fairness and Islamic compliance review

---

## 📜 License
MIT — Open for contributions that respect the above principles.

🕌 *"خير الزاد التقوى" — Quran 2:197*