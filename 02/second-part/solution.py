import re


def get_number(str):
  return int(re.search(r'\d+', str).group())

def get_color(str):
  return re.search(r'red|green|blue', str).group()

def get_set_power(set):
  return set['red'] * set['green'] * set['blue']

def get_minimum_set(game):
  minimum_set = {
    'red': 0,
    'green': 0,
    'blue': 0
  }
  for set in game.split(':')[1].split(';'):
    cubes = set.split(',')
    for cube in cubes:
      color, number = get_color(cube), get_number(cube)
      if minimum_set[color] < number:
        minimum_set[color] = number
  return minimum_set

def get_minimum_sets(data):
  return [get_minimum_set(x) for x in data]

try:
  with open('../input', 'r') as f:
    data = f.readlines()
except:
  print('Input data not loaded')

minimum_sets = get_minimum_sets(data)
result = 0
for minimum_set in minimum_sets:
  result += get_set_power(minimum_set)
print(result)