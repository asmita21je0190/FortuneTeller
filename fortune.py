# fortune.py v1.0

print("🔮 Welcome to Asmita Verma's Fortune Teller (21JE0190) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral): ")

if mood.lower() == "happy":
    print("✨ Your fortune: Great things await you, Asmita! Keep smiling. ✨")
elif mood.lower() == "sad":
    print("🌧️ Your fortune: Tough times don’t last. Hang in there! 🌈")
elif mood.lower() == "neutral":
    print("🌤️ Your fortune: A surprise is just around the corner. Be ready! 🌟")
else:
    print("Hmm... I can't sense your mood. Try again later.")
