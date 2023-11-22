from src.connectMyKU import client
from tabulate import tabulate
from src.getTranscript import get_transcript
from src.countCredits import count_credits, maximumCredits


def main():
    stdid = client.login().json()["user"]["idCode"]
    token = client.access_token

    headers = ["Type", "Credits", "MaximumCredits"]
    table = []

    credits_count = count_credits(get_transcript(stdid, token))

    for i in credits_count:
        table.append([i, credits_count[i], maximumCredits[i]])
    print(tabulate(table, headers=headers, tablefmt="psql"))


if "__main__" == __name__:
    main()
