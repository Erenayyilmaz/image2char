from PIL import Image

# Define the ASCII characters to use
ASCII_CHARS = [' ', '.', ':', '-', '=', '+', '*', '#', '%', '@']

# Define the block size
BLOCK_SIZE = 10

# Load the input image and resize it
image = Image.open("messi.png").resize((200, 200))

# Convert the image to grayscale
gray_image = image.convert("L")

# Define the threshold value to map grayscale values to intervals
threshold = 10

# Iterate over the blocks in the grayscale image and map the grayscale values to ASCII characters
ascii_blocks = []
for y in range(0, gray_image.height, BLOCK_SIZE):
    ascii_row = []
    for x in range(0, gray_image.width, BLOCK_SIZE):
        block = gray_image.crop((x, y, x+BLOCK_SIZE, y+BLOCK_SIZE))
        average = block.getbbox() and round(sum(block.histogram()) / (BLOCK_SIZE * BLOCK_SIZE))
        # Map average grayscale value to ASCII character index
        ascii_index = int(average / 255 * len(ASCII_CHARS))
        # Append ASCII character to row
        ascii_row.append(ASCII_CHARS[ascii_index])
    # Join row with empty string and append newline character
    ascii_blocks.append("".join(ascii_row) + "\n")

# Return ASCII art as a string instead of printing it
print( "".join(ascii_blocks))

