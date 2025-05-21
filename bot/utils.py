import json

def load_translations(lang_code):
    with open(f"bot/translations/{lang_code}.json", "r", encoding="utf-8") as f:
        return json.load(f)

def validate_interval(value):
    if not (900 <= value <= 86400):
        raise ValueError("Interval must be between 15 minutes and 24 hours")
