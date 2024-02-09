from csv import reader
from csv import writer

with open("organizations-1000.csv" , newline = '' , encoding = "utf-8") as file:
    content = reader(file)
    header = next(content)
    with open("organizations-filtered-1000.csv" , "w" , newline = '' , encoding = "utf-8") as w_file:
        w_content = writer(w_file)
        w_content.writerow(header)
        for row in content:
            try:
                if int(row[6]) < 2000:
                    print(row[6])
                    w_content.writerow(row)
            except TypeError:
                continue



input("Press any key to exit...")