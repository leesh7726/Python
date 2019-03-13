'''
test1 = open("c:\\Python37\\test2.py", "r")

while True:
    line = test1.readline()
    print(line)
    if not line:
        break;


'''


test1 = open("c:\\Python37\\test2.py", "r")
lines = test1.read(20)
print(lines)
