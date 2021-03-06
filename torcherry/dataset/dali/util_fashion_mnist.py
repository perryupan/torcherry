# -*- coding: UTF-8 -*-

# Author: Perry
# @Create Time: 2020-02-09 23:50


import os
import errno

from torchvision.datasets.utils import download_and_extract_archive


_url = "https://storage.live.com/items/709703FB7C5DF5D6!125?.&authkey=!APufmGmlfphI5M8&e=Xi9Jnw&ithint=.zip"

_MD5 = "7f2f98e499c1736ff3dc4ecba15b2b3e"
_filename = "FASHION_MNIST_records.zip"

_data_root_name = "FASHION_MNIST_tfrecords"

_fashion_mnist_train_filename = "fashion_mnist_train.tfrecords"
_fashion_mnist_train_idxname = "fashion_mnist_train_idx"

_fashion_mnist_test_filename = "fashion_mnist_test.tfrecords"
_fashion_mnist_test_idxename = "fashion_mnist_test_idx"

_raw_root = "raw"
_processed_root = "processed"


def process_fashion_mnist(download_root, is_download=True):
    data_root = os.path.join(download_root, _data_root_name)

    raw_folder = os.path.join(data_root, _raw_root)
    processed_folder = os.path.join(data_root, _processed_root)

    if is_download:
        _download(raw_folder=raw_folder, processed_folder=processed_folder)

    if not _check_exists(processed_folder):
        raise RuntimeError('Dataset not found.' +
                           ' You can use download=True to download it')


def _download(raw_folder, processed_folder):
    if _check_exists(processed_folder):
        return

    _makedir_exist_ok(raw_folder)
    _makedir_exist_ok(processed_folder)

    download_and_extract_archive(_url, download_root=raw_folder, extract_root=processed_folder,
                                 filename=_filename, md5=_MD5)


def _makedir_exist_ok(dirpath):
    """
    Python2 support for os.makedirs(.., exist_ok=True)
    """
    try:
        os.makedirs(dirpath)
    except OSError as e:
        if e.errno == errno.EEXIST:
            pass
        else:
            raise


def _check_exists(processed_folder):
    return (os.path.exists(os.path.join(processed_folder, _fashion_mnist_train_filename)) and
            os.path.exists(os.path.join(processed_folder, _fashion_mnist_train_idxname)) and
            os.path.exists(os.path.join(processed_folder, _fashion_mnist_test_filename)) and
            os.path.exists(os.path.join(processed_folder, _fashion_mnist_test_idxename)))


if __name__ == '__main__':
    process_fashion_mnist("./datasets")
