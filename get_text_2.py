import json, re

with open("output/02_text_res.json", "r", encoding="utf-8") as f:
    data = json.load(f)

MIN_CONF = 0.85
def reverse_arabic_runs(s: str) -> str:
    # reverse only Arabic letter spans; keep digits/Latin as-is
    return re.sub(r'[\u0600-\u06FF]+', lambda m: m.group(0)[::-1], s)

def y_center(b): return (b[1] + b[3]) / 2.0
def x_right(b):  return b[2]

lines = []
for t, sc, b in zip(data["rec_texts"], data["rec_scores"], data["rec_boxes"]):
    if sc >= MIN_CONF:
        lines.append({"text": reverse_arabic_runs(t), "score": sc, "box": b})

lines.sort(key=lambda r: (round(y_center(r["box"]) / 30), -x_right(r["box"])))
full_text = "\n".join([r["text"] for r in lines])
print(full_text)
open("ocr_arabic.txt", "w", encoding="utf-8").write(full_text)