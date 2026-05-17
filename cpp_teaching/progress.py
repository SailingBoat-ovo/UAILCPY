import json
import os
from datetime import datetime

PROGRESS_FILE = os.path.join(os.path.dirname(__file__), "progress.json")


def _default(lang):
    return {
        "current_lesson": 0,
        "current_step": 0,
        "completed_lessons": {},
        "start_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "language": lang
    }


def load_progress(lang="cpp"):
    if not os.path.exists(PROGRESS_FILE):
        return _default(lang)
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    if "language" not in data:
        data = _default(lang)
    if "current_step" not in data:
        data["current_step"] = 0
    return data


def save_progress(progress):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=2)


def save_current_pos(lesson_id, step_idx, lang="cpp"):
    progress = load_progress(lang)
    progress["current_lesson"] = lesson_id
    progress["current_step"] = step_idx
    progress["language"] = lang
    save_progress(progress)


def load_current_pos(lang="cpp"):
    progress = load_progress(lang)
    return progress.get("current_lesson", 0), progress.get("current_step", 0)


def mark_lesson_completed(lesson_id, lesson_name, lang="cpp"):
    progress = load_progress(lang)
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    key = f"{lang}_{lesson_id}"
    progress["completed_lessons"][key] = {
        "name": lesson_name,
        "completed_at": today,
        "language": lang
    }
    if lang == progress.get("language", "cpp"):
        if lesson_id >= progress["current_lesson"]:
            progress["current_lesson"] = lesson_id + 1
        progress["current_step"] = 0
    progress["language"] = lang
    save_progress(progress)
    return progress


def get_current_lesson(lang="cpp"):
    progress = load_progress(lang)
    return progress["current_lesson"]


def get_progress_data(lang="cpp"):
    return load_progress(lang)


def is_completed(lesson_id, lang="cpp"):
    progress = load_progress(lang)
    return f"{lang}_{lesson_id}" in progress["completed_lessons"]


def get_completed_count(lang="cpp"):
    progress = load_progress(lang)
    count = 0
    for k in progress["completed_lessons"]:
        if k.startswith(f"{lang}_"):
            count += 1
    return count
