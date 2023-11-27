import json
import re

with open("GenEdList.json", encoding="utf-8") as fp:
    GenEdList = json.load(fp)[0]["result"]["data"]["json"]


def SubjectTypeMap(thName: str):
    th_to_en = {
        "กลุ่มสาระอยู่ดีมีสุข": "Wellness",
        "กลุ่มสาระศาสตร์แห่งผู้ประกอบการ": "Entrepreneurship",
        "กลุ่มสาระภาษากับการสื่อสาร": "Language and Communication",
        "กลุ่มสาระพลเมืองไทยและพลเมืองโลก": "Thai Citizen and Global Citizen",
        "กลุ่มสาระสุนทรียศาสตร์": "Aesthetics",
    }
    if thName in th_to_en.keys():
        return th_to_en[thName]
    else:
        return "NOT_GENED"


def findCreditsAndType(stdid: str):
    for subject in GenEdList:
        if stdid == subject["subjectCode"]:
            return {
                "type": SubjectTypeMap(subject["subjectGroup"]),
                "credits": int(
                    re.match(r"^[0-9]*", subject["subjectCredits"]).group(0)
                ),
            }
    return None
