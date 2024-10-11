from PIL import Image

def superimpose_images(base_image_path, overlay_image_path, output_image_path, position=(0, 0), transparency=0.5):
    # Open the base image and overlay image
    base_image = Image.open(base_image_path).convert("RGBA")
    overlay_image = Image.open(overlay_image_path).convert("RGBA")

    overlay_image = overlay_image.resize(base_image.size)

    # Adjust transparency of the overlay by creating a new image with an alpha channel
    alpha_overlay = overlay_image.copy()
    alpha = int(255 * transparency)
    # Apply transparency to the overlay image
    for y in range(overlay_image.height):
        for x in range(overlay_image.width):
            r, g, b, a = overlay_image.getpixel((x, y))
            alpha_overlay.putpixel((x, y), (r, g, b, min(a, alpha)))

    combined_image = Image.alpha_composite(base_image, alpha_overlay)
    combined_image.save(output_image_path, "PNG")
    print(f"Image saved as {output_image_path}")

base_image_path = "scrambled1.png"
overlay_image_path = "scrambled2.png"
output_image_path = "flag.png"
superimpose_images(base_image_path, overlay_image_path, output_image_path, position=(0, 0), transparency=0.5)