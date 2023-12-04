import os
file_path = os.path.dirname(os.path.realpath(__file__)) + "/input.txt"
file_input = open(file_path, "r").read().strip()
file_lines = file_input.split("\n")
answer = 0


def get_nb_winning_cards(values):
  parts = values.split(" | ")
  winning_numbers = parts[0].split()
  numbers = parts[1].split()
  winnings_nb = 0
  for n in numbers:
    if n in winning_numbers:
      winnings_nb += 1
  return winnings_nb

cards_vals = {}


for line in file_lines:
  values = line.split(": ")[1]
  card_number = int(line.split(":")[0].split()[1])
  
  card_winning_nb = get_nb_winning_cards(values)
  cards_vals[card_number] = {"nb_winning_cards": card_winning_nb, "nb_cards": 1}

for key in cards_vals:
  val = cards_vals[key]
  for key2 in range(val['nb_winning_cards']):
    cards_vals[key + key2+1]['nb_cards'] += cards_vals[key]['nb_cards']

for key in cards_vals:
  answer += cards_vals[key]['nb_cards']

print(answer)