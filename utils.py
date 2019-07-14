file_name = "requirements.txt"

myset = set()

with open(file_name, 'r') as reqs:
    for line in reqs:
        print(line)
        req_name = line.split("==")

        myset.add(req_name[0])

mylist = list(myset)
print(mylist)
mylist.sort()
print(mylist)

new_file = "reqs_new.txt"
with open(new_file, 'w') as nf:
    for item in mylist:
        nf.write(item)
        nf.write('\n')
