from dataclasses import dataclass, fields

from . import pj_root

# リポジトリのルートディレクトリ
REPO_ROOT = pj_root.find_project_root()
# データセットのルートディレクトリ
DATASET_ROOT = REPO_ROOT / "dataset"

COMP_DIR = DATASET_ROOT / "processed/compress/"
TRAIN_CSV = DATASET_ROOT / "processed/compress/train.csv"
