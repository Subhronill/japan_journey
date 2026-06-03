# Japan Readiness Checker
# Chapter 2 — Day 0

python_days = 1          # days you have studied Python
japanese_cards = 10      # total Anki cards reviewed
github_repos = 1         # number of repos on your GitHub
jlpt_level = 0           # current JLPT level (0 = none)
year = 2026

print("=== JAPAN READINESS REPORT ===")
print(f"Date: June 2026")
print(f"Target: Tokyo by 2030")
print()

if python_days < 30:
    python_status = "Beginner — keep going daily"
elif python_days < 180:
    python_status = "Intermediate — real progress"
else:
    python_status = "Advanced — strong foundation"

if japanese_cards < 50:
    japanese_status = "Just started — trust the process"
elif japanese_cards < 500:
    japanese_status = "Building — do not break the streak"
else:
    japanese_status = "Strong — Anki is working"

if github_repos == 0:
    github_status = "Empty — fix this today"
elif github_repos < 5:
    github_status = "Starting — keep pushing code"
else:
    github_status = "Active — recruiters will notice"

print(f"Python:   {python_status}")
print(f"Japanese: {japanese_status}")
print(f"GitHub:   {github_status}")
print()
print("Status: MISSION ACTIVE. 2030 is the deadline.")