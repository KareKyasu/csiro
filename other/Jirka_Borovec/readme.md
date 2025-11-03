# Jirka_Borovec's Notebooks

このディレクトリには、[Jirka Borovec](https://www.kaggle.com/jirka-borovec) によって作成された、CSIRO - Image2Biomass Prediction コンペティションのための探索的データ分析（EDA）とモデル構築に関するJupyter Notebookが格納されています。

## Notebookの概要

### 1. `CSIRO Image2Biomass EDA.ipynb`

*   **目的**: データセットの探索的データ分析（EDA）。
*   **内容**:
    *   学習データ（`train.csv`）を読み込み、ターゲット変数（バイオマス量）やカテゴリカル変数（州、牧草の種類など）の分布を可視化します。
    *   画像データの一部をサンプル表示し、データへの理解を深めます。
    *   データセットの基本的な統計量や特性を分析します。

### 2. `CSIRO Img2Bio EDA XGBoost.ipynb`

*   **目的**: EDAとXGBoostによるベースラインモデルの構築。
*   **内容**:
    *   `CSIRO Image2Biomass EDA.ipynb` と同様のEDAを行います。
    *   Hugging Faceの `transformers` ライブラリとDINOv2モデルを使用して、画像から特徴量を抽出します。
    *   抽出した画像特徴量と、テーブルデータ（`target_name`など）を組み合わせて、XGBoost回帰モデルを学習させます。
    *   機械学習によるシンプルなベースライン性能の評価を目的としています。

### 3. `CSIRO Img2Bio EDA.ipynb`

*   **目的**: PyTorch Lightningを使用したCNNモデルの構築と学習。
*   **内容**:
    *   PyTorch Lightningと`timm`ライブラリを活用し、効率的な深層学習の実験パイプラインを構築します。
    *   バックボーンとして強力なCNNモデル（例: `efficientnet_h_b5`）を実装し、回帰タスクを解きます。
    *   データ拡張、カスタムデータセット/データモジュール、学習、予測、提出ファイル作成までの一連の流れを実装しています。
    *   より高度なコンピュータビジョンモデルによる性能向上を目指すアプローチです。
