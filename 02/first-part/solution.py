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
  a = sets.split(';')
  for i in a:
    b = i.split(',')
    for x in b:
      if BAG[get_color(x)] < get_number(x):
        return 0
  return id

def parse_games(data):
  return [get_valid_id(x) for x in data]

try:
  with open('../input', 'r') as f:
    data = f.readlines()
except:
  print('Input data not loaded')

valid_ids = parse_games(data)
result = 0
for id in valid_ids:
  result += id
print(result)