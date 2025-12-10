
# 🎮  Hangman Game 
A simple console-based Hangman game built in python. The game automaticlly picks a random word from a list of five predefined words. The player guesses letters with a limit of six incorrect attempts. The program uses basic Python concepts like the random module, loops, conditionals, strings, and lists. All input and output happens in the terminal without any graphics.


## ⭐ Features

-  **Random Word Selection :** The game chooses a random word from a predefined list every time you play, ensuring each round feels different.

- **ASCII Hangman Display :** A multi-stage ASCII figure updates after each wrong guess, giving a visual representation of progress.

- **Input Validation :** The game prevents repeated guesses, non-alphabet characters, multiple characters, reduces errors and keeps gameplay clean.

- **Live Word Progress Display :** The game shows which letters you’ve correctly guessed and which ones are still hidden.

- **Win/Lose End Screens :** Displays a clear win message or the final hangman stage with the correct word when the game ends.



## 🕹 Gameplay Rules

-  The game picks one random word from list of the five predefined wrods.

- You can guess one letter at a time.

- You can only make six incorrect guesses.

- With each incorrect guess, the ASCII hangman gains another body part until the figure is fully completed.

- The game ends when : You guess all letters correctly (win), or you reach six wrong guesses (loss).

## 📂 Project Structure

```bash
  project-folder/
│
├── hangman.py       # Main game file
└── README.md        # Documentation
```
## 📥 Installation

Install the project locally :

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

## 📝 Usage/Examples

When you run the program, you’ll see something similar to :

```bash
  Welcome to Hangman!
Guess the word one letter at a time. You have 6 wrong guesses.

Current word: _ _ _ _ _
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
The hangman updates after each incorrect guess until the game ends.

## 🎓Lessons Learned

Working on this project helps reinforce :

- Using the random module

- Tracking state using sets and lists

- Updating the display dynamically

- Handling user input safely

- Building a complete loop-based game flow


## 🔮Future improvements

- Add difficulty levels

- Add replay option

- Add more word categories

- Add colors for better readability

- Add a high-score or attempt tracker

## 👤 Author

- [@shreyakantha](https://github.com/shreyakantha)


## 🙌 Acknowledgements

 - Inspiration from classic Hangman console games
 
 - ASCII art adapted from common hangman templates

 - General README guidelines from open-source communities




## 📜 License

This project is open for educational and personal use under the MIT License.  
Feel free to modify, improve, and expand it as needed!


## 💬 Feedback

If you have any feedback, please reach out to us at shreyakantha348@gmail.com
## ❓FAQ

#### Q1. Why does the game allow only 6 wrong guesses?
Six attempts match the classic Hangman structure and the ASCII art stages.

#### Q2. Can I add more words to the game?
Yes. Just open hangman.py and add more items to the words list.

#### Q3. Does the game support lowercase letters?
All input is converted to uppercase automatically.


