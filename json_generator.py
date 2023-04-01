import os
import json

folder_path = "/Users/ari/Desktop/DVFinalProject/data/buffett_letters"

yearly_text = {}

for filename in os.listdir(folder_path):
    if filename.endswith(".txt") and filename.startswith("Chairman Letter - "):
        year = filename.replace("Chairman Letter - ", "").replace(".txt", "")
        with open(os.path.join(folder_path, filename), "r") as file:
            content = file.read()
        yearly_text[year] = content

with open("data/combined_letters.json", "w") as json_file:
    json.dump(yearly_text, json_file)

