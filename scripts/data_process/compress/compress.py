# 画像をjpeg形式で圧縮するスクリプト

import shutil
from pathlib import Path

from path_utils import path_all
from PIL import Image


def compress_images(input_dir, output_dir, quality=85):
    """
    指定されたディレクトリ内の画像を圧縮し、別のディレクトリに保存する。

    :param input_dir: 圧縮対象の画像が含まれるディレクトリ
    :param output_dir: 圧縮後の画像を保存するディレクトリ
    :param quality: JPEGの圧縮品質 (1-95)
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)

    if not input_path.exists():
        print(f"エラー: 入力ディレクトリが見つかりません: {input_path}")
        return

    supported_formats = [".jpg", ".jpeg", ".png"]
    image_files = [f for f in input_path.iterdir() if f.is_file() and f.suffix.lower() in supported_formats]

    if not image_files:
        print("圧縮対象の画像が見つかりませんでした。")
        return

    print(f"{len(image_files)}個の画像を圧縮します...")

    for image_file in image_files:
        try:
            with Image.open(image_file) as img:
                # RGBA (PNGなど) の場合はRGBに変換してJPEGで保存
                if img.mode == "RGBA":
                    img = img.convert("RGB")
                if img.mode != "RGB":
                    img = img.convert("RGB")
                # 新しいファイル名を作成 (拡張子を.jpgに統一)
                new_filename = image_file.stem + ".jpg"
                output_file_path = output_path / new_filename
                if output_file_path.exists():
                    print(f"  - スキップ: {output_file_path.name} は既に存在します。")
                    continue

                # 画像を保存
                img.save(output_file_path, "JPEG", quality=quality, optimize=True)
                original_size = image_file.stat().st_size / 1024  # KB
                compressed_size = output_file_path.stat().st_size / 1024  # KB
                print(
                    f"  - {image_file.name} ({original_size:.2f} KB) -> "
                    f"{output_file_path.name} ({compressed_size:.2f} KB)"
                )
        except Exception as e:
            print(f"エラー: {image_file.name} の処理中にエラーが発生しました: {e}")

    print("画像の圧縮が完了しました。")


if __name__ == "__main__":
    input_dirs = []
    output_dirs = []

    input_dirs.append(path_all.DATASET_ROOT / "source" / "Image2Biomass" / "train")
    input_dirs.append(path_all.DATASET_ROOT / "source" / "Image2Biomass" / "test")
    output_dirs.append(path_all.DATASET_ROOT / "processed" / "compress" / "train")
    output_dirs.append(path_all.DATASET_ROOT / "processed" / "compress" / "test")

    # 出力ディレクトリが存在しない場合は作成
    for d in output_dirs:
        # 画像ディレクトリに関して
        if not d.exists():
            d.mkdir(parents=True, exist_ok=True)

    # 圧縮を実行
    for input_d, output_d in zip(input_dirs, output_dirs):
        compress_images(input_d, output_d)
