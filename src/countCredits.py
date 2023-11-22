from src.genEd import findCreditsAndType

maximumCredits = {
    "Wellness": 6,
    "Entrepreneurship": 3,
    "Thai Citizen and Global Citizen": 5,
    "Language and Communication": 13,
    "Aesthetics": 3,
    "Others": 6,
}


def count_credits(transcript):
    genEdCreditsCount = {
        "Wellness": 0,
        "Entrepreneurship": 0,
        "Thai Citizen and Global Citizen": 0,
        "Language and Communication": 0,
        "Aesthetics": 0,
        "Others": 0,
    }
    for i in transcript["results"]:
        for j in i["grade"]:
            if j["grade"] == "P":
                continue
            type_and_credits = findCreditsAndType(j["subject_code"])
            if type_and_credits == None:
                continue
            if (
                genEdCreditsCount[type_and_credits["type"]]
                < maximumCredits[type_and_credits["type"]]
            ):
                genEdCreditsCount[type_and_credits["type"]] += type_and_credits[
                    "credits"
                ]
            else:
                genEdCreditsCount["Others"] += type_and_credits["credits"]
    return genEdCreditsCount
