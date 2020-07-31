#!/usr/bin/env python3
import credentials
from sys import argv


def writeFile(variableName):
    with open("./credentials.py", "+w") as fileHandle:
        for d in variableName:
            fileHandle.write("%s" % d)


for i in range(1, len(argv)):
    if argv[i] != 'EndRetweet':
        credentials.channels.append(argv[i][26:-1])
    else:
        break
i += 1

for i in range(i, len(argv)):
    if argv[i] != 'EndFollow':
        credentials.followSource.append(argv[i][26:-1])
    else:
        break
i += 1

for i in range(i, len(argv)):
    if argv[i] != 'EndError':
        credentials.captions.append(argv[i])
    else:
        break
i += 1

# Write to file
newText = f"""account = {credentials.account}
channels = {credentials.channels}
followSource = {credentials.followSource}
captions = {credentials.captions}"""
writeFile(newText)
