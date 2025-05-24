from pathlib import Path

import cv2
import numpy as np


def read_image(path: Path) -> np.ndarray | None:
    """Return image read from the given path or ``None`` on failure."""
    image_data = np.fromfile(str(path), dtype=np.uint8)
    return cv2.imdecode(image_data, cv2.IMREAD_COLOR)

