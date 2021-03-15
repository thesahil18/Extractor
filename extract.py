import re
with open("name of file from where u want to extract emails", 'r') as f:
    data = f.read()

i = 1

extractor = re.findall(r'[0-9a-zA-Z!@#$%&]+@[0-9a-zA-Z]+[.][0-9a-zA-Z]+', data)


# print(len(extractor))
for email in extractor:
    with open("Extracted.txt", "a") as f:
        f.write(f'{i}. {email}\n')
        i+=1
