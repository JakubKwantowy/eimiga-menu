import sys

with open(sys.argv[1], "br") as file:
    content = file.read()
print(len(content))

dumped = ";".join([str(i) for i in content])
with open("dump.txt","w") as file:
    file.write(dumped)
