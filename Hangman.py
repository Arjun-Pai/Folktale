import random

riddles = [
    ("I have keys but open no locks. What am I?", "keyboard"),
    ("I have hands but cannot clap. What am I?", "clock"),
    ("I get wetter the more I dry. What am I?", "towel"),
    ("I have a neck but no head. What am I?", "bottle"),
    ("I am full of holes but still hold water. What am I?", "sponge"),
    ("I have cities but no houses and water but no fish. What am I?", "map"),
    ("The more you take of me, the more you leave behind. What am I?", "footsteps"),
    ("I can fly without wings and cry without eyes. What am I?", "cloud"),
    ("I have a face and two hands but no arms or legs. What am I?", "watch"),
    ("I am tall when I am young and short when I am old. What am I?", "candle"),
    ("I have teeth but cannot bite. What am I?", "comb"),
    ("I am always in front of you but cannot be seen. What am I?", "future")
]

escaped = 0
trapped = 0
game_running = True

print("Welcome to the Escape Room!")
print("Solve each riddle by guessing the letters of the answer.")
print("You have 6 lives in every room. Type 'exit' at any time to quit.")
print("")

while game_running:
    question, answer = random.choice(riddles)
    guessed = []
    lives = 6
    room_running = True

    print("A door slams shut behind you. A new room appears!")
    print("The lock asks you:")
    print(question)
    print("")

    while room_running:
        display = ""
        for letter in answer:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        print(display)
        print("Lives left: " + str(lives))
        print("Letters guessed: " + " ".join(guessed))

        guess = input("Guess a letter: ").lower()

        if guess == "exit":
            room_running = False
            game_running = False
        elif len(guess) != 1 or not guess.isalpha():
            print("Invalid input entered")
        elif guess in guessed:
            print("You already guessed that letter")
        else:
            guessed.append(guess)

            if guess in answer:
                print("Correct! The lock clicks.")
            else:
                lives -= 1
                print("Wrong! The walls close in a little more.")

            solved = True
            for letter in answer:
                if letter not in guessed:
                    solved = False

            if solved:
                escaped += 1
                print("The answer was " + answer + "! The door swings open. You escaped!")
                room_running = False
            elif lives == 0:
                trapped += 1
                print("The walls close in. The answer was " + answer + ". You are trapped!")
                room_running = False

        print("")

    if game_running:
        print("Rooms escaped: " + str(escaped) + " | Times trapped: " + str(trapped))
        print("")

print("Thanks for playing!")
print("Final score - Rooms escaped: " + str(escaped) + " | Times trapped: " + str(trapped))
