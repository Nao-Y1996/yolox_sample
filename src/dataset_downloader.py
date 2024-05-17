import os
import shutil

import fiftyone as fo
from fiftyone import zoo

from const.const_values import ROOT

if __name__ == '__main__':

    dataset_name = "coco-2017"
    val_dataset = zoo.datasets.load_zoo_dataset(
        name=dataset_name,
        split="validation",
        label_types=["detections"],
        classes=["car", "person"],  # 対象のクラスを指定
        max_samples=100,  # ダウンロードするサンプル数の上限
        dataset_dir=os.path.join(ROOT, f"datasets/{dataset_name}")
    )

    train_dataset = zoo.datasets.load_zoo_dataset(
        name=dataset_name,
        split="train",
        label_types=["detections"],
        classes=["car", "person"],  # 対象のクラスを指定
        max_samples=300,  # ダウンロードするサンプル数の上限
        dataset_dir=os.path.join(ROOT, f"datasets/{dataset_name}")
    )

    test_dataset = zoo.datasets.load_zoo_dataset(
        name=dataset_name,
        split="test",
        label_types=["detections"],
        classes=["car", "person"],  # 対象のクラスを指定
        max_samples=50,  # ダウンロードするサンプル数の上限
        dataset_dir=os.path.join(ROOT, f"datasets/{dataset_name}")
    )

    # 画像データの移動先ディレクトリのパス
    dataset_dir = os.path.join(ROOT, "datasets", dataset_name)
    dest_dir = os.path.join(str(dataset_dir), 'images')
    # ディレクトリが存在しない場合は作成
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # 移動するディレクトリリスト
    sub_dirs = ['train/data', 'validation/data', 'test/data']

    # 各ディレクトリ内のファイルを移動
    for sub_dir in sub_dirs:
        src_dir = os.path.join(str(dataset_dir), sub_dir)
        for filename in os.listdir(src_dir):
            src_file = os.path.join(src_dir, filename)
            dest_file = os.path.join(dest_dir, filename)
            if os.path.isfile(src_file):
                shutil.move(src_file, dest_file)
        # delete sub_dir
        shutil.rmtree(src_dir)
