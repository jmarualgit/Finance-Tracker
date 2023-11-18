import csv
import Edit as edit
import Read as read

edit.create_csv('test.csv', ['Date Posted', 'Name', 'Amount($)', 'Category', 'Card Used'])

read.read_csv('test.csv')