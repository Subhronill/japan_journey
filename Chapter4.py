# Japan Progress Tracker — Chapter 4
# A function-based system to track your mission

def assess_python(days_studied):
    if days_studied < 7:
        return "Week 1 — fundamentals"
    elif days_studied < 30:
        return "Month 1 — building base"
    elif days_studied < 90:
        return "Quarter 1 — getting real"
    else:
        return "Solid foundation — start projects"

def assess_japanese(hiragana_rows, anki_cards):
    if hiragana_rows < 3:
        return "Hiragana incomplete — keep going"
    elif hiragana_rows < 10:
        return f"{hiragana_rows}/10 rows — making progress"
    else:
        if anki_cards < 200:
            return "Hiragana done — build vocabulary"
        else:
            return "Strong foundation — aim for N5"

def assess_github(repos, commits):
    score = repos * 10 + commits
    if score < 20:
        return "Just started — push code daily"
    elif score < 50:
        return "Growing — keep committing"
    else:
        return "Active profile — recruiters notice this"

def full_mission_report(name, python_days, hiragana_rows,
                         anki_cards, repos, commits):
    print("=" * 40)
    print(f"  MISSION REPORT — {name.upper()}")
    print("=" * 40)
    print(f"Python:   {assess_python(python_days)}")
    print(f"Japanese: {assess_japanese(hiragana_rows, anki_cards)}")
    print(f"GitHub:   {assess_github(repos, commits)}")
    print("=" * 40)
    print("Target: Tokyo 2030. Keep moving.")
    print("=" * 40)

full_mission_report(
    name="Subhronil",
    python_days=1,
    hiragana_rows=3,
    anki_cards=10,
    repos=1,
    commits=3
)