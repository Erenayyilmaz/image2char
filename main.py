from PIL import Image
import sys

args = sys.argv


ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " "]

BLOCK_WIDTH = 4
BLOCK_HEIGHT = 5

#image = Image.open("messi2.png")
image = Image.open(args[1])
width, height = image.size
new_width = int(width / BLOCK_WIDTH)
new_height = int(height / BLOCK_HEIGHT)
resized_image = image.resize((new_width, new_height))

grayscale_image = resized_image.convert("L")

blocks = []
for i in range(0, new_height):
    y = i * BLOCK_HEIGHT
    row = []
    for j in range(0, new_width):
        x = j * BLOCK_WIDTH
        block = grayscale_image.crop((x, y, x + BLOCK_WIDTH, y + BLOCK_HEIGHT))
        row.append(block)
    blocks.append(row)

ascii_image = ""
for row in blocks:
    ascii_row = ""
    for block in row:
        grayscale_values = block.getdata()
        average = sum(grayscale_values) / len(grayscale_values)
        ascii_value = ASCII_CHARS[int(average / 255 * (len(ASCII_CHARS) - 1))]
        ascii_row += ascii_value
    ascii_image += ascii_row + "\n"

print(ascii_image)


