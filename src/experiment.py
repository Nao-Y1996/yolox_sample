from yolox.exp.yolox_base import Exp as DefaultExp
from const.const_values import ROOT
import os


class Exp(DefaultExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.num_classes = 2
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = 'sample'

        self.input_size = (640, 640)
        self.test_size = (640, 640)

        # dir of dataset images, if data_dir is None, this project will use `datasets` dir
        self.data_dir = os.path.join(ROOT, "datasets/coco-2017/images")
        # name of annotation file for training
        self.train_ann = os.path.join(ROOT, "datasets/coco-2017/train/labels.json")
        # name of annotation file for evaluation
        self.val_ann = os.path.join(ROOT, "datasets/coco-2017/validation/labels.json")
        # name of annotation file for testing
        self.test_ann = os.path.join(ROOT, "datasets/coco-2017/test/labels.json")

        self.max_epoch = 300

        # TODO
        #  - クラスの指定
        #  - get_dataset (train, val, test) 実装
        #  - dataLoader実装

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
            name="",
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

