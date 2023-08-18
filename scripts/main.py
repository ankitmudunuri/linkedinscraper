import linkedinscrape as lis
from datetime import datetime
import keyboard as kb

path = __file__.replace("scripts\\main.py", "")

def passlink(listoflinks):
    for x in listoflinks:
        lis.scrape(x[0], x[1])

def main():

    linkedin = open(f"{path}files/linkedinlinks.txt", "r").read()
    linkedin = linkedin.split("\n")
    linkedinlinks = []
    for x in linkedin:
        temp = x.split(",")
        linkedinlinks.append((temp[0], temp[1]))


    passlink(linkedinlinks)
    start = datetime.now()

    while True:
        now = datetime.now()
        diff = now - start
        if diff.seconds > 900:
            passlink(linkedinlinks)
            start = datetime.now()

        if kb.is_pressed("alt+h"):
            break
 
if __name__ == "__main__":
    main()