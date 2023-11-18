import csv

def print_csv(fileName):
    with open(fileName, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)