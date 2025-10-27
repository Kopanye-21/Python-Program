print("🤖 Hello! I'm SmartCareerBot — your tech career guide.\n")
print("Answer these questions to find the best tech career path for you!\n")

# Initialize scores
scores = {
    "coding": 0,
    "data": 0,
    "security": 0,
    "design": 0,
    "hardware": 0
}

# Questions and options
questions = [
    "1️⃣ What do you enjoy most?\n(a) Building apps\n(b) Analyzing numbers\n(c) Finding system weaknesses\n(d) Creating graphics\n(e) Fixing devices",
    "2️⃣ Which school subject do you like most?\n(a) Computer Studies\n(b) Maths/Statistics\n(c) Networking\n(d) Art/Design\n(e) Physics/Electronics",
    "3️⃣ What type of work do you enjoy?\n(a) Writing code\n(b) Studying patterns\n(c) Protecting information\n(d) Designing interfaces\n(e) Assembling machines",
    "4️⃣ Which sounds most exciting?\n(a) Developing a mobile app\n(b) Predicting trends from big data\n(c) Stopping hackers\n(d) Designing a game UI\n(e) Building a robot",
    "5️⃣ Which tool would you like to master?\n(a) Python or Java\n(b) SQL or Excel\n(c) Firewalls\n(d) Figma or Photoshop\n(e) Arduino or Raspberry Pi"
]

# Loop through questions
for q in questions:
    print("\n" + q)
    answer = input("Choose (a/b/c/d/e): ").lower()

    # Use conditionals to add scores
    if answer == "a":
        scores["coding"] += 1
    elif answer == "b":
        scores["data"] += 1
    elif answer == "c":
        scores["security"] += 1
    elif answer == "d":
        scores["design"] += 1
    elif answer == "e":
        scores["hardware"] += 1
    else:
        print("Invalid choice. Skipping question.")
        continue

# Decide the best career based on max score
best_field = max(scores, key=scores.get)

career_recommendations = {
    "coding": "Software Developer or Web Developer",
    "data": "Data Scientist or Data Analyst",
    "security": "Cybersecurity Specialist",
    "design": "UI/UX Designer",
    "hardware": "Computer Engineer or Embedded Systems Engineer"
}

print("\n🔍 Analyzing your results...\n")

print(f"✅ Based on your answers, you’d make a great {career_recommendations[best_field]}!")
print("\n📘 Tip: Keep learning and build personal projects in that area to strengthen your skills.")
print("Good luck on your tech journey 🚀")