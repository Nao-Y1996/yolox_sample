# yoloxを用いた物体検出プロジェクト

## 1. 環境構築

### 1.1 ライブラリのインストール

```bash
poetry install
```

### 1.2. YOLOXリポジトリのクローン

YOLOXのリポジトリをサブモジュールとして追加します。
YOLOXのリポジトリを`yolox`ディレクトリのなかに追加します。

```bash
git submodule add git@github.com:Megvii-BaseDetection/YOLOX.git yolox
```

サブモジュールの初期化と更新を行います。

```bash
git submodule init 
git submodule update
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

