import csv

my_dict = {"test": 1, "testing": 2}

with open('mycsvfile.csv', 'wb') as f:  # 'w' mode in python 3.x
    w = csv.DictWriter(f, my_dict.keys())
    w.writeheader()
    w.writerow(my_dict)