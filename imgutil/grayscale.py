import sys
from pathlib import Path

import cv2
from . import read_image


def main():
    if len(sys.argv) != 2:
        print("Usage: python -m imgutil.grayscale <input.png>")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    if not input_path.is_file():
        print(f"File not found: {input_path}")
        sys.exit(1)

    # Read the image using helper so non-ASCII paths work
    image = read_image(input_path)
    if image is None:
        print(f"Failed to read image: {input_path}")
        sys.exit(1)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Build output file path
    output_name = input_path.stem + ".out" + input_path.suffix
    output_path = input_path.with_name(output_name)

    # Save the grayscale image. Use cv2.imencode/ndarray.tofile so
    # that writing also works with non-ASCII paths.
    success, buffer = cv2.imencode(input_path.suffix, gray)
    if not success:
        print(f"Failed to encode image: {output_path}")
        sys.exit(1)
    try:
        buffer.tofile(str(output_path))
    except Exception as e:
        print(f"Failed to write image: {output_path} ({e})")
        sys.exit(1)

    print(f"Saved grayscale image to: {output_path}")


if __name__ == "__main__":
    main()
