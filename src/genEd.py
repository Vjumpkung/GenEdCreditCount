import json
import re

with open("GenEdList.json", encoding="utf-8") as fp:
    GenEdList = json.load(fp)[0]["result"]["data"]["json"]


def SubjectTypeMap(thName: str):
    if thName == "กลุ่มสาระอยู่ดีมีสุข":
        return "Wellness"
    elif thName == "กลุ่มสาระศาสตร์แห่งผู้ประกอบการ":
        return "Entrepreneurship"
    elif thName == "กลุ่มสาระภาษากับการสื่อสาร":
        return "Language and Communication"
    elif thName == "กลุ่มสาระพลเมืองไทยและพลเมืองโลก":
        return "Thai Citizen and Global Citizen"
    elif thName == "กลุ่มสาระสุนทรียศาสตร์":
        return "Aesthetics"
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
