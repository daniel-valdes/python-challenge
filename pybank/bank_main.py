import os
import csv

# csvpath = '/Users/danvaldes/Desktop/bootcamp/repo/03-Python/Homework/Instructions/PyBank/Resources/budget_data.csv'

path = '/Users/danvaldes/desktop/bootcamp/python-challenge'
csvpath = os.path.join(path, 'pybank', 'budget_data.csv')


months = []
profloss = []

with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for column in csvreader:
        months.append(column[0])
        profloss.append(column[1])
       
# Total number of months
monthtot = len(months) 


#convert string values into integers
profloss = [int(i) for i in profloss]

totprof = sum(profloss)
avgprof = round(totprof / len(profloss), 2)

maxindex = profloss.index(max(profloss))
minindex = profloss.index(min(profloss))

print(f'Financial Analysis\n ------------------ \n Total Months: {monthtot}\n Total: ${totprof}\n Average Change: ${avgprof}\n Greatest Increase in Profits: {months[maxindex]} ${max(profloss)}\n Greatest Decrease in Profits: {months[minindex]} ${min(profloss)}')

outputpath = os.path.join(path, 'pybank', 'output.txt')

with open (outputpath, 'w') as datafile:
    datafile.write(f'Financial Analysis\n ------------------ \n Total Months: {monthtot}\n Total: ${totprof}\n Average Change: ${avgprof}\n Greatest Increase in Profits: {months[maxindex]} ${max(profloss)}\n Greatest Decrease in Profits: {months[minindex]} ${min(profloss)}')