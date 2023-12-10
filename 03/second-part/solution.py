import re


def clean_breaks(data):
  return [x.replace('\n', '') for x in data]

def get_complete_number(x, y, n_cols, data):
  number = data[x][y]
  for i in range(y + 1):
    if i == 0:
      continue
    if data[x][y - i].isdigit():
      number = f'{data[x][y - i]}{number}'
    else:
      break
  for i in range(n_cols - y):
    if i == 0:
      continue
    if data[x][y + i].isdigit():
      number = f'{number}{data[x][y + i]}'
    else:
      break
  return int(number)

def get_gear_ratio(x, y, n_rows, n_cols, data):
  is_left_border = y == 0
  is_right_border = y == n_cols - 1
  is_top_border = x == 0
  is_bottom_border = x == n_rows - 1

  gears = []
  if not is_top_border:
    if not is_left_border and data[x - 1][y - 1].isdigit():
      number = get_complete_number(x-1, y-1, n_cols, data)
      if not number in gears:
        gears.append(number)
    if not is_right_border and data[x - 1][y + 1].isdigit():
      number = get_complete_number(x-1, y+1, n_cols, data)
      if not number in gears:
        gears.append(number)
    if data[x - 1][y].isdigit():
      number = get_complete_number(x-1, y, n_cols, data)
      if not number in gears:
        gears.append(number)
  if not is_bottom_border:
    if not is_left_border and data[x + 1][y - 1].isdigit():
      number = get_complete_number(x+1, y-1, n_cols, data)
      if not number in gears:
        gears.append(number)
    if not is_right_border and data[x + 1][y + 1].isdigit():
      number = get_complete_number(x+1, y+1, n_cols, data)
      if not number in gears:
        gears.append(number)
    if data[x + 1][y].isdigit():
      number = get_complete_number(x+1, y, n_cols, data)
      if not number in gears:
        gears.append(number)
  if not is_left_border and data[x][y - 1].isdigit():
    number = get_complete_number(x, y-1, n_cols, data)
    if not number in gears:
        gears.append(number)
  if not is_right_border and data[x][y + 1].isdigit():
    number = get_complete_number(x, y+1, n_cols, data)
    if not number in gears:
        gears.append(number)
  
  if len(gears) == 2:
    return gears[0] * gears[1]
  return 0



try:
  with open('../input', 'r') as f:
    data = clean_breaks(f.readlines())
except:
  print('Input data not loaded')

n_rows, n_cols = len(data), len(data[0])
result = 0
for x, row in enumerate(data):
  for match in re.finditer(r'\*', row):
    y = match.start()
    result += get_gear_ratio(x, y, n_rows, n_cols, data)
print(result)
