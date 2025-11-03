# CSIRO Image to Biomass - EfficientNetV2 Baseline

## 概要

このNotebookは、Kaggleの「CSIRO - Image2Biomass Prediction」コンペティションに対するベースラインソリューションです。牧草地の画像を入力として、5種類のバイオマス量を予測する回帰モデルを学習し、提出ファイルを作成します。

## モデル

-   **アーキテクチャ:** `timm` ライブラリの `tf_efficientnetv2_s_in21k` をバックボーンとして使用しています。
-   **フレームワーク:** `PyTorch Lightning` を使用して、学習プロセスを効率化しています。
-   **出力層:** 5つのバイオマスターゲットに対応する線形層（Multi-head Regression）。

## 入力

-   **`train.csv`**: 学習用の画像パス、メタデータ（サンプリング日、州、牧草の種類など）、および5種類のバイオマスのターゲット値が含まれています。
-   **`test.csv`**: 予測対象の画像パスとメタデータが含まれています。
-   **画像データ**: `train/` および `test/` ディレクトリにあるJPEG形式の牧草地画像。

## 処理フロー

1.  **セットアップ**: 必要なライブラリ（`timm`, `albumentations`, `pytorch-lightning`など）をインストールします。
2.  **データ読み込みと前処理**: `train.csv`を読み込み、ロングフォーマットからワイドフォーマットへ変換します。
3.  **探索的データ分析 (EDA)**: ターゲットの分布、相関、メタデータ、画像特性などを可視化して分析します。
4.  **データ拡張 (Augmentation)**: `albumentations` を使用して、リサイズ、反転、回転、色調変更などの画像拡張を適用します。
5.  **データセットの準備**: PyTorchの`Dataset`と`DataLoader`を作成し、学習用と検証用にデータを分割します。
6.  **モデルの学習**: `PyTorch Lightning`を用いて`EfficientNetV2-S`モデルを学習させます。損失関数には`SmoothL1Loss`、評価指標には加重R2スコアを使用します。
7.  **推論**: 学習済みの最良モデルを使い、テストデータに対して予測を行います。Test Time Augmentation (TTA)を適用して予測精度を向上させます。
8.  **提出ファイルの作成**: 予測結果を`submission.csv`として出力します。

## 出力

-   **`submission.csv`**: `sample_id`と予測された`target`値を含む提出ファイル。

## 主要なライブラリ

-   `pandas`
-   `numpy`
-   `timm`
-   `albumentations`
-   `pytorch-lightning`
-   `torch`
-   `opencv-python` (`cv2`)
-   `matplotlib`
-   `scikit-learn`
