import csv

#write to a csv file 

with open('data2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(['name', 'age', 'city'])
    writer.writerow(['Pankaj', 25, 'Delhi'])
    writer.writerow(['Amit', 30, 'Mumbai'])

writing multiple rows 
writer.writerows(rows)


writing dictioary data

data = [
    {'name': 'Pankaj', 'age': 25},
    {'name': 'Amit', 'age': 30}
]

with open('output.csv', 'w', newline='') as file:
    fieldnames = ['name', 'age']
    
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(data)





    