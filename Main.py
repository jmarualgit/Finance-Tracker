import csv
import Edit as edit

edit.create_csv('test.csv', ['Date Posted', 'Name', 'Amount($)', 'Category', 'Card Used'])

with open('test.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)