import re


def clean_breaks(data):
  return [x.replace('\n', '') for x in data]

def is_symbol(char):
  return char != '.' and not char.isdigit()

def is_part_number(x, number_length, y_start, n_rows, n_cols, data):
  y_end = y_start + number_length - 1
  is_left_border = y_start == 0
  is_right_border = y_end == n_cols - 1
  is_top_border = x == 0
  is_bottom_border = x == n_rows - 1

  if not is_top_border:
    if not is_left_border and is_symbol(data[x - 1][y_start - 1]):
      return True 
    if not is_right_border and is_symbol(data[x - 1][y_end + 1]):
      return True
    for i in range(number_length):
      if is_symbol(data[x - 1][y_start + i]):
        return True
  if not is_bottom_border:
    if not is_left_border and is_symbol(data[x + 1][y_start - 1]):
      return True
    if not is_right_border and is_symbol(data[x + 1][y_end + 1]):
      return True
    for i in range(number_length):
      if is_symbol(data[x + 1][y_start + i]):
        return True
  if not is_left_border and is_symbol(data[x][y_start - 1]):
    return True
  if not is_right_border and is_symbol(data[x][y_end + 1]):
    return True
  return False

try:
  with open('../input', 'r') as f:
    data = clean_breaks(f.readlines())
except:
  print('Input data not loaded')

n_rows, n_cols = len(data), len(data[0])
result = 0
for x, row in enumerate(data):
  for match in re.finditer(r'\d+', row):
    number = match.group()
    y_start = match.start()
    number_length = len(number)
    if is_part_number(x, number_length, y_start, n_rows, n_cols, data):
      result += int(number)
print(result)