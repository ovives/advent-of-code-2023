def get_first_number(str):
  for char in str:
    if char.isdigit():
      return char

def get_calibration_value(str):
  first_digit = get_first_number(str)
  last_digit = get_first_number(str[::-1])
  return int(f'{first_digit}{last_digit}')

def get_calibration_document(data):
  return [get_calibration_value(x) for x in data]

try:
  with open('../input', 'r') as f:
    data = f.readlines()
except:
  print('Input data not loaded')

calibration_document = get_calibration_document(data)
sum_caliration_numbers = 0
for i in calibration_document:
  sum_caliration_numbers += i
print(sum_caliration_numbers)
