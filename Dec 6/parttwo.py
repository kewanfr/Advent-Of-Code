import os
file_path = os.path.dirname(os.path.realpath(__file__)) + "/input.txt"
file_input = open(file_path, "r").read().strip()
file_lines = file_input.split("\n")
answer = 0
time = int(file_lines[0].split(": ")[1].replace(" ", ""))
distance = int(file_lines[1].split(": ")[1].replace(" ", ""))

# print(time, distance)
options = []
for t in range(time):
  if (time-t)*t > distance:
    options.append([t, (time-t)*t])

answer = len(options)

print("They are", answer, "ways to win the big race.")