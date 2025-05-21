# codex_test_250520

This project uses [Poetry](https://python-poetry.org/) for dependency management with Python **3.12**.

## Setup

1. Install Python 3.12 (e.g. with [pyenv](https://github.com/pyenv/pyenv)).
2. Install Poetry.
3. Run `poetry install` to create the virtual environment.
4. The source code resides in the `imgutil/` package.
   Run the grayscale utility with `python -m imgutil.grayscale <input.png>`.

## Dependencies

The project requires `numpy` **2.2.6** and `opencv-python` **4.11.0.86**.

## Notes

`imgutil/grayscale.py` now reads and writes images using `np.fromfile` and
`cv2.imdecode/encode`. This allows the script to handle file paths that
contain non-ASCII characters (e.g. Japanese) on Windows.
