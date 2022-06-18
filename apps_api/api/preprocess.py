import torchvision

def image_to_tensor(image):
    """Convert image data to tensor"""
    image_tensor = torchvision.transforms.functional.to_tensor(image)
    return image_tensor