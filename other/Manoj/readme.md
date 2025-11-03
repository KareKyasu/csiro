# Manoj氏のNotebooks概要

このディレクトリには、KaggleユーザーManoj氏によって作成された、CSIRO Image2Biomassコンペティション用のNotebookが格納されています。
それぞれ異なるアプローチによる推論やモデル構築の実験が行われています。

---

## 各Notebookの概要

### 1. `LB 0.57 Infer Model Code.ipynb`

#### 概要
このJupyter Notebookは、LBスコア0.57を達成したモデルの推論処理を実装したものです。
学習済みの5-FoldモデルアンサンブルとTest Time Augmentation (TTA) を用いて、テストデータのバイオマス量を予測し、提出用の `submission.csv` を生成します。

#### モデル
-   **アーキテクチャ:** `convnext_tiny` (timmライブラリ)
-   **戦略:** Two-Stream, Multi-Head
    -   入力画像 (2000x1000) を左右2つのパッチ (1000x1000) に分割。
    -   各パッチを `768x768` にリサイズし、共有のバックボーンに入力します。
    -   結合された特徴量を、3つのターゲット (`Dry_Total_g`, `GDM_g`, `Dry_Green_g`) それぞれに対応する3つのMLPヘッドで個別に予測します。

---

### 2. `CSIRO Image2Biomass LB 59.ipynb`

#### 概要
このNotebookは、複数のモデルの予測結果をアンサンブルすることで、LBスコア0.59を目指す複雑な推論パイプラインです。`convnext_tiny`と`DINOv2`という2種類のアーキテクチャを組み合わせています。

#### 手法
1.  **`convnext_tiny`による推論:**
    -   `LB 0.57 Infer Model Code.ipynb`と同様のTwo-Stream, Multi-Headアーキテクチャを持つ`convnext_tiny`モデルを使用し、5-FoldアンサンブルとTTAで予測を行います。
2.  **`DINOv2` + `Lasso`による推論:**
    -   `DINOv2` (baseおよびgiant) を用いて画像から特徴量を抽出します。
    -   抽出した特徴量を入力として、ターゲットごとに学習させた`Lasso`回帰モデルで予測を行います。
3.  **最終アンサンブル:**
    -   上記で得られた複数の予測結果（`convnext_tiny`、`DINOv2-base`、`DINOv2-giant`など）を、重み付け平均することで最終的な提出ファイルを生成します。

---

### 3. `DINOv2 Lasso Baseline LB 0.54.ipynb`

#### 概要
このNotebookは、`DINOv2`と古典的な機械学習モデルである`Lasso`回帰を組み合わせたベースラインです。LBスコア0.54を達成しています。

#### 手法
1.  **特徴量抽出:**
    -   事前学習済みの`DINOv2`モデル（`dinov2-base`）を使用して、各画像から高次元の特徴量ベクトルを抽出します。
2.  **モデル学習:**
    -   抽出した特徴量を入力データ、バイオマスの各ターゲットを目的変数として、ターゲットごとに`Lasso`回帰モデルを学習させます。学習は5-Foldクロスバリデーションで行われます。
3.  **推論:**
    -   テスト画像から同様に特徴量を抽出し、学習済みの5つの`Lasso`モデルで予測を行い、その平均値を最終的な予測結果とします。
