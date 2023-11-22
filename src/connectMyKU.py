import pymyku
import getpass

client = pymyku.Client(
    username=input("input Nontri username : "),
    password=getpass.getpass("input Nontri password : "),
)
