"""
نظام تقييم استحقاق الحج — Hajj Lottery Scorer
الهدف: تحديد من يستحق الحج بناءً على معايير قابلة للقياس (proxy for التقوى والظروف)
"""

import json
from pathlib import Path
from typing import Dict, Any
from datetime import datetime

# ── Config ──────────────────────────────────────────────
CONFIG_PATH = Path(__file__).parent.parent / "config" / "weights.json"
# ──────────────────────────────────────────────────────────

class HajjScorer:
    """ يحسب نقاط المتقدم للحج بناءً على معايير متعددة """

    def __init__(self, config_path: Path = CONFIG_PATH):
        with open(config_path, 'r', encoding='utf-8') as f:
            self.config = json.load(f)
        self.weights = self.config['weights']
        self.thresholds = self.config['thresholds']

    def calculate_score(self, applicant: Dict[str, Any]) -> int:
        """
        applicant keys:
        - income: annual income in USD
        - age: int
        - health: "none" | "chronic" | "disability"
        - hajj_count: int (number of previous Hajj performances)
        - community_service_hours: int
        - fasting_consistency: "consistent" | "occasional" | "inconsistent"
        """
        score = 0

        # 1. Income (30%)
        income = applicant.get('income', 0)
        income_points = self._get_income_points(income)
        score += income_points

        # 2. Age (15%)
        age = applicant.get('age', 30)
        age_points = self._get_age_points(age)
        score += age_points

        # 3. Health (15%)
        health = applicant.get('health', 'none')
        health_points = self.thresholds['health_conditions'][health]['points']
        score += health_points

        # 4. Hajj count (20%) — first time gets more
        count = applicant.get('hajj_count', 0)
        if count == 0:
            hajj_points = self.thresholds['hajj_novelty']['first_time']['points']
        elif count == 1:
            hajj_points = self.thresholds['hajj_novelty']['once_before']['points']
        else:
            hajj_points = self.thresholds['hajj_novelty']['multiple']['points']
        score += hajj_points

        # 5. Community service (10%)
        hours = applicant.get('community_service_hours', 0)
        service_points = self._get_service_points(hours)
        score += service_points

        # 6. Fasting consistency (10%)
        fasting = applicant.get('fasting_consistency', 'inconsistent')
        fasting_points = self.thresholds['fasting_consistency'][fasting]['points']
        score += fasting_points

        return score

    def _get_income_points(self, income: int) -> int:
        levels = self.thresholds['income_levels']
        if income <= levels['low']['max']:
            return levels['low']['points']
        elif income <= levels['medium']['max']:
            return levels['medium']['points']
        else:
            return levels['high']['points']

    def _get_age_points(self, age: int) -> int:
        groups = self.thresholds['age_groups']
        if age >= groups['elderly']['min']:
            return groups['elderly']['points']
        elif age >= groups['middle']['min']:
            return groups['middle']['points']
        else:
            return groups['young']['points']

    def _get_service_points(self, hours: int) -> int:
        groups = self.thresholds['community_service_hours']
        if hours >= groups['high']['min']:
            return groups['high']['points']
        elif hours >= groups['medium']['min']:
            return groups['medium']['points']
        else:
            return groups['low']['points']

    def evaluate_applicant(self, applicant: Dict[str, Any]) -> Dict[str, Any]:
        """إرجاع تقرير كامل عن التقييم"""
        score = self.calculate_score(applicant)
        max_score = sum(self.weights.values())
        percentage = (score / max_score) * 100

        return {
            "applicant_id": applicant.get('applicant_id', 'unknown'),
            "score": score,
            "max_possible": max_score,
            "percentage": round(percentage, 1),
            "breakdown": {
                "income": self._get_income_points(applicant.get('income', 0)),
                "age": self._get_age_points(applicant.get('age', 30)),
                "health": self.thresholds['health_conditions'][applicant.get('health','none')]['points'],
                "hajj_novelty": self._get_hajj_novelty_points(applicant.get('hajj_count', 0)),
                "community_service": self._get_service_points(applicant.get('community_service_hours', 0)),
                "fasting_consistency": self.thresholds['fasting_consistency'][applicant.get('fasting_consistency','inconsistent')]['points']
            }
        }

    def _get_hajj_novelty_points(self, count: int) -> int:
        if count == 0:
            return self.thresholds['hajj_novelty']['first_time']['points']
        elif count == 1:
            return self.thresholds['hajj_novelty']['once_before']['points']
        else:
            return self.thresholds['hajj_novelty']['multiple']['points']


# ── CLI ──────────────────────────────────────────────────
if __name__ == "__main__":
    import argparse
    import sys

    parser = argparse.ArgumentParser(description="Hajj Lottery Scorer CLI")
    parser.add_argument("--applicant", type=str, help="Path to applicant JSON file")
    parser.add_argument("--list", action="store_true", help="Show scoring breakdown")
    args = parser.parse_args()

    scorer = HajjScorer()

    if args.applicant:
        with open(args.applicant, 'r', encoding='utf-8') as f:
            applicant_data = json.load(f)
        result = scorer.evaluate_applicant(applicant_data)
        print(json.dumps(result, indent=2, ensure_ascii=False))
    elif args.list:
        print("📊 Scoring Breakdown:")
        print(json.dumps(scorer.weights, indent=2, ensure_ascii=False))
    else:
        parser.print_help()