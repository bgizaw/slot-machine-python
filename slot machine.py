import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# frequency/rarity of each symbol
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

# multiplier value of each symbol
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


# check how much user won and which lines they won on
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    # check lines in slot machine based on how many lines user said they would bet on
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            #
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break

        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    # list to hold all symbols from previous dictionary
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        # loop for how many occurrences a symbol has (ex. A appends to the list twice)
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        # create a copy of all_symbols to paste into the new symbols list so they don't affect each other
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        # append the column from this iteration to the full columns list
        columns.append(column)

    # pre-transposed representation of columns in 2d list
    return columns


# visual of slot machine
def print_slot_machine(columns):
    # columns[0] is the first row of the 2d list of columns and row iterates through it
    for row in range(len(columns[0])):
        # use enumerate to pass both the row and column number of the 2d list into the variables.
        # enumerate returns the row index and the row itself as a list. the row represents the column since it is
        # not transposed yet
        for i, column in enumerate(columns):

            if i != len(columns) - 1:
                # the loop runs through each "row" of the 2d list and prints the i'th index of each "row"
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()


# get the amount of money to be deposited from user
def deposit():
    while True:
        print("What would you like to deposit?")
        amount = input("$")
        if amount.isdigit():
            amount = int(amount)
            # break out of loop if input given is greater than 0
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number.")
    # balance
    return amount


# ask user how many out of the total number of lines they want to bet on
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        # number of lines must be a positive number between the min and max already set
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number.")
    # number of rows used
    return lines


# ask user how much money they want to bet on each slot line
def get_bet():
    # infinite loop to keep asking for input based on if it is valid or not
    while True:
        print("What would you like to bet on each line?")
        amount = input("$")
        # if input is a positive number, then convert the string input into an integer. break out of loop if
        # bet amount is not within parameters
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    # amount of bet per line
    return amount


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance} ")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
