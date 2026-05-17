import json
import os
from datetime import datetime, date, timedelta

CALENDAR_FILE = os.path.join(os.path.dirname(__file__), "calendar.json")


def _default():
    return {}


def load_calendar():
    if not os.path.exists(CALENDAR_FILE):
        return _default()
    try:
        with open(CALENDAR_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return _default()


def save_calendar(data):
    with open(CALENDAR_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def record_study(lang="python", lessons_done=0, steps_done=0, run_check=False):
    data = load_calendar()
    today_str = date.today().isoformat()
    if today_str not in data:
        data[today_str] = {
            "study_minutes": 0,
            "lessons_completed": 0,
            "steps_done": 0,
            "checks_done": 0,
            "languages": []
        }
    entry = data[today_str]
    if lessons_done > 0:
        entry["lessons_completed"] = entry.get("lessons_completed", 0) + lessons_done
    if steps_done > 0:
        entry["steps_done"] = entry.get("steps_done", 0) + steps_done
    if run_check:
        entry["checks_done"] = entry.get("checks_done", 0) + 1
    langs = entry.get("languages", [])
    if lang not in langs:
        langs.append(lang)
    entry["languages"] = langs
    entry["study_minutes"] = entry.get("study_minutes", 0) + 1
    save_calendar(data)


def get_month_data(year, month):
    data = load_calendar()
    result = {}
    first = date(year, month, 1)
    if month == 12:
        last = date(year + 1, 1, 1) - timedelta(days=1)
    else:
        last = date(year, month + 1, 1) - timedelta(days=1)
    d = first
    while d <= last:
        ds = d.isoformat()
        result[ds] = data.get(ds, None)
        d += timedelta(days=1)
    return result


def get_month_stats(year, month):
    month_data = get_month_data(year, month)
    total_days = 0
    total_lessons = 0
    total_steps = 0
    total_checks = 0
    total_minutes = 0
    for ds, entry in month_data.items():
        if entry is not None:
            total_days += 1
            total_lessons += entry.get("lessons_completed", 0)
            total_steps += entry.get("steps_done", 0)
            total_checks += entry.get("checks_done", 0)
            total_minutes += entry.get("study_minutes", 0)
    return {
        "total_days": total_days,
        "total_lessons": total_lessons,
        "total_steps": total_steps,
        "total_checks": total_checks,
        "total_minutes": total_minutes
    }


def get_all_stats():
    data = load_calendar()
    total_days = len(data)
    total_lessons = 0
    total_steps = 0
    total_checks = 0
    total_minutes = 0
    first_date = None
    for ds, entry in data.items():
        if first_date is None or ds < first_date:
            first_date = ds
        total_lessons += entry.get("lessons_completed", 0)
        total_steps += entry.get("steps_done", 0)
        total_checks += entry.get("checks_done", 0)
        total_minutes += entry.get("study_minutes", 0)
    return {
        "total_days": total_days,
        "total_lessons": total_lessons,
        "total_steps": total_steps,
        "total_checks": total_checks,
        "total_minutes": total_minutes,
        "first_date": first_date or "今天"
    }
