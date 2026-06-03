# Hiragana Trainer — Chapter 3
# Tests your knowledge of the characters learned so far

hiragana = {
    "あ": "a",
    "い": "i",
    "う": "u",
    "え": "e",
    "お": "o",
    "か": "ka",
    "き": "ki",
    "く": "ku",
    "け": "ke",
    "こ": "ko",
}

print("=== HIRAGANA TRAINER ===")
print(f"Testing {len(hiragana)} characters\n")

correct = 0
total = 0

for character, reading in hiragana.items():
    print(f"Character: {character}")
    answer = input("Reading: ")
    
    if answer.lower() == reading:
        print("Correct!\n")
        correct += 1
    else:
        print(f"Wrong. It is: {reading}\n")
    
    total += 1

print(f"Score: {correct}/{total}")

if correct == total:
    print("Perfect score. Your brain is working.")
elif correct >= total * 0.7:
    print("Good. Keep reviewing with Anki.")
else:
    print("Keep practicing. Repetition is the path.")