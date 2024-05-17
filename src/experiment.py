from yolox.exp.yolox_base import Exp as DefaultExp
from const.const_values import ROOT
import os


class Exp(DefaultExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.num_classes = 80
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = 'sample'

        self.input_size = (640, 640)
        self.test_size = (640, 640)

        # dir of dataset images, if data_dir is None, this project will use `datasets` dir
        self.data_dir = os.path.join(ROOT, "datasets/coco-2017")
        # name of annotation file for training. This file should be under {data_dir}/annotations directory
        self.train_ann = "train_labels.json"
        # name of annotation file for evaluation. . This file should be under {data_dir}/annotations directory
        self.val_ann = "val_labels.json"
        # name of annotation file for test. This file should be under {data_dir}/annotations directory
        self.test_ann = "test_labels.json"
        # name of image directory for train. This directory should be under {data_dir} directory
        self.train_img_dir = "train2017"
        # name of image directory for evaluation. This directory should be under {data_dir} directory
        self.val_img_dir = "val2017"
        # name of image directory for test. This directory should be under {data_dir} directory
        self.test_img_dir = "test2017"

        self.max_epoch = 300

        # TODO
        #  - [ ] 推論時のクラスラベルの指定
        #  - [x] get_dataset (train, val, test) 実装g
        #  - [ ] dataLoader実装

    def get_dataset(self, cache: bool = False, cache_type: str = "ram"):
        """
        Get dataset according to cache and cache_type parameters.
        Args:
            cache (bool): Whether to cache imgs to ram or disk.
            cache_type (str, optional): Defaults to "ram".
                "ram" : Caching imgs to ram for fast training.
                "disk": Caching imgs to disk for fast training.
        """
        from yolox.data import COCODataset, TrainTransform

        return COCODataset(
            data_dir=self.data_dir,
            name=self.train_img_dir,
            json_file=self.train_ann,
            img_size=self.input_size,
            preproc=TrainTransform(
                max_labels=50,
                flip_prob=self.flip_prob,
                hsv_prob=self.hsv_prob
            ),
            cache=cache,
            cache_type=cache_type,
        )

    def get_eval_dataset(self, **kwargs):
        from yolox.data import COCODataset, ValTransform
        testdev = kwargs.get("testdev", False)
        legacy = kwargs.get("legacy", False)

        return COCODataset(
            data_dir=self.data_dir,
            json_file=self.val_ann if not testdev else self.test_ann,
            name=self.val_img_dir if not testdev else self.test_img_dir,
            img_size=self.test_size,
            preproc=ValTransform(legacy=legacy),
        )

