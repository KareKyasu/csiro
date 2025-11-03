# LB 0.57 PyTorch Lightning推論Notebook

## 概要
このNotebookは、Kaggleの「CSIRO - Image2Biomass Prediction」コンペティションにおいて、学習済みのCNNモデルを使用してバイオマス量を予測し、提出ファイルを作成するためのものです。PyTorch Lightningをフレームワークとして利用しています。

## モデル
- **アーキテクチャ:** `efficientnet_b2`
- **特徴:**
    - 画像を中央で左右2つに分割し、両方の半分を同時にモデルに入力するデュアルブランチアーキテクチャを採用しています。
    - 3つの異なるFoldで学習されたモデルのアンサンブルにより、予測の頑健性を高めています。
    - Test Time Augmentation (TTA) を適用し、精度を向上させています。

## フレームワーク
- `PyTorch Lightning`

## 入力
- **テーブルデータ:** `test.csv` - 予測対象の画像パスやターゲット名が含まれます。
- **画像データ:** `test/` ディレクトリ内のJPEG画像。

## 処理フロー
1.  `test.csv`を読み込み、推論対象の画像パスを取得します。
2.  `InferenceDataset`クラスを用いて、画像を読み込み、左右に分割してテンソルに変換するデータセットを準備します。
3.  3つのFoldそれぞれについて、学習済みの`efficientnet_b2`モデル（`.ckpt`ファイル）をロードします。
4.  各Foldのモデルで、Test Time Augmentation (水平反転、垂直反転) を行いながら予測値を計算します。
5.  3つのFoldの予測結果を平均し、最終的な予測値とします。
6.  モデルの出力（3つのターゲット）から、提出に必要な5つのバイオマスターゲット（`Dry_Green_g`, `Dry_Dead_g`, `Dry_Clover_g`, `GDM_g`, `Dry_Total_g`）を計算します。
7.  計算結果を`submission.csv`形式に整形します。

## 出力
- `submission.csv`: Kaggleコンペティションへの提出用ファイル。

## 主要なライブラリ
- `pytorch-lightning`
- `torch`
- `timm`
- `pandas`
- `numpy`
- `scikit-learn`
- `PIL`
- `torchvision`
