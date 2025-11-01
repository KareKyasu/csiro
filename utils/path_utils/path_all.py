from dataclasses import dataclass, fields

from . import pj_root

# リポジトリのルートディレクトリ
REPO_ROOT = pj_root.find_project_root()
# データセットのルートディレクトリ
DATASET_ROOT = REPO_ROOT / "dataset"
