import csv
import Edit as edit
import Read as read

edit.create_csv('test.csv', ['Date Posted', 'Name', 'Amount($)', 'Category', 'Card Used'])

read.read_csv('test.csv')

"""
data = {
    'Date Posted' : ['2023-11-17', '2023-11-18'],
    'Name' : ['test1', 'test2'],
    'Amount($)' : [10, 12],
    'Category' : ['Food', 'Bills'],
    'Card Used' : ['Debit', 'Credit']
}
"""

#edit.add_row('data.csv', data)
#read.read_csv('data.csv')

read.print_csv('data.csv')
edit.add_row('data.csv', 0, 'Name', 'Changed Name')
print("edited!\n")
read.print_csv('data.csv')