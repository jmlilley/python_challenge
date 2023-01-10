import os
import csv

bank_csv = os.path.join('Resources', 'budget_data.csv')

with open (bank_csv, 'r') as csvfile:
    csvreader = csv.reader(bank_csv, delimiter=',')
    header = next(csvreader)

    print(header)

    month_count = 0
    net_total = 0

    for row in csvreader:
        month_count += 1
        print(row[0])

print(f'Total Months: {month_count}')
#print(f'Total: {net_total}')