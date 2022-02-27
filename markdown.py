file = open("aeneid.md")

content = file.readlines()
file.close()

head = 0
while content[head][0:4] != "## L":
	head += 1

line = 0
for m in range(head,len(content)):
	if content[m] != "\n":
		line += 1
		if content[m][0:4] == "## L":
			line = 0
		else:
			if line%5==0:
				content[m] = str(line) + ". " + content[m]
			else:
				content[m] = "- " + content[m]


file = open("new.md","w")
file.writelines(content)
file.close()