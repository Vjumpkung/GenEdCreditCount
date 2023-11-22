import requests


def get_transcript(stdid, token):
    transcript = requests.get(
        url=f"https://myapi.ku.th/std-profile/checkGrades?idcode={stdid}",
        headers={
            "App-Key": "txCR5732xYYWDGdd49M3R19o1OVwdRFc",
            "X-Access-Token": token,
        },
    ).json()
    return transcript
