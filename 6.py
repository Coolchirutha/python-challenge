# Importing necessary libraries
import zipfile
import re

# Now the hint in the source code was zip.
# So, when we change the url to channel.zip we get a
# zip file downloaded which contains many txt files each
# linking to another file. Now the target is to open the
# first txt file and follow the numbers till we reach the end.
# Read the readme.txt file for instructions.

# This is the first file we start with (from readme.txt)
nextNothing = "90052"
curStr = ""

# Assigning the open zipfile to a variable
archive = zipfile.ZipFile("external/channel.zip", "r")

# Collecting the comments in an array (Read further for clarification)
comments = []

# Accessing every file till we get to the end
while True:
    try:
        # Opening the txt file in the archive and decoding into a string
        curStr = archive.read(nextNothing + ".txt").decode("utf-8")
        print(curStr)

        # Getting the comment for every file and appending into a list.
        # The reason for getting the comment is because the last
        # file said to collect all the comments. Every zip file
        # can contain a comment for the file in archive. So we get
        # the comment and append to a list
        curComment = archive.getinfo(nextNothing + ".txt").comment
        comments.append(curComment.decode("utf-8"))
        # Getting the next file path
        nextNothing = curStr.split()[-1]
    except:
        # We break the file search when we reach the end which is
        # signified by the file not being found when we try to open it
        break

# Since the obained comments look like a design, we append and print
print("".join(comments))
