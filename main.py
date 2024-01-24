MAX_LINES = 5
MIN_LINES = 1

def deposite():
  while True:
    amount = input("What would you like to deposit? $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Amount must be greater than 0.")
    else:
      print("Please enter a number.")

  return amount

def get_number_of_lines():
  while True:
    lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
    if lines.isdigit():
      lines = int(lines)
      if MIN_LINES <= lines <= MAX_LINES:
        break
      else:
        print("Enter a valid number of lines.")
    else:
      print("Please enter a number.")

  return lines

def main():
  balance = deposite()
  lines = get_number_of_lines()
  print(balance, lines)

main()