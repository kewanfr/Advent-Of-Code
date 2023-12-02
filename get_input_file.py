# Simple script to download input files from Advent of Code
# Don't forget to put your session token in session.txt
# You can find it in your browser cookies
# This script will create a folder for each day, and put the input file in it

import os
import requests
from datetime import datetime

YEAR_IN_FOLDER_NAME = False # If True, the folder will be named "2020 Dec" instead of "Dec"
CURRENT_YEAR = datetime.now().year # Change this if you want to download input files from another year

os.environ["AOC_SESSION"] = open(os.path.dirname(os.path.realpath(__file__)) + "/session.txt", "r").read()


def download_input_txt_file(day, year):
  file_dir = os.path.dirname(os.path.realpath(__file__)) + "\\"
  if YEAR_IN_FOLDER_NAME:
    file_dir += str(year) + " "
  
  file_dir += "Dec " + str(day) + "\\"

  os.makedirs(os.path.dirname(file_dir), exist_ok=True)
  file_path = file_dir + "input.txt"

  request = requests.get("https://adventofcode.com/" + str(year) + "/day/" + str(day) + "/input", cookies={"session": os.environ["AOC_SESSION"]})
  
  if request.status_code == 200:
    file_input = request.text
    open(file_path, "w").write(file_input)
    print("Fichier d'entrée du jour récupéré avec succès !")
  else:
    print("Error: " + str(request.status_code))
    print("X Impossible de récupérer le fichier d'entrée. Il est possible que le jour ne soit pas encore sorti, ou que le token de session.txt soit invalide.")

  return

current_day = datetime.now().day

download_input_txt_file(current_day, CURRENT_YEAR)