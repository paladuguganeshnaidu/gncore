"""Install the complete developer catalog with recoverable managed retirement."""
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from gncore import GncoreCli
if __name__ == "__main__":
    raise SystemExit(GncoreCli().run(["export", "--all", "--prune-retired", *sys.argv[1:]]))
