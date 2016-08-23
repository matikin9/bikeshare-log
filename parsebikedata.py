from lxml import html

logfile = open("logs/2016-07.html", "r")

content = logfile.read()

print(content)

logfile.close()
