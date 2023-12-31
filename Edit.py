import csv
import pandas as pd
import glob

def create_csv(fileName, fileLabels):
    with open(fileName, 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(fileLabels)

def add_row(fileName, data):
    df = pd.DataFrame(data)
    
    df.to_csv(fileName, mode='a', index=False, header=False)

# row number will be +1 what is listed on the left bc of the label on line 1
def edit_row(fileName, rowNumber, columnName, newValue):
    df = pd.read_csv(fileName)
    
    # loc locates/accesses the specific part of the dataframe
    df.loc[rowNumber, columnName] = newValue
    
    df.to_csv(fileName, index=False, header=True)

def merge_csv(path, string):
    
    # sample string would be stmt*
        # gets all files that start with stmt
    statements = glob.glob(f'{path}/{string}')
    
    combinedDataFrame = []
    
    for statement in statements:
        
        new_dataframe = pd.read_csv(statement)
        combinedDataFrame.append(new_dataframe)
    
    df = pd.concat(combinedDataFrame)
    
    df.to_csv('data.csv', index=False)