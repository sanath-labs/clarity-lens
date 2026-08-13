import json
from flag_detector import analyze_sentence

with open("data/sample_texts.json") as f:
    samples = json.load(f)

for text in samples:
    result = analyze_sentence(text)
    print(result)
    print("-" * 40)
