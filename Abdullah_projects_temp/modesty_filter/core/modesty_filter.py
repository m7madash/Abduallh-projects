"""
وضع غض البصر — Modesty Filter for Social Platforms
الهدف: حماية المستخدمين (خاصة الرجال) من المحتوى النسائي المثير
الضوابط: الشرعية (غض البصر) + الخصوصية + فعالية
"""

import json
import os
from dataclasses import dataclass, asdict
from typing import List, Set, Optional
from pathlib import Path

# ── إعدادات ──────────────────────────────────────────────
CONFIG_PATH = Path("config/settings.json")
# ──────────────────────────────────────────────────────────

@dataclass
class ModestyConfig:
    enabled: bool = True
    user_gender: str = "male"  # "male" or "female"
    strict_mode: bool = False  # stricter filtering
    allow_educational: bool = True  #允许 محتوى تعليمي (صحة، دين)
    blocked_categories: List[str] = None
    allowed_educational_tags: List[str] = None

    def __post_init__(self):
        if self.blocked_categories is None:
            self.blocked_categories = [
                "swimsuit", "lingerie", "tight clothing", "modeling",
                "dating", "intimate", "body exposure", "provocative",
                " Cosmetic", "beauty_ads", "fitness_model"
            ]
        if self.allowed_educational_tags is None:
            self.allowed_educational_tags = [
                "health education", "islamic", "awareness", "psychology",
                "medical", "religious", "family", "education"
            ]


class ModestyFilter:
    """ فلترة المحتوى بناءً على إعدادات المستخدم والضوابط الشرعية """

    def __init__(self, config_path: str = CONFIG_PATH):
        self.config = self._load_config(config_path)

    def _load_config(self, path: Path) -> ModestyConfig:
        if path.exists():
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return ModestyConfig(**data)
        return ModestyConfig()

    def save_config(self, path: Path = CONFIG_PATH):
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(asdict(self.config), f, ensure_ascii=False, indent=2)

    # ── Public API ─────────────────────────────────────────
    def should_hide_post(self, post: dict) -> bool:
        """
        قرر إذا كان يجب إخفاء المنشور.
        post: {id, text, category: str, tags: List[str], media_type: str, gender_focus: str}
        """
        if not self.config.enabled:
            return False

        # 1. فحص الفئة المحظورة
        if post.get("category") in self.config.blocked_categories:
            # استثناء: المحتوى التعليمي مسموح به
            if self.config.allow_educational and self._is_educational(post):
                return False
            return True

        # 2. فحص التركيز النسائي (للمستخدمين الذكور)
        if self.config.user_gender == "male":
            if self._is_female_focused(post):
                # التعليمي مسموح
                if self.config.allow_educational and self._is_educational(post):
                    return False
                return True

        # 3. وضع صارم: حظر إعلانات الجمال/الموضة للذكور
        if self.config.strict_mode and self.config.user_gender == "male":
            if post.get("category") in ["fashion", "beauty", "cosmetics"]:
                return True

        return False

    def _is_educational(self, post: dict) -> bool:
        tags = set(post.get("tags", []))
        return any(tag in self.config.allowed_educational_tags for tag in tags)

    def _is_female_focused(self, post: dict) -> bool:
        """ي Lawrence如果 المحتوى موجه للنساء أو يظهر بشكل نسائي"""
        # علامات نصية
        text_lower = post.get("text", "").lower()
        female_keywords = ["نساء", "نسوان", "بنات", "أنثى", "حريم", "م massa"]
        if any(kw in text_lower for kw in female_keywords):
            return True

        # وسوم
        tags = set(post.get("tags", []))
        female_tags = ["women", "female", "girls", "ladies", "fashion", "beauty"]
        if any(tag in female_tags for tag in tags):
            return True

        # نوع الإعلام
        if post.get("media_type") == "image":
            # في التطبيق الكامل: vision model here
            # حالياً: نعتمد على العلامات الوصفية
            pass

        return False

    # ── Helper ─────────────────────────────────────────────
    def get_filter_summary(self, total_posts: int, hidden_count: int) -> str:
        return (f"🛡️ Modesty Mode: {hidden_count}/{total_posts} posts filtered "
                f"({100*hidden_count/max(total_posts,1):.0f}%)")


# ── CLI用于 manual testing ─────────────────────────────────
if __name__ == "__main__":
    import sys
    import argparse

    parser = argparse.ArgumentParser(description="Modesty Filter CLI")
    parser.add_argument("--enable", action="store_true", help="Enable filter")
    parser.add_argument("--disable", action="store_true", help="Disable filter")
    parser.add_argument("--gender", choices=["male", "female"], help="Set user gender")
    parser.add_argument("--strict", action="store_true", help="Enable strict mode")
    parser.add_argument("--status", action="store_true", help="Show current config")
    parser.add_argument("--test-post", type=str, help="Test a post JSON file")
    args = parser.parse_args()

    filter = ModestyFilter()

    if args.enable:
        filter.config.enabled = True
        filter.save_config()
        print("✅ Modesty Mode enabled")
    elif args.disable:
        filter.config.enabled = False
        filter.save_config()
        print("❌ Modesty Mode disabled")

    if args.gender:
        filter.config.user_gender = args.gender
        filter.save_config()
        print(f"👤 Gender set to: {args.gender}")

    if args.strict:
        filter.config.strict_mode = True
        filter.save_config()
        print("🔒 Strict mode enabled")

    if args.status:
        print("📋 Current Modesty Filter Config:")
        print(json.dumps(asdict(filter.config), indent=2, ensure_ascii=False))

    if args.test_post:
        with open(args.test_post, "r", encoding="utf-8") as f:
            post = json.load(f)
        hidden = filter.should_hide_post(post)
        print(f"🎯 Post {'HIDDEN' if hidden else 'VISIBLE'}: {post.get('category')}")
        if hidden:
            print(f"   Reason: female-focused={filter._is_female_focused(post)}, "
                  f"educational={filter._is_educational(post)}")
