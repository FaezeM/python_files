from csv import reader
from csv import writer

def csv_filter():
    with open("organizations-1000.csv" , newline = '' , encoding = "utf-8") as file:
        content = reader(file)
        header = next(content)
        with open("organizations-filtered-1000.csv" , "w" , newline = '' , encoding = "utf-8") as w_file:
            w_content = writer(w_file)
            w_content.writerow(header)
            for row in content:
                try:
                    if int(row[6]) < 2000:
                        w_content.writerow(row)
                except TypeError:
                    continue

def country_filter(country , founded):
    with open("organizations-1000.csv" , newline = '' , encoding = "utf-8") as file:
        content = reader(file)
        header = next(content)
        with open("organizations-filtered-1000.csv" , "w" , newline = '' , encoding = "utf-8") as w_file:
            w_content = writer(w_file)
            w_content.writerow(header)
            for row in content:
                if row[4] == country and row[6] < founded:
                    w_content.writerow(row)

def filter_data(file):
    with open(file) as filter:
        content = reader(filter)
        count = 0
        li = []
        for row in content:
            count += 1
            li += row
        print(count)
        return li


csv_filter()
print(filter_data("organizations-filtered-1000.csv"))

input("Press any key to exit...")