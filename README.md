# Folktale

Folktale is a lightweight, terminal-based Python escape-room game that combines classic riddles with Hangman-style letter guessing. Players move from room to room, solving randomly selected riddles before their six lives run out. Correct guesses reveal letters in the answer, while incorrect guesses bring the walls closer and make escape more difficult.

The game is designed as a simple and entertaining command-line experience for practicing Python fundamentals such as loops, conditionals, lists, user input, random selection, and string processing. Each successful solution opens the door to another room, while failed attempts are tracked so players can see how many rooms they escaped and how many times they were trapped.

## Features

- Randomly selects a riddle for each escape-room challenge.
- Uses Hangman-style letter guessing to reveal answers.
- Gives the player six lives per room.
- Prevents invalid and repeated guesses.
- Tracks rooms escaped and rooms where the player was trapped.
- Allows the player to type `exit` at any time to quit.
- Runs entirely in the terminal with no external dependencies.

## Requirements

- Python 3.7 or later

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Arjun-Pai/Folktale.git
cd Folktale
```

### 2. Run the game

```bash
python Hangman.py
```

On some systems, you may need to use:

```bash
python3 Hangman.py
```

## How to Play

1. Start the game from your terminal.
2. Read the riddle shown in the room.
3. Guess one letter at a time.
4. Solve the answer before losing all six lives.
5. Continue through as many rooms as you can.
6. Type `exit` whenever you want to stop playing.

## Project Structure

```text
Folktale/
├── Hangman.py   # Main game logic
└── README.md    # Project documentation
```

## Example Gameplay

```text
Welcome to the Escape Room!
Solve each riddle by guessing the letters of the answer.
You have 6 lives in every room. Type 'exit' at any time to quit.

A door slams shut behind you. A new room appears!
The lock asks you:
I have keys but open no locks. What am I?

_ _ _ _ _ _ _
Lives left: 6
Letters guessed:
Guess a letter:
```

## Learning Goals

Folktale is a beginner-friendly project that demonstrates how to build an interactive Python program. It provides practice with random data selection, nested loops, input validation, state tracking, and basic game design.

## License

No license has been specified for this repository yet.
