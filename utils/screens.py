from PIL import ImageChops
import numpy as np

def screenshots_different(img1, img2):
    """
    Returns percentage of pixels that changed between two images
    """
    # Ensure same mode & size
    if img1.size != img2.size:
        raise ValueError("Images must be same size")

    diff = ImageChops.difference(img1, img2)

    diff_np = np.array(diff)

    # If RGB, reduce to grayscale-like magnitude
    if diff_np.ndim == 3:
        diff_np = diff_np.max(axis=2)

    changed_pixels = np.count_nonzero(diff_np)
    total_pixels = diff_np.size

    percent_changed = (changed_pixels / total_pixels) * 100
    return percent_changed


def screenshots_color_different(img1, img2, threshold=5):
    img1 = img1.convert("RGB")
    img2 = img2.convert("RGB")

    if img1.size != img2.size:
        raise ValueError("Images must be same size")

    diff = ImageChops.difference(img1, img2)
    diff_np = np.array(diff)

    if diff_np.ndim == 3:
        diff_np = diff_np.max(axis=2)

    # Only count pixels above threshold
    changed_pixels = np.count_nonzero(diff_np > threshold)
    total_pixels = diff_np.size

    return (changed_pixels / total_pixels) * 100


def screenshot_change_percent(img1, img2):
    """
    Returns percentage of pixels that changed between two images
    """
    # Ensure same mode & size
    if img1.size != img2.size:
        raise ValueError("Images must be same size")

    diff = ImageChops.difference(img1, img2)

    diff_np = np.array(diff)

    # If RGB, reduce to grayscale-like magnitude
    if diff_np.ndim == 3:
        diff_np = diff_np.max(axis=2)

    changed_pixels = np.count_nonzero(diff_np)
    total_pixels = diff_np.size

    percent_changed = (changed_pixels / total_pixels) * 100
    return percent_changed