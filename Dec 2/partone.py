import os
file_path = os.path.dirname(os.path.realpath(__file__)) + "/input.txt"
file_input = open(file_path, "r").read().strip()
file_lines = file_input.split("\n")
answer = 0

bag_cubes = {
  "red": 12,
  "green": 13,
  "blue": 14
}

for line in file_lines:
  possible = True
  id_, line = line.split(": ")
  id_number = id_.split(" ")[1]
  game_number = id_.split(" ")[0]
  for e in line.split("; "):
    for ball in e.split(", "):
      count, color = ball.split()
      if int(count) > bag_cubes[color]:
        possible = False
  print(possible, id_number)
  if possible == True:
    answer += int(id_number)

print(answer)
