# Using urllib.request library to open and read
# the current challenge webpage.
import urllib.request

url = "http://www.pythonchallenge.com/pc/def/ocr.html"
webpage = urllib.request.urlopen(url)
contents = str(webpage.read())
webpage.close()

# splitting the contents of the webpage to extract the relevant data
# here we split the string and get the part from the start of the string
contents = contents.split("<!--")[-1][:-8]

# Creating a hashmap to sto+re the count of each character in the string
mp = {}
for c in contents:
    if c in mp:
        mp[c] += 1
    else:
        mp[c] = 1

# After printing the count of each characters, some characters came out
# to be occurring only once. So, printing out only those characters.
res = ""
for key, val in mp.items():
    if val == 1:
        res += key
print(res)
