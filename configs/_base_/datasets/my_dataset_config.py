# 在./mmseg/datasets/__init__.py 中定义的数据集类型
dataset_type = 'MyDataset'
# 数据集准备生成的文件夹路径
data_root = 'data/my_dataset'

img_norm_cfg = dict(  # 常用这组参数归一化是因为它是 ImageNet 1K 预训练使用的图像均值与方差
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)

crop_size = (512, 512)  # 训练时图像裁剪的大小
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', reduce_zero_label=True),
    dict(type='Resize', img_scale=(512, 512), ratio_range=(0.5, 2.0)),
    dict(type='RandomCrop', crop_size=crop_size, cat_max_ratio=0.75),
    dict(type='RandomFlip', prob=0.5),
    dict(type='PhotoMetricDistortion'),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size=crop_size, pad_val=0, seg_pad_val=255),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_semantic_seg']),
]







test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(512, 512),
        # img_ratios=[0.5, 0.75, 1.0, 1.25, 1.5, 1.75],
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]


train_dataloader = dict(
    batch_size=4,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='InfiniteSampler', shuffle=True),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        data_prefix=dict(
            img_path='Images/img', seg_map_path='Images/lab'),
        ann_file='ImageSets/Segmentation/train.txt',
        pipeline=train_pipeline))

val_dataloader = dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        data_prefix=dict(
            img_path='Images/img', seg_map_path='Images/lab'),
        ann_file='ImageSets/Segmentation/val.txt',
        pipeline=test_pipeline))
test_dataloader =  dict(
    batch_size=1,
    num_workers=4,
    persistent_workers=True,
    sampler=dict(type='DefaultSampler', shuffle=False),
    dataset=dict(
        type=dataset_type,
        data_root=data_root,
        data_prefix=dict(
            img_path='Images/img', seg_map_path='Images/lab'),
        ann_file='ImageSets/Segmentation/test.txt',
        pipeline=test_pipeline))

val_evaluator = dict(type='IoUMetric', iou_metrics=['mIoU'])
test_evaluator = val_evaluator


# data = dict(
#     samples_per_gpu=4,  # 单个 GPU 的 Batch size
#     workers_per_gpu=4,  # 单个 GPU 分配的数据加载线程数
#     train=dict(  # 训练数据集配置
#         type=dataset_type,  # 数据集的类别, 细节参考自 mmseg/datasets/
#         data_root=data_root,  # 数据集的根目录。
#         img_dir='img_dir/train',  # 数据集图像的文件夹
#         ann_dir='ann_dir/train',  # 数据集注释的文件夹
#         pipeline=train_pipeline),  # 流程， 由之前创建的 train_pipeline 传递进来
#     val=dict(  # 验证数据集的配置
#         type=dataset_type,
#         data_root=data_root,
#         img_dir='img_dir/val',
#         ann_dir='ann_dir/val',
#         pipeline=test_pipeline),  # 由之前创建的 test_pipeline 传递的流程
#     test=dict(
#         type=dataset_type,
#         data_root=data_root,
#         img_dir='img_dir/val',
#         ann_dir='ann_dir/val',
#         pipeline=test_pipeline))