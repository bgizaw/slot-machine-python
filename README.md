# Slot Machine Game - Python

Welcome to the mesmerizing world of the Slot Machine Game in Python! Test your luck, spin the reels, and watch the symbols align to win big! This simple yet captivating game offers an opportunity to experience the excitement of a real slot machine right from your command line.

## How to Play

1. Run the Python code in your preferred environment.
2. Upon starting the game, you'll be prompted to deposit an initial amount to begin playing.
3. Choose the number of lines you want to bet on (between 1 and 3).
4. Enter the amount you want to bet on each line (ranging from $1 to $100).
5. Watch the virtual reels spin and hope for matching symbols to land on the winning lines.
6. Your winnings will be displayed, and you can continue playing as long as you have enough balance.
7. Press 'q' at any time to quit the game and see the final amount left in your balance.

## Game Rules

- The Slot Machine consists of 3 reels and 3 rows.
- Each symbol has a different rarity and multiplier value, enhancing the excitement of each spin:
  - Symbol "A": Rarity 2, Multiplier 5x
  - Symbol "B": Rarity 4, Multiplier 4x
  - Symbol "C": Rarity 6, Multiplier 3x
  - Symbol "D": Rarity 8, Multiplier 2x

- To win, you need to get the same symbol on a winning line.
- The number of lines you bet on multiplies your potential winnings, so choose wisely!

## Code Snippet

```python
# Import the required libraries
import random

# Constants (can be adjusted)
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

# Frequency/rarity of each symbol
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# Multiplier value of each symbol
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# ... (Rest of the code)

# Play the game
main()
```

Feel free to customize the constants and symbol values to create your unique Slot Machine experience.

# Contributing
We welcome contributions from the community! If you have ideas for enhancements, bug fixes, or new features, feel free to open an issue or submit a pull request on our GitHub repository.

# Acknowledgements
Special thanks to the Python community for their support and inspiration in creating this entertaining Slot Machine Game.

So, what are you waiting for? It's time to test your luck and have some fun! Spin the reels and let the adventure begin! 

**Disclaimer:** This game is for entertainment purposes only and does not involve real money gambling.
