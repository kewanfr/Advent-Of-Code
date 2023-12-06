import os
file_path = os.path.dirname(os.path.realpath(__file__)) + "/input.txt"
file_input = open(file_path, "r").read().strip()
file_lines = file_input.split("\n")
answer = 0

times = file_lines[0].split(": ")[1].split()
distances = file_lines[1].split(": ")[1].split()
record_ways = []
for index in range(len(times)):
  time = int(times[index])
  distance = int(distances[index])

  # print(time, distance)
  options = []
  for t in range(time):
    if (time-t)*t > distance:
      options.append([t, (time-t)*t])
  record_ways.append(len(options))

answer = 1
for record in record_ways:
  answer *= record

print("The ways to win multiplied together are", answer)