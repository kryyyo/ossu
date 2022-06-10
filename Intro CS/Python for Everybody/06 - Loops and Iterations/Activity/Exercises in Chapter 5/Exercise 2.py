# Initialize variables
max = None
min = None

# Main Loop
while True:
  try: 
    userInput = input('Enter a number: ')

    if userInput == 'done': 
      break
    else:
      userInput = float(userInput)
  except: 
    print('Invalid input')
    continue

  # Finding the max number
  if max is None and min is None:
    max = userInput
    min = userInput
  elif userInput >= max: 
    max = userInput
  elif userInput <= min:
    min = userInput

print('Maximum is', int(max))
print('Minimum is', int(min))