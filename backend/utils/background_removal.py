from rembg import remove
import os
import uuid

def remove_background(image_path):
    """
    Remove background from an image using rembg.

    Args:
        image_path (str): Path to the input image.

    Returns:
        str: Path to the new image with background removed.
    """
    # Open the image file
    with open(image_path, "rb") as file:
        input_image = file.read()

    # Remove background using rembg
    output_image = remove(input_image)

    # Save the new image with a unique name
    base, ext = os.path.splitext(image_path)
    unique_id = uuid.uuid4().hex[:8]
    new_image_path = f"{base}_no_bg_{unique_id}{ext}"
    with open(new_image_path, "wb") as file:
        file.write(output_image)

    return new_image_path