import sys
from pathlib import Path

import cv2
import numpy as np
from . import read_image


def shift_image(img: np.ndarray, dx: int, dy: int) -> np.ndarray:
    """Return image shifted by (dx, dy) using constant border."""
    rows, cols = img.shape[:2]
    M = np.float32([[1, 0, dx], [0, 1, dy]])
    return cv2.warpAffine(
        img,
        M,
        (cols, rows),
        borderMode=cv2.BORDER_CONSTANT,
        borderValue=(0, 0, 0),
    )


def main():
    if len(sys.argv) != 3:
        print("Usage: python -m imgutil.shift <input> <pixels>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    try:
        shift_pixels = int(sys.argv[2])
    except ValueError:
        print("Shift amount must be an integer")
        sys.exit(1)

    if not input_path.is_file():
        print(f"File not found: {input_path}")
        sys.exit(1)

    image = read_image(input_path)
    if image is None:
        print(f"Failed to read image: {input_path}")
        sys.exit(1)

    # Generate shifted images: up, down, left and right
    shifts = [
        (0, -shift_pixels),  # up
        (0, shift_pixels),   # down
        (-shift_pixels, 0),  # left
        (shift_pixels, 0),   # right
    ]
    for i, (dx, dy) in enumerate(shifts, start=1):
        shifted = shift_image(image, dx, dy)
        output_name = f"{input_path.stem}.out_{i}.png"
        output_path = input_path.with_name(output_name)
        success, buffer = cv2.imencode('.png', shifted)
        if not success:
            print(f"Failed to encode image: {output_path}")
            sys.exit(1)
        try:
            buffer.tofile(str(output_path))
        except Exception as e:
            print(f"Failed to write image: {output_path} ({e})")
            sys.exit(1)
        print(f"Saved shifted image to: {output_path}")


if __name__ == "__main__":
    main()
