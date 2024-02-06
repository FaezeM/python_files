def is_even(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

try:

    with open("numbers.txt" , "r") as file:

        content = file.readlines()
        
        for line in content:

            try:

                num = int(line.strip())
                stat = is_even(num)
                print(f"{num} is {stat}.")

            except ValueError:
                "This is not an integer!"

except FileNotFoundError:

    print("File not found!")

input("Press any key to exit...")