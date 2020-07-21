"""Contains the standard train/test splits for the cyclegan data."""

"""The size of each dataset. Usually it is the maximum number of images from
each domain."""
DATASET_TO_SIZES = {
    'monet2photo_train': 7359,
    'monet2photo_test': 872
}

"""The image types of each dataset. Currently only supports .jpg or .png"""
DATASET_TO_IMAGETYPE = {
    'monet2photo_train': '.jpg',
    'monet2photo_test': '.jpg',
}

"""The path to the output csv file."""
PATH_TO_CSV = {
    'horse2zebra_train': './CycleGAN_TensorFlow/input/horse2zebra/monet2photo_train.csv',
    'horse2zebra_test': './CycleGAN_TensorFlow/input/horse2zebra/monet2photo_test.csv',
}
