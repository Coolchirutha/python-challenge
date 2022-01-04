# Using requests library to get the data and Image for processing
import requests
from PIL import Image

# Getting the html response using the credentials set
r = requests.get(
    "http://www.pythonchallenge.com/pc/return/good.html", auth=("huge", "file")
)

# Extracting html from response and splitting for the array
data = r.text.split("<!--")[-1][17:-5].strip()

# Extracting the array and converting the array of string to int
first = [int(num) for num in data.split(":")[-2][:-6].strip().split(",")]
second = [int(num) for num in data.split(":")[-1].strip().split(",")]

# Combining the arrays
allDots = first + second

# Creating a new black blank image
img = Image.new("RGB", (640, 480))

# For all the elements in the array, we assume pairs and mark the
# pixels as white into the image we created and saving the image
for i in range(0, len(allDots), 2):
    img.putpixel((allDots[i], allDots[i + 1]), (255, 255, 255, 255))

img.save("external/nine.png")
