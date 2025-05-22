import shutil
import sys
from pathlib import Path
import subprocess


def test_shift_output():
    """Run shift script and check output images."""
    src = Path(__file__).parent / "img" / "日本語.jpg"
    dst = Path("/tmp") / src.name
    shutil.copy(src, dst)

    try:
        subprocess.run(
            [sys.executable, "-m", "imgutil.shift", str(dst), "10"],
            check=True,
        )
    finally:
        pass

    for i in range(1, 5):
        out_path = dst.with_name(f"{dst.stem}.out_{i}.png")
        assert out_path.is_file(), f"Output image not found: {out_path}"
        assert out_path.stat().st_size > 0, f"Output image {i} is empty"
        out_path.unlink(missing_ok=True)

    dst.unlink(missing_ok=True)
