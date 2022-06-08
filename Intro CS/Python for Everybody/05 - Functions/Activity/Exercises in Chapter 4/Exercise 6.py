# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).
try: 
  hrs = float(input('Enter number of hrs: '))
  rate_per_hr = float(input('Enter rate per hr: '))
except: 
  print('Error, please enter numeric input')
  quit()

def computepay(hours, rate): 
  if hours > 40:
    addtl_hrs = hours - 40
    ot_pay = addtl_hrs * (1.5 * rate)
    basic_pay = 40 * rate
    pay = basic_pay + ot_pay
  else:
    pay = hours * rate
  return pay

print('Pay', computepay(hrs, rate_per_hr))