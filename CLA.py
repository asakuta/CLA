import math
import sys

def salary():
    if len(sys.argv) > 1:
        File=sys.argv[1]
        handle=open(File, "r")
        text=handle.read()
        handle.close()
        tempList=text.split("\n")
        winner=[{"name":"none", "salary":0}]
        for x in range(1, len(tempList)-1):
            newList=tempList[x].split(",")
            if int(newList[1]) > winner[0]["salary"]:
                winner=[{"name":"none", "salary":0}]
                winner[0]["name"]=newList[0]
                winner[0]["salary"]=int(newList[1])
            else:
                if int(newList[1]) == winner[0]["salary"]:
                    winner.insert(len(winner), {"name": newList[0], "salary": int(newList[1])})
        print(winner)
    else:
        print("nope")

salary()