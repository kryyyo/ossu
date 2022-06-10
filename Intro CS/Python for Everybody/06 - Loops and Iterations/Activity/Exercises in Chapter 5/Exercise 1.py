# Initialize variables
sum = 0
count = 0 

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

  sum = sum + userInput 
  count = count + 1


try:
  print(sum, count, sum/count)
except:
  print('Error, cannot be divided by zero')