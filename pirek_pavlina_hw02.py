import json


def count_decade(startyear):
    if startyear.isdigit():
        return (int(startyear) // 10) * 10
    else:
        return None


with open("netflix_titles.tsv", mode='r', encoding="UTF-8") as file:
    lines = file.readlines()
    headers = lines[0].strip().split("\t")


    output = []

    for line in lines[1:]:
        values = line.strip().split("\t")

        netflix = dict()

        netflix["title"] = values[headers.index("PRIMARYTITLE")]

        director = values[headers.index("DIRECTOR")]
        netflix["directors"] = director.split(", ") if director != "" else []

        cast = values[headers.index("CAST")]
        netflix["cast"] = cast.split(", ") if cast != "" else []

        genres = values[headers.index("GENRES")]
        netflix["genres"] = genres.split(",")

        startyear = values[headers.index("STARTYEAR")]
        netflix["decade"] = count_decade(startyear)   

        output.append(netflix)

with open("hw02_output.json", mode="w", encoding="UTF-8") as output_file:
    json.dump(output, output_file, ensure_ascii=False, indent=4)


