
import json

with open("alice.txt", mode="r", encoding="utf-8") as file:
    alice = file.read()

slovnik = dict()
retezec = alice

retezec_edited = (retezec.strip().lower().replace(" ", "").replace("\n", ""))

for i in retezec_edited:
    if i in slovnik:
        slovnik[i] += 1
    else:
        slovnik[i] = 1

sorted_slovnik = dict(sorted(slovnik.items()))

with open("hw01_output.json", mode="w", encoding="utf-8") as output_file:
    json.dump(sorted_slovnik, output_file, ensure_ascii=False, indent=4)
