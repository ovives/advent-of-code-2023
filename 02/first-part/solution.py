import re

BAG = {
  'red': 12,
  'green': 13,
  'blue': 14
}

def get_number(str):
  return int(re.search(r'\d+', str).group())

def get_color(str):
  return re.search(r'red|green|blue', str).group()

def get_valid_id(game):
  [game_id, sets] = game.split(':')
  id = get_number(game_id)
  splitted_sets = sets.split(';')
  for set in splitted_sets:
    cubes = set.split(',')
    for cube in cubes:
      if BAG[get_color(cube)] < get_number(cube):
        return 0
  return id

def get_valid_ids(data):
  return [get_valid_id(x) for x in data]

try:
  with open('../input', 'r') as f:
    data = f.readlines()
except:
  print('Input data not loaded')

valid_ids = get_valid_ids(data)
result = 0
for id in valid_ids:
  result += id
print(result)