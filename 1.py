# Using urllib.request library to open and read
# the current challenge webpage.
import urllib.request
url = "http://www.pythonchallenge.com/pc/def/map.html"
webpage = urllib.request.urlopen(url)
contents = str(webpage.read())
webpage.close()

# splitting the contents of the webpage to extract the relevant data
# here we split the string and get the part from the start of the string
contents = contents.split("<font color=\"#f000f0\">")[-1]

# Here we split the content till the end of the string and remove the newline characters at the start and end as well.
contents = contents.split("</tr>")[0][2:-2]

# Creating an empty string for the translated string
res = ""

# Iterate over the string and transpose every letter we find with
# the second next. Example: a->c, b->d, ... , z->b
for c in contents:
  # Here 97 is the ASCII code for 'a' and 122 is for 'z'
  if ord(c) >= 97 and ord(c) <=122:
    # Checking for overflow
    if ord(c) + 2 >= 123:
      res += chr((ord(c) + 2) - 26)
    else:
      res += chr(ord(c) + 2)
  else:
    res += c

print(res)
