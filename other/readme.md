# 他のKagglerの手法比較

このドキュメントは、`/other` ディレクトリに格納されている他のKaggler（コンペ参加者）の公開Notebookの手法をまとめたものです。
各アプローチの概要を比較し、本コンペティションにおける有効な戦略を探ることを目的とします。

## 手法比較表

| 著者 | モデル / 手法 | LBスコア | 概要 / 特徴 |
| :--- | :--- | :--- | :--- |
| **Aic** | `convnext_tiny` (デュアルストリーム) | - | 5-fold CVアンサンブル + TTA。画像を左右に分割し、3ターゲットを直接予測。 |
| **Chirag_Desai** | `tf_efficientnetv2_s` (マルチヘッド) | - | PyTorch Lightningを使用。5つのターゲットを同時に予測するマルチヘッド構成。 |
| **Jirka_Borovec** | DINOv2 + XGBoost / `efficientnet_b5` | - | DINOv2による特徴抽出 + XGBoostの古典的MLアプローチと、PyTorch LightningによるCNNアプローチの両方を試行。 |
| **Mahou_Lettuce** | `efficientnet_b2` (デュアルブランチ) | 0.57 | PyTorch Lightningを使用。3-foldアンサンブル + TTA。画像を左右に分割するデュアルブランチ構成。 |
| **Manoj** | `convnext_tiny` + DINOv2 + Lasso | **0.59** | `convnext_tiny` (LB 0.57) と DINOv2+Lasso (LB 0.54) の重み付けアンサンブルでスコアを向上。 |
| **Taimo** | `convnext_tiny` (デュアルストリーム) | - | 学習と推論を1つのNotebookで完結させたベースライン。AicやManojと同様のデュアルストリーム構成。 |

## 主な傾向と考察

-   **デュアルストリーム/ブランチアーキテクチャ:** 多くの高スコアアプローチで、画像を左右に分割して処理する手法が採用されています。これは、画像の異なる領域から補完的な情報を抽出するのに有効である可能性を示唆しています。(`Aic`, `Mahou_Lettuce`, `Manoj`, `Taimo`)
-   **モデルアンサンブル:** 複数のモデル（異なるFoldやアーキテクチャ）の予測を組み合わせるアンサンブルは、スコアを安定させ、向上させるための一般的な戦略です。(`Aic`, `Mahou_Lettuce`, `Manoj`)
-   **TTA (Test-Time Augmentation):** 水平反転などの簡単な拡張を推論時に行うことで、精度を向上させるテクニックが広く使われています。
-   **特徴抽出 + MLモデル:** DINOv2のような強力な事前学習済みモデルで画像特徴量を抽出し、XGBoostやLassoといった古典的な機械学習モデルで回帰を行うアプローチも有効なベースラインとなっています。(`Jirka_Borovec`, `Manoj`)
-   **フレームワーク:** `PyTorch Lightning` が、コードの整理や効率的な学習パイプラインの構築のために複数のNotebookで採用されています。(`Chirag_Desai`, `Jirka_Borovec`, `Mahou_Lettuce`)
-   **高スコアモデル:** `convnext_tiny` と `efficientnet` ファミリーがバックボーンとして人気が高いようです。
