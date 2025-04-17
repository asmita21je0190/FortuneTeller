# fortune.py v1.1

import random

print("🔮 Welcome to Asmita Verma's Fortune Teller (21JE0190) 🔮")
mood = input("How are you feeling today? (happy/sad/neutral/stressed): ")

fortunes = {
    "happy": [
        "✨ Great things await you, Asmita! Keep smiling. ✨",
        "🌟 Joy will follow your path today!"
    ],
    "sad": [
        "🌧️ Storms pass, brighter days are ahead. 💛",
        "🍀 Good luck is just around the corner!"
    ],
    "neutral": [
        "🌤️ A surprise is coming—stay alert!",
        "🔔 Something unexpected will brighten your day."
    ],
    "stressed": [
        "🧘 Take a breath, Asmita. Peace is near.",
        "🌸 Focus on now—tomorrow is yours."
    ]
}

if mood.lower() in fortunes:
    print("Your fortune:", random.choice(fortunes[mood.lower()]))
else:
    print("Hmm... I can't sense your mood. Try again later.")

