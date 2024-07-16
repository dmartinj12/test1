# imported modules
import os
import csv


# path
Total_Months = 0
Sum = 0
Max = 0
Min = 0 
PNLChange = 0
PNLList = []

i = 1



csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")
    for row in csvreader:
        Total_Months = Total_Months + 1
        Sum = Sum + int(row[1])
        i = i + 1
        PNLChange = int(row[1]) - int(cell(2, i + 1))
        PNLList.append = int(row[1])
        if i > 86:
            i = 85
        if PNLChange < Max:
            Max = PNLChange
            MaxDate == row[0]
        if PNLChange > Min:
            Min = PNLChange
            MinDate == row[0]

PNLSum = sum([PNLList]) 
average = (PNLSum)/Total_Months

# determine the index on the min and the max of the PNLChange

# Based on that index determine the correspoinding date

print("Total Months:" , Total_Months)
print("Total:" , Sum)
print("Average Change" , average)
print("Greatest Increase In Profits:", MaxDate, "("Max")")
print("Greatest Decrease In Profits:", MinDate, "("Min")")

output_path = os.path.join("analysis", "analysis.txt")
with open(output_path,'w') as f:
    print(f'Total Months:" , {Total_Months}')
    f.writelines("\n")
    print(f'Total: , {Sum}')
    f.writelines("\n")
    print(f'Average Change , {average}')
    f.writelines("\n")
    print(f'Greatest Increase In Profits:, {MaxDate}, '('{Max}')'')
    f.writelines("\n")
    print(f'Greatest Decrease In Profits:, {MinDate}, '('{Min}')'')




    