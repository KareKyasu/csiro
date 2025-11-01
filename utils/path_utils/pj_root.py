# scripts/init_data/yolo_to_coco.py から
from pathlib import Path


# 何階層上まで探すか
def find_project_root(marker=".git") -> Path:
    cur_path = Path(__file__).resolve()
    for parent in [cur_path] + list(cur_path.parents):
        if (parent / marker).exists():
            return parent
    raise FileNotFoundError(f"Not found: {marker}")
