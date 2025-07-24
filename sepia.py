from PIL import Image

def apply_sepia(input_image_path, output_image_path):
    image = Image.open(input_image_path).convert("RGB")
    width, height = image.size
    pixels = image.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]

            tr = int(0.393 * r + 0.769 * g + 0.189 * b)
            tg = int(0.349 * r + 0.686 * g + 0.168 * b)
            tb = int(0.272 * r + 0.534 * g + 0.131 * b)

            tr = min(255, tr)
            tg = min(255, tg)
            tb = min(255, tb)

            pixels [x, y] = (tr, tg, tb)

    print(f"Sample pixel after sepia: {pixels[0, 0]}")
    print(f"Saving image as {output_image_path}...")
    image.save(output_image_path)
    print("Done!")

apply_sepia("smokey.gif", "output_sepia.jpg")
