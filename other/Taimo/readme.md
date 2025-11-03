# 学習・推論ベースラインNotebook

## 概要

このNotebookは、CSIRO Image2Biomassコンペティションのための学習と推論のベースラインを提供します。
画像を左右に分割して処理するデュアルストリームアーキテクチャを採用しており、学習と推論の両方のプロセスを単一のNotebookで実行できます。

## モデル

-   **アーキテクチャ:** `convnext_tiny` (timmライブラリより)
-   **特徴:**
    -   デュアルストリーム: 画像を左右に分割し、それぞれの特徴量を結合して利用します。
    -   マルチヘッド: `Dry_Total_g`, `GDM_g`, `Dry_Green_g` の3つのターゲットを同時に予測します。

## 入力

-   **テーブルデータ:** `train.csv`
-   **画像データ:** `train/` ディレクトリ内のJPEG画像

## 処理フロー

1.  **データ準備:** `train.csv` をワイドフォーマットに変換し、層化K-Foldで分割します。
2.  **学習:**
    -   設定されたFold数だけモデルの学習を繰り返します。
    -   各Foldで最良のモデルの重み (`best_model_fold*.pth`) を保存します。
    -   OOF（Out-of-Fold）予測を生成して保存します。
3.  **推論:**
    -   学習済みの全Foldのモデルを自動で読み込み、アンサンブルします。
    -   テストデータに対して予測を行い、提出ファイル (`submission.csv`) を生成します。
    -   TTA (Test-Time Augmentation) にも対応しています。

## 出力

-   **モデルの重み:** `best_model_fold{fold_number}.pth`
-   **提出ファイル:** `submission.csv`
-   **OOF予測:** `oof_fold{fold_number}.csv`

## 主要なライブラリ

-   `torch`
-   `timm`
-   `pandas`
-   `numpy`
-   `opencv-python`
-   `albumentations`
-   `scikit-learn`
