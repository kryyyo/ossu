hrs = float(input('Enter number of hrs: '))
rate_per_hr = float(input('Enter rate per hr: '))

if hrs > 40:
  addtl_hrs = hrs - 40
  ot_pay = addtl_hrs * (1.5 * rate_per_hr)
  basic_pay = 40 * rate_per_hr
  pay = basic_pay + ot_pay
else:
  pay = hrs * rate_per_hr

print('Pay:', pay)