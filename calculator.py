from art import logo
print(logo)

# Calculater Functions
def add(n1, n2):
  return n1 + n2
def multiply(n1, n2):
  return n1 * n2
def subtract(n1, n2):
  return n1 - n2
def divide(n1,n2):
  return n1 / n2

# Calculator Operations
operation_dict = {
  "+":add,
  "*":multiply,
  "-":subtract,
  "/": divide,
  }

def calculator():
  first_number = float(input("What's the first number?:\n"))
  for operation in operation_dict:
    print(operation)

  keep_going = True
  while keep_going:
    operation_symbol = input("Pick an operation:\n")
    second_number = float(input("What's the next number?\n"))
    calculation_function = operation_dict[operation_symbol]
    answer = calculation_function(first_number, second_number)

    print(f"{first_number} {operation_symbol} {second_number} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer} or type 'n' to start a new calculation:\n").lower() == 'y':
      first_number = answer
    else:
      keep_going = False
      calculator()

calculator()
