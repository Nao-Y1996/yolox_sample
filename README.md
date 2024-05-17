# yoloxを用いた物体検出プロジェクト

## 1. 環境構築

### 1.1 クローン

yoloxがサブモジュールとし含まれるため、サブモジュールを一緒にクローンする必要がありす。以下のコマンドリポジトリをクローンしてください

```bash
git clone --recurse-submodules git@github.com:Nao-Y1996/yolox_sample.git
```

`--recurse-submodules`をつけずにクローンした場合は以下のコマンドでyoloサブモジュールを取得してください

```bash
git submodule init 
git submodule update
```

### 1.2 ライブラリのインストール

```bash
poetry shell
poetry install
```

### 1.3. YOLOXのインストール

YOLOXのインストールを行う前に`yolox/requirements.txt`を修正します。
`onnx`と`onnx-simplifier`をコメントアウトしてください。

変更前

```requirements.txt
# 省略
onnx>=1.13.0
onnx-simplifier==0.4.10
```

変更後

```requirements.txt
# 省略
# onnx>=1.13.0
# onnx-simplifier==0.4.10
```

続いて、YOLOXのインストールを行います。

```bash
cd yolox
python setup.py develop
```

インストールが完了したら このコメントアウトを解除してもとに戻してください。
これは、サブモジュールでの変更の管理は煩雑なため、サブモジュールは変更をしないようにする意図があります。


### 1.4. データセットのダウンロード

YOLOXの学習に使用するデータセットとして、[mini-coco128](https://drive.google.com/file/d/16N3u36ycNd70m23IM7vMuRQXejAJY9Fs/view?usp=sharing)
をダウンロードします。
ダウンロードしたzipファイルを解凍し、`datasets`ディレクトリに配置します。
`datases/coco128`のようになっていればOKです。


## データセットの準備

ディレクトリ構成は以下のようになっていることを想定しています。

```
yolox_sample
├── datasets
│   └── coco128  # data_dir
│       └── annotations
│           ├── instances_val2017.json  # json_file
│           └── instances_train2017.json
│       └── val2017  # name
│           ├── 000000000139.jpg
│           ├── 000000000285.jpg
│           ├── ...
│       └── train2017
│           ├── 000000000009.jpg
│           ├── 000000000025.jpg
│           ├── ...
```

