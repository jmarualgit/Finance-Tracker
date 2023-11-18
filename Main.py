import csv

with open('test.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['Date Posted', 'Name', 'Amount($)', 'Category', 'Card Used'])
        
        filewriter.writerow(['2023-11-08', 'test', 8, 'Food', 'Debit'])