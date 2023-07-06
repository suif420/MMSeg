from mmseg.registry import DATASETS
from .basesegdataset import BaseSegDataset


# 将 MyDataset 类注册到 DATASETS 里
@DATASETS.register_module()
class MyDataset(BaseSegDataset):
    # # 数据集标注的各类名称，即 0, 1, 2, 3... 各个类别的对应名称
    # CLASSES = ('outcrop', 'crack')
    # # 各类类别的 BGR 三通道值，用于可视化预测结果
    # PALETTE = [[255, 255, 255], [0, 0, 255]]

    METAINFO = dict(
        classes=('outcrop', 'crack'),
        palette=[[255, 255, 255], [0, 0, 255]])
    # 图片和对应的标注，这里对应的文件夹下均为 .png 后缀

    # -------------------#
    # reduce_zero_label = False : 此时 label 里的 0（上面 CLASSES 里第一个 “label_a”）在计算损失函数和指标时不会被忽略
    # reduce_zero_label = True  : 如果 label 中的 0 是背景并且想在计算评价指标的时候忽略掉它，需要设置
    def __init__(self,
                 img_suffix='.png',
                 seg_map_suffix = '.png',
                 reduce_zero_label = True,
                 **kwargs)->None:
        super().__init__(
            img_suffix=img_suffix,
            seg_map_suffix=seg_map_suffix,
            reduce_zero_label=reduce_zero_label,
            **kwargs)