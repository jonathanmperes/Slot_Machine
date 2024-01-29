# Slot Machine

This is a simple Python project that implements a text-based slot machine game. Users can deposit money, place bets on multiple lines, and spin the slot machine. The game checks for winning combinations and calculates winnings based on the provided symbol values.

## Fundamentals of Python

The project is built using fundamental concepts of the Python programming language. Here are some key aspects of the code:

- **Random Module:** The `random` module is utilized for generating random values, essential for the slot machine spin.

- **Data Structures:** The project employs dictionaries to store symbol counts (`symbol_count`) and symbol values (`symbol_value`). Lists are used to represent the columns of the slot machine.

- **Functions:** The code is organized into functions, such as `check_winnings`, `get_slot_machine_spin`, `print_slot_machine`, `deposite`, `get_number_of_lines`, `get_bet`, `spin`, and `main`, to enhance modularity and readability.

- **Loops:** The code utilizes `for` and `while` loops for tasks like checking winning lines, depositing money, and validating user input.

- **User Input:** The `input` function is used to interact with the user, allowing them to deposit money, place bets, and choose to play or quit.

## How to Play

1. Deposit money by entering a positive amount.
2. Press Enter to spin the slot machine or 'q' to quit.
3. Choose the number of lines to bet on (between 1 and 3).
4. Specify the bet amount per line (between $1 and $100).
5. The slot machine will display the results, showing if you've won and the winning lines.
6. The game continues until the user decides to quit.
