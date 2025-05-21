import sys
from pathlib import Path

import cv2
import numpy as np


def main():
    if len(sys.argv) != 2:
        print("Usage: python grayscale.py <input.png>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.is_file():
        print(f"File not found: {input_path}")
        sys.exit(1)

    # Read the image using OpenCV
    image = cv2.imread(str(input_path))
    if image is None:
        print(f"Failed to read image: {input_path}")
        sys.exit(1)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Build output file path
    output_name = input_path.stem + ".out" + input_path.suffix
    output_path = input_path.with_name(output_name)

    # Save the grayscale image
    if not cv2.imwrite(str(output_path), gray):
        print(f"Failed to write image: {output_path}")
        sys.exit(1)

    print(f"Saved grayscale image to: {output_path}")


if __name__ == "__main__":
    main()
