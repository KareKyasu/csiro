# CSIRO - Image2Biomass Prediction ワークスペース
このワークスペースは、Kaggleの「CSIRO - Image2Biomass Prediction」コンペティションのためのものです。

## 概要説明
このコンペは、牧草地の画像を入力として、5種類のバイオマス量を予測する回帰タスクです。

入力 (Input)
モデルの学習と予測に使用するデータは以下の通りです。

## 画像データ:

train/: モデルの学習に使用する牧草地のJPEG画像が含まれています。
test/: 予測対象の画像が含まれています。コンペの採点時に提供されます。
テーブルデータ (CSV):

train.csv: 学習用データです。各画像に対して、以下の情報が提供されます。

image_path: train/ ディレクトリ内の画像ファイルへのパス。
target_name: 予測対象のバイオマス成分の名前。以下の5種類のいずれかです。
Dry_Green_g (クローバーを除く乾燥した緑の植物)
Dry_Dead_g (乾燥した枯れた物質)
Dry_Clover_g (乾燥したクローバー)
GDM_g (緑色乾燥物)
Dry_Total_g (総乾燥バイオマス)
target: 上記 target_name に対応する実際のバイオマス量 (グラム単位)。
その他、Sampling_Date (サンプリング日)、State (サンプリングされたオーストラリアの州)、Species (牧草の種類) などの補助的な情報も含まれており、これらもモデルの入力として利用できます。
注意点: 1つの画像 (image_path) に対して、5つの target_name が存在するため、train.csv 内では1つの画像が5行で表現されます。
test.csv: 提出ファイルを作成するための定義ファイルです。

sample_id: 予測ごと（画像とターゲットのペアごと）に振られたユニークなID。
image_path: test/ ディレクトリ内の画像ファイルへのパス。
target_name: 予測を求められているバイオマス成分の名前。
出力 (Output)
最終的に提出するファイルは sample_submission.csv という形式のCSVファイルです。

sample_submission.csv:
sample_id: test.csv からコピーしたID。
target: あなたのモデルが予測したバイオマス量 (グラム単位の数値)。
タスクの要約

test.csv で指定された各 sample_id（つまり、各画像と各バイオマス成分の組み合わせ）に対して、バイオマス量を予測し、sample_submission.csv の target カラムにその値を記入して提出する必要があります。

## 重要なディレクトリとファイル

データセット:
dataset/source/Image2Biomass: Kaggleからダウンロードした元のデータを格納します。このディレクトリは変更しないでください。
dataset/processed: sourceのデータを加工（圧縮、リサイズ、形式変換など）したものを格納します。ディレクトリ名は 元データ名_処理内容 という命名規則に従います。

パス管理:
プロジェクト内のすべてのファイルパスは、utils/path_utils/path_all.py で一元管理されています。コード内でパスをハードコーディングせず、必ずこのモジュールをインポートして使用してください。

データ加工:
データセットの加工スクリプトは scripts/data_process 配下にあります。

モデル学習・推論:
モデルの学習や推論に関するコードは src ディレクトリにあります。

可視化:
データセットの可視化にはFiftyOneを使用します。data_check.ipynb がその一例です。

ドキュメント:
docs ディレクトリにまとめてあります。
コンペのルールやデータ仕様は docs/original/*.md を参照してください。
アイディアは docs/memo/*.md に記録しています。
docs/memo/idea.md には今後試したいアイディアをリストアップしています。

## 引用
docs/memo/Estimating Pasture Biomass from Top-View Images A Dataset for Precision Agriculture.pdf
docs/memo/Estimating Pasture Biomass Dataset/main.tex
がこのコンペティションのデータセットに関する論文です。
