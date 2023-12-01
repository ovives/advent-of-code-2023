import re

NUMBERS = [
  'zero', 'one', 'two', 
  'three', 'four', 'five', 
  'six', 'seven', 'eight', 
  'nine'
]

def convert_to_int(numberish):
  try:
      return int(numberish)
  except ValueError:
      return NUMBERS.index(numberish)

def get_calibration_value(str):
  numbers = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', str)
  first, last = convert_to_int(numbers[0]), convert_to_int(numbers[-1])
  return int(f'{first}{last}')

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
