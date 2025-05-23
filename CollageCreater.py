from PIL import Image
from tkinter import filedialog, Tk
import math
import os

def select_images():
    """Open a file dialog to select multiple images."""
    root = Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames(
        title='Select Images for Collage',
        filetypes=[('Image Files', '*.jpg *.jpeg *.png *.bmp *.gif')]
    )
    return root.tk.splitlist(file_paths)

def create_collage(images, collage_width=800):
    """Create a collage from a list of image paths."""
    if not images:
        print("No images selected.")
        return

    # Load all images and resize to a uniform size
    loaded_images = [Image.open(img_path) for img_path in images]
    img_width, img_height = loaded_images[0].size
    uniform_size = (200, 200)
    resized_images = [img.resize(uniform_size) for img in loaded_images]

    # Determine grid size
    num_images = len(resized_images)
    cols = int(math.sqrt(num_images))
    rows = math.ceil(num_images / cols)

    collage_height = rows * uniform_size[1]
    collage = Image.new('RGB', (cols * uniform_size[0], collage_height), color='white')

    # Paste images into collage
    for index, img in enumerate(resized_images):
        x = (index % cols) * uniform_size[0]
        y = (index // cols) * uniform_size[1]
        collage.paste(img, (x, y))

    output_path = "collage.jpg"
    collage.save(output_path)
    print(f"Collage saved as {output_path}")
    collage.show()

if __name__ == "__main__":
    image_paths = select_images()
    create_collage(image_paths)
