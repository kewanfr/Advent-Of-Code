import os

with open('./1 Dec/input.txt') as f:
  input_text = f.readlines()

def getCalibrationValue(input):
  first = None
  second = None
  for i in input:
    if i.isdigit():
      if first == None:
        first = i
      second = i
  return int(first+ second)


sum = 0
for i in input_text: 
  sum += getCalibrationValue(i)
print(sum)