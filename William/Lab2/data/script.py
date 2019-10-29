file = open('SMSSpamCollection.txt', 'r')
content = file.read()
file.close()
all = content.split("\n")
sub = []
for i in all:
    if '"' not in i:
        sub += [i]

content = ""
for i in sub:
    content += i +  "\\n"
content = content.replace("\t", ",\'")
file = open('SMSSpamCollection.csv', 'w')
file.write(content)
file.close()
