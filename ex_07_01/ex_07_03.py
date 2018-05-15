
fname = input("Enter file name: ")
count = 0

try:
	fhand = open(fname)
except: 
	if line.upper() == "Na na boo":
		print("Na Na boo") 
	else:
		print("File can't be opened: ", fname)
		quit()
for line in fhand:
	if line.startswith('Subject:'):
		count = count + 1
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print("There were {0} subject lines in {1}.".format(str(count), fname))  
	