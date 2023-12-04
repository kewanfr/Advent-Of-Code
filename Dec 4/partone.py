import os
file_path = os.path.dirname(os.path.realpath(__file__)) + "/input3.txt"
file_input = open(file_path, "r").read().strip()
file_lines = file_input.split("\n")
answer = 0

for line in file_lines:
  values = line.split(": ")[1]
  parts = values.split(" | ")
  winning_numbers = parts[0].split()
  numbers = parts[1].split()
  winning = 0
  for n in numbers:
    if n in winning_numbers:
      if winning > 1:
        winning = winning *2
      else:
        winning += 1 
  answer += winning

print(answer)