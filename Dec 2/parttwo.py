import os
file_path = os.path.dirname(os.path.realpath(__file__)) + "/input.txt"
file_input = open(file_path, "r").read().strip()
file_lines = file_input.split("\n")
answer = 0


for line in file_lines:
  possible = True
  id_, line = line.split(": ")
  id_number = id_.split(" ")[1]
  game_number = id_.split(" ")[0]
  bag_cubes = {
    "red": 0,
    "green": 0,
    "blue": 0
  }

  for e in line.split("; "):
    for ball in e.split(", "):
      count, color = ball.split()
      if int(count) > bag_cubes[color]:
        bag_cubes[color] = int(count)
  
  power = None
  for key in bag_cubes:
    if power == None:
      power = bag_cubes[key]
    else:
      power = power * bag_cubes[key]

  answer += power

print(answer)
