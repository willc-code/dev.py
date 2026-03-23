# 🪢 Hangman

A classic command-line Hangman game built in Python. Guess the hidden word one letter at a time — but watch out, you only have 6 lives!

---

## 🎮 How to Play

1. A random word is chosen at the start of the game.
2. The word is displayed as a series of underscores (`_`), one per letter.
3. Enter a letter guess when prompted.
4. If the letter is in the word, it replaces the corresponding underscore(s).
5. If the letter is **not** in the word, you lose a life.
6. You win by guessing all letters before running out of lives.
7. You lose if the hangman is fully drawn (0 lives remaining).

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/willc-code/hangman.git
   cd hangman
   ```

2. Ensure the following supporting files are in the same directory as `main.py`:
   - `hangman_words.py` — contains the `word_list` variable (a list of words)
   - `hangman_art.py` — contains the `stages` list (ASCII art) and `logo` string

3. Run the game:
   ```bash
   python main.py
   ```

---

## 📁 Project Structure

```
hangman/
│
├── main.py              # Main game logic
├── hangman_words.py     # Word bank
├── hangman_art.py       # ASCII art for logo and hangman stages
└── README.md

```

---

## ✨ Features

- Random word selection from a word bank
- Live display of correctly guessed letters
- Tracks previously guessed letters to avoid penalising repeated guesses
- ASCII art hangman that updates with each wrong guess
- Win/lose detection with game-ending messages

---

## 🔧 Possible Improvements

- [ ] Hide the chosen word (currently printed for testing purposes)
- [ ] Add difficulty levels (easy / medium / hard word lists)
- [ ] Track and display previously guessed wrong letters
- [ ] Add a play-again prompt without restarting the script
- [ ] Implement a scoring system

---

## 📚 Concepts Demonstrated

- `while` loops and `for` loops
- Lists and list methods (`.append()`, `in` operator)
- String manipulation and f-strings
- Importing from custom modules
- Random selection with the `random` module
- Boolean flags for game state management

---

