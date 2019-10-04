import csv
import os

# csvpath = '/Users/danvaldes/Desktop/bootcamp/python-challenge/pypoll/election_data.csv'

path = 'Users/danvaldes/Desktop/bootcamp/repo/03-Python/Homework/Instructions/PyPoll'
csvpath = os.path.join(path, 'Resources', 'election_data.csv')

# create lists
voterid = []
candidate = []

# read file and append lists
with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    for column in csvreader:
        voterid.append(column[0])
        candidate.append(column[2])

# lists for vote totals
kvotes = []
cvotes = []
lvotes = []
ovotes = []

for name in candidate:
    if name == "Khan":
        kvotes.append(name)
    elif name == "Correy":
        cvotes.append(name)
    elif name == "Li":
        lvotes.append(name)
    elif name == "O'Tooley":
        ovotes.append(name)

totalvote = len(voterid)
ktot = len(kvotes)
ctot = len(cvotes)
ltot = len(lvotes)
otot = len(ovotes)

kper = round(((ktot / totalvote) * 100))
cper = round(((ctot / totalvote) * 100))
lper = round(((ltot / totalvote) * 100))
oper = round(((otot / totalvote) * 100))

# find winner
candidate2 = ["Khan", "Correy", "Li", "O,Tooley"]
candidatetotal = [ktot, ctot, ltot, otot]

maxindex = candidatetotal.index(max(candidatetotal))

winner = candidate2[maxindex]

# print output
print(f"Election Results\n-------------------------\nTotal Votes: {totalvote}\n-------------------------\nKhan: {kper}% {ktot}\nCorrey: {cper}% {ctot}\nLi: {lper}% {ltot}\nO'Tooley: {oper}% {otot}\n-------------------------\nWinner: {winner}\n-------------------------\n")

outputpath = '/Users/danvaldes/Desktop/bootcamp/python-challenge/pypoll/electionoutput.txt'

with open (outputpath, 'w') as datafile:
    datafile.write(f"Election Results\n-------------------------\nTotal Votes: {totalvote}\n-------------------------\nKhan: {kper}% {ktot}\nCorrey: {cper}% {ctot}\nLi: {lper}% {ltot}\nO'Tooley: {oper}% {otot}\n-------------------------\nWinner: {winner}\n-------------------------\n")