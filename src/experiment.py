from yolox.exp.yolox_base import Exp as DefaultExp
from const.const_values import ROOT
import os


class Exp(DefaultExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.num_classes = 14
        self.depth = 0.33
        self.width = 0.50
        self.exp_name = 'sample'

        # dir of dataset images, if data_dir is None, this project will use `datasets` dir
        self.data_dir = os.path.join(ROOT, "datasets/coco128/train2017")
        # name of annotation file for training
        self.train_ann = os.path.join(ROOT, "datasets/coco128/annotations/instances_train2017.json")
        # name of annotation file for evaluation
        self.val_ann = os.path.join(ROOT, "datasets/coco128/annotations/instances_val2017.json")
        # name of annotation file for testing
        self.test_ann = os.path.join(ROOT, "datasets/coco128/annotations/instances_val2017.json")

        self.max_epoch = 300

