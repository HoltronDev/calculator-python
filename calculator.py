print("Welcome to the Calculator (Python)")
print("Available operations are:")
print("X + Y")
print("X - Y")
print("X * Y")
print("X / Y")
print("Type 'exit' to leave.")

while True:
  userInput = input()

  if userInput == "exit":
    break

  parts = userInput.split()

  if len(parts) != 3:
    print("Invalid formatting. Input was: {}".format(userInput))

  try:
    first = int(parts[0])
  except:
    print("Invalid format for first number. Input was: {}".format(parts[0]))
    continue
  
  try:
    second = int(parts[2])
  except:
    print("Invalid format for second number. Input was: {}".format(parts[2]))
    continue

  if parts[1] == "+":
    print("Answer: {}".format(first + second))
  elif parts[1] == "-":
    print("Answer: {}".format(first - second))
  elif parts[1] == "*":
    print("Answer: {}".format(first * second))
  elif parts[1] == "/":
    print("Answer: {}".format(first / second))
  else:
    print("Invalid operation input. Input was: {}".format(parts[1]))

print("Good bye!")