# Using urllib.request library to open and read
# the current challenge webpage.
import urllib.request

# Importing regex library
import re

# This is the base url string which we will use to run pings
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="

# Initial value
curVal = "12345"

# Concat string with val and getting the contents for new val
curpage = urllib.request.urlopen(url + curVal)
curContents = str(curpage.read())
curpage.close()

# Extract the value required to navigate to next page
curVal = curContents.split()[-1][:-1]
print(curVal)

# Pinging current url and getting new val and repeating 400 times
for i in range(0, 400):
    curpage = urllib.request.urlopen(url + curVal)
    curContents = str(curpage.read())
    curpage.close()
    curVal = curContents.split()[-1][:-1]
    print(str(i) + " : " + str(curVal))

# After the 399th or some execution we get the
# next html link which is the answer.
