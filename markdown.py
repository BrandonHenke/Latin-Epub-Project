file = open("Metamorphoseon.md")

content = file.readlines()
file.close()

print(len(content[0][-3:-1]))

for n in range(len(content)):
	# print(line[-2:])
	# if content[n][-3:-1] != "  ":
	# 	if content[n][-1] == "\n":
	# 		content[n] = content[n][:-1] + "  " + content[n][-1:]
	# 	else:
	# 		content[n] += " "
	# content[n].replace("\t","&nbsp;") # 1 space tabs
	# content[n].replace("\t","&ensp;") # 2 space tabs
	content[n].replace("\t","&emsp;") # 4 space tabs


file = open("New.md","w")
file.writelines(content)
file.close()
