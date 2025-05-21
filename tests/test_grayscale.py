import shutil
import sys
from pathlib import Path
import subprocess


def test_grayscale_output():
    """Run grayscale script on 日本語.jpg and check output in /tmp."""
    # Copy the test image to /tmp with its Japanese name
    src = Path(__file__).parent / "img" / "日本語.jpg"
    dst = Path("/tmp") / src.name
    shutil.copy(src, dst)

    try:
        subprocess.run(
            [sys.executable, "-m", "imgutil.grayscale", str(dst)],
            check=True,
        )
    finally:
        pass

    out_path = dst.with_stem(dst.stem + ".out")
    assert out_path.is_file(), f"Output image not found: {out_path}"
    assert out_path.stat().st_size > 0, "Output image is empty"

    # Clean up generated files
    dst.unlink(missing_ok=True)
    out_path.unlink(missing_ok=True)
