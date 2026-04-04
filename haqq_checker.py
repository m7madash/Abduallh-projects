import sys
import json

def verify_content(query):
    # هذه مسودة للأداة التي سنطورها لربط البحث بالضوابط
    print(f"🔎 جاري التحقق من: {query}")
    print("ضوابط HaqqBot:")
    print("- التأكد من السند (للأحاديث)")
    print("- رفض التفسير بالرأي")
    print("- القول بـ 'لا أعلم' عند غياب الدليل")
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        verify_content(" ".join(sys.argv[1:]))
