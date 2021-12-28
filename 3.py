# Using urllib.request library to open and read
# the current challenge webpage.
import urllib.request

# Importing regex library
import re

url = "http://www.pythonchallenge.com/pc/def/equality.html"
webpage = urllib.request.urlopen(url)
contents = str(webpage.read())
webpage.close()

# splitting the contents of the webpage to extract the relevant data
contents = contents.split("<!--")[-1][:-8]

# Removing all the newlines to better iterate over the string
contents = contents.replace("\\n", '')

# This is the regex for finding a lowercase alphabet
# surrounded by exactly 3 uppercase characters.
reg = "[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]"

# Searching for the matches in the given string
match = re.findall(reg, contents)

# Initializing result
res = ""

# Adding all letters
for c in match:
  res += c

print(res)
