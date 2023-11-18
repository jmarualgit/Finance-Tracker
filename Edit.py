import csv


def create_csv(fileName, fileLabels):
    with open(fileName, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(fileLabels)