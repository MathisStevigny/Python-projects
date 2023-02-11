import csv
with open('Book1.csv', 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    theList = list(csv_reader)
    print(theList)
print(theList[0][0])
print(max(theList[0]))