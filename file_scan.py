def scan(file_name):
    with open(file_name , encoding = 'utf-8') as file:
        content = file.read()
        print(len(content))
        print(len(content.split()))
        print(content.count('\n') + 1)