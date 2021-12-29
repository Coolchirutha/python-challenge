# Importing necessary libraries
import urllib.request

# The hint was peak hell which translates to pickle library in
# python which is used for serializing and deserializing a
# python object structure.
import pickle

# This url is obtained from the source code of the webpage.
url = "http://www.pythonchallenge.com/pc/def/banner.p"

# The data is in the form of a byte stream.
encodedData = urllib.request.urlopen(url)

# We use pickle to convert the bytestream data to a tuple
decodedData = pickle.load(encodedData)

# The tuple consists of tuples of dicts of characters
# which are to be printed. So, we print them.
for x in decodedData:
    print("".join(key * val for key, val in x))
