# Importing the necessary image processing library
from PIL import Image

# Gives an image object to work with
oxygen = Image.open("external/oxygen.png")

# In the given image, there is a small section where it is of a
# different color. So when we print out the rgb color values of
# those pixels we get a tuple of numbers which when converted
# to character using the ASCII table we get text which i am printing out.
s = ""
for x in range(0, 607, 7):
    s += chr(oxygen.getpixel((x, 47))[0])

print(s)

# Now, finally we need to convert the current tuple to string
toConvert = [105, 110, 116, 101, 103, 114, 105, 116, 121]

res = ""
for i in toConvert:
  res += chr(i)

print(res)
