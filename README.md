# 🎮 Hangman Game 
A simple console-based Hangman game built in python. The game automaticlly picks a random word from a list of five predefined words. The player guesses letters with a limit of six incorrect attempts. The program uses basic Python concepts like the random module, loops, conditionals, strings, and lists. All input and output happens in the terminal without any graphics.

## 🎯 Goal
Build a simple text-based Hangman game in Python where the player guesses a word one letter at a time, with a maximum of six incorrect attempts.

## ⭐ Features
- **Random Word Selection :** The game selects a word from a predefined list for each round.
- **ASCII Hangman Display :** The hangman figure updates after each incorrect guess.
- **Input Validation :** Prevents repeated and invalid guesses to keep gameplay clean.
- **Live Word Progress Display :** Shows guessed letters and remaining blanks in real time.
- **Win/Lose End Screens :** Displays a win message or the final hangman with the correct word.

## 🧠 Key Concepts Used
- random module
- While loops
- If-else conditions
- Strings and lists
- Sets for tracking guesses

## 🛠 Tech Stack
**Language :** Python

**Environment :** Terminal Command Line

## 🕹 Gameplay Rules
-  The game picks one random word from list of the five predefined wrods
- You can guess one letter at a time
- You can only make six incorrect guesses
- With each incorrect guess, the ASCII hangman gains another body part until the figure is fully completed
- The game ends when you guess all letters correctly (win), or you reach six wrong guesses (loss)

## 📂 Project Structure
```bash
CodeAlpha_HangmanGame/
│
├── hangman.py       # Main game file
└── README.md        # Documentation
```

## 📥 Installation
Clone the repository using Git :
```bash
  git clone https://github.com/shreyakantha/CodeAlpha_HangmanGame
cd CodeAlpha_HangmanGame
```

## 🖥 Run Locally
Navigate to the location of your file :
```bash
  cd CodeAlpha_HangmanGame
```
Run the script :
```bash
 python hangman.py
```

## 🎥 Demo
*A video demonstration of the Hangman Game showing the complete gameplay flow, including random word selection, letter-by-letter guessing, ASCII hangman progression, and win or loss outcomes.*

**Click Here** ▶ [Hangman-Game-Demo-Video](https://github.com/shreyakantha/CodeAlpha_HangmanGame/releases/tag/v1.0)

## 📝 Usage/Examples

When you run the program, you’ll see something similar to :

```bash
  Welcome to Hangman!
Guess the word one letter at a time. You have 6 wrong guesses.

Current word: _ _ _ _ _ _ _ _ _
Wrong guesses: 0/6
Hangman:
    +---+
    |   |
        |
        |
        |
        |
=========
Guess a letter:
```
*The hangman updates after each incorrect guess until the game ends.*  

Near the end of the game, with only one incorrect guess remaining, the hangman figure is almost complete and only a few letters are left to guess :

```text
Wrong guesses: 5/6
Hangman:
  +---+
  |   |
  o   |
 /|\  |
 /    |
      |
=========
Current word: S P A _ H E _ T _
Guess a letter:
```
*The game continues updating the hangman until a win or loss is reached.*

## 🚀 Deployment
This is a local console-based Python script and does not require deployment. It can be executed on any system with Python installed.

## ⚙ Optimisations
- Uses a set to efficiently track guessed letters and avoid repeated guesses
- Limits memory usage by using a small predefined word list
- Updates only necessary game state variables during each guess
- Keeps game logic lightweight and easy to extend

## 🎓 Lessons Learned
Working on this project helps reinforce :
- Using the random module
- Tracking state using sets and lists
- Updating the display dynamically
- Handling user input safely
- Building a complete loop-based game flow

## 🔮 Future improvements
- Add difficulty levels
- Add replay option
- Add more word categories
- Add colors for better readability
- Add a high-score or attempt tracker

## 📄 Documentation
This project is documented using this README.md, which explains the game overview, rules, features, installation steps, and sample gameplay output. The source code (hangman.py) is organized in a readable way with clear variable names and logical flow, making it easy for beginners to understand and modify.

## 👤 Author
- [@shreyakantha](https://github.com/shreyakantha)

## 🙌 Acknowledgements
 - Inspiration from classic Hangman console games
 - ASCII art adapted from common hangman templates
 - General README guidelines from open-source communities

## 📜 License
This project is open for educational and personal use under the MIT License.  
Feel free to modify, improve, and expand it as needed.

## 💬 Feedback
If you have any feedback, please reach out to us at 📧 shreyakantha348@gmail.com

## ❓FAQ
#### Q1. Why does the game allow only 6 wrong guesses?
Six attempts match the classic Hangman structure and the ASCII art stages.
#### Q2. Can I add more words to the game?
Yes. Just open hangman.py and add more items to the words list.
#### Q3. Does the game support lowercase letters?
All input is converted to uppercase automatically.

## 🧩 Appendix
The project ***Hangman Game*** is part of task under the **CodeAlpha Internship**.

## 📌 Related Projects
*The following projects were completed as part of the same **CodeAlpha internship** program and focus on strengthening core Python programming concepts.*
🔗 [Stock Portfolio Tracker – Data processing using Python](https://github.com/shreyakantha/CodeAlpha_StockPortfolioTracker)
🔗 [Email Extraction Automation – File handling and regular expressions in Python](https://github.com/shreyakantha/CodeAlpha_EmailExtractor)
🔗 [Basic Chatbot – Rule-based conversation using conditional logic](https://github.com/shreyakantha/CodeAlpha_BasicChatbot)
