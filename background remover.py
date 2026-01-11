from rembg import remove
from PIL import Image
import io

# Input and output paths
input_path = r"C:\Users\sarab\Downloads\1234.jpg"
output_path = 'output2.png'

try:
    # Open the input image
    with open(input_path, 'rb') as input_file:
        input_image = input_file.read()

    # Remove the background
    output_image_data = remove(input_image)

    # Save the output image
    output_image = Image.open(io.BytesIO(output_image_data))
    output_image.save(output_path)

    print(f"Background removed successfully. Saved to {output_path}")

except FileNotFoundError:
    print(f"Error: The file '{input_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
