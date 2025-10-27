# Simple Tech Career Chatbot
print("👋 Hello! I'm CareerBot, your tech career guide.")
print("Let's find out which tech career suits you best!\n")

# Dictionary of interests and possible careers
careers = {
    "coding": "Software Developer or Web Developer",
    "data": "Data Scientist or Data Analyst",
    "security": "Cybersecurity Specialist",
    "design": "UI/UX Designer",
    "hardware": "Computer Engineer or Embedded Systems Engineer"
}

# Loop to keep asking until valid input
while True:
    interest = input("What interests you most? (coding/data/security/design/hardware): ").lower()

    # Conditional to match interest with career
    if interest in careers:
        print(f"\nAwesome! Based on your interest in {interest}, "
              f"you could pursue a career as a {careers[interest]}.\n")
        break
    else:
        print("Hmm 🤔 I didn't get that. Please choose one of the options above.\n")
        continue

# More personalized advice
extra = input("Would you like some study advice? (yes/no): ").lower()

if extra == "yes":
    print("\n📘 Tip: Focus on building projects and learning core programming languages early.")
    print("You can also join hackathons or online coding communities!\n")
else:
    print("\nAlright! Wishing you the best on your tech journey 🚀")

print("Goodbye! 👋")