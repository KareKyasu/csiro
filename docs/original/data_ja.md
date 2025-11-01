# データセットの説明
## コンペティションの概要
このコンペティションでは、牧草地の画像を用いて、放牧と飼料管理に不可欠な5つの主要なバイオマス成分を予測することが課題となります。

- 乾燥した緑地（クローバーを除く）
- 乾燥した枯死体
- 乾燥したクローバーバイオマス
- 緑地乾物量（GDM）
- 総乾燥バイオマス

これらの量を正確に予測することで、農家や研究者は牧草地の成長を監視し、飼料の供給を最適化し、畜産システムの持続可能性を向上させることができます。

## ファイル

### test.csv

- sample_id — 各予測行の一意の識別子（画像とターゲットのペアごとに1行）。
- image_path — 画像への相対パス（例：test/ID1001187975.jpg）。
- target_name — この行で予測するバイオマス成分の名前。Dry_Green_g、Dry_Dead_g、Dry_Clover_g、GDM_g、Dry_Total_gのいずれか。

テストセットには800枚以上の画像が含まれています。

### train/

- トレーニング画像（JPEG）を含むディレクトリ。image_path で参照されます。

### test/

テスト画像用に予約されたディレクトリ（スコアリング時には非表示）。test.csv 内のパスはこのディレクトリを指します。

### train.csv

- sample_id — 各トレーニングサンプル（画像）の一意の識別子。
- image_path — トレーニング画像への相対パス（例：images/ID1098771283.jpg）。
- Sampling_Date — サンプル採取日。
- State — サンプルが採取されたオーストラリアの州。
- Species — 存在する牧草種。バイオマス順（アンダースコア区切り）。
- Pre_GSHH_NDVI — 正規化植生指数（GreenSeeker）の測定値。
- Height_Ave_cm — フォーリングプレート法で測定した牧草地の平均高（cm）。
- target_name — この行のバイオマス成分名（Dry_Green_g、Dry_Dead_g、Dry_Clover_g、GDM_g、または Dry_Total_g）。
- target — この画像の target_name に対応するグラウンドトゥルースバイオマス値（グラム）。

### sample_submission.csv

- sample_id — test.csv からコピーします。要求された (image, target_name) ペアごとに1行です。
- target — その sample_id に対する予測バイオマス値（グラム）。

## 予測すべき値

test.csv の各 sample_id に対して、sample_submission.csv に1つの数値ターゲット値を出力します。各行は1つの (image_path, target_name) ペアに対応します。その成分の予測バイオマス値（グラム）を指定する必要があります。実際のテスト画像は、スコアリング時にノートブックで利用できます。

## 引用
このデータセットを研究目的で使用する場合は、この論文を引用してください。

```
@misc{liao2025estimatingpasturebiomasstopview,

title={上面画像からの牧草地バイオマス推定：精密農業のためのデータセット},

author={Qiyu Liao、Dadong Wang、Rebecca Haling、Jiajun Liu、Xun Li、Martyna Plomecka、Andrew Robson、Matthew Pringle、Rhys Pirie、Megan Walker、Joshua Whelan},

year={2025},

eprint={2510.22916},

archivePrefix={arXiv},

primaryClass={cs.CV},

url={https://arxiv.org/abs/2510.22916},

}
```