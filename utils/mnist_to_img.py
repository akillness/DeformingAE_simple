
# this is opensource from github : https://gist.github.com/xkumiyu/c93222f2dce615f4b264a9e71f6d49e0
import argparse
import gzip
import pathlib
import struct

import numpy as np
import pandas as pd
import requests

from tqdm import tqdm
from PIL import Image

import torch
import torchvision
import torchvision.transforms as transfroms

def donwload(urls, path):
    path.mkdir(parents=True, exist_ok=True)
    for url in urls:
        filepath = path / pathlib.Path(url).name
        if not filepath.exists():
            res = requests.get(url)
            if res.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(res.content)


def load(paths):
    print('load')
    x_path, y_path = paths
    with gzip.open(x_path) as fx, gzip.open(y_path) as fy:
        fx.read(4)
        fy.read(4)
        N, = struct.unpack('>i', fy.read(4))
        if N != struct.unpack('>i', fx.read(4))[0]:
            raise RuntimeError('wrong pair of MNIST images and labels')
        fx.read(8)

        images = np.empty((N, 784), dtype=np.uint8)
        labels = np.empty(N, dtype=np.uint8)

        for i in tqdm(range(N)):
            labels[i] = ord(fy.read(1))
            for j in range(784):
                images[i, j] = ord(fx.read(1))
    return images, labels


def make_images(path, images, labels):
    print('make image')
    path.mkdir(parents=True, exist_ok=True)
    for (i, image), label in tqdm(zip(enumerate(images), labels)):
        filepath = path / '{}_{}.jpg'.format(label, i)
        Image.fromarray(image.reshape(28, 28)).save(filepath)


def make_labellist(path, kind, labels):
    print('make label list')
    path.mkdir(parents=True, exist_ok=True)
    filepaths = [
        '{}_{}.jpg'.format(label, i) for i, label in enumerate(labels)
    ]
    df = pd.DataFrame({'name': filepaths, 'target': labels.tolist()})
    df.to_csv(path / '{}.csv'.format(kind), index=False, header=False)


def main():
    parser = argparse.ArgumentParser(
        description='Download and Convert MNIST binary files to image files')
    parser.add_argument('-p', '--path', type=pathlib.Path, default='./data')
    parser.add_argument('-o', '--out', choices=['npz', 'jpg'], default='jpg')
    args = parser.parse_args()

    def pipeline(kind):
        _kind = kind
        if kind == 'test':
            _kind = 't10k'

        # baseurl = 'http://yann.lecun.com/exdb/mnist'
        # urls = [
        #     '{}/{}-images-idx3-ubyte.gz'.format(baseurl, _kind),
        #     '{}/{}-labels-idx1-ubyte.gz'.format(baseurl, _kind)
        # ]
        # donwload(urls, args.path / 'raw')
        #

        # MNIST 데이터셋 로드
        train_set = torchvision.datasets.MNIST(
            root = './data/MNIST',
            train = True,
            download = True,
            transform = transfroms.Compose([
                transfroms.ToTensor() # 데이터를 0에서 255까지 있는 값을 0에서 1사이 값으로 변환
            ])
        )
        test_set = torchvision.datasets.MNIST(
            root = './data/MNIST',
            train = False,
            download = True,
            transform = transfroms.Compose([
                transfroms.ToTensor() # 데이터를 0에서 255까지 있는 값을 0에서 1사이 값으로 변환
            ])
        )

        paths = [
            args.path / 'MNIST' / 'raw' / '{}-images-idx3-ubyte.gz'.format(_kind),
            args.path / 'MNIST' / 'raw' / '{}-labels-idx1-ubyte.gz'.format(_kind)
        ]
        images, labels = load(paths)

        if args.out == 'jpg':
            path = args.path / 'processed'
            make_images(path / 'images' / kind, images, labels)
            make_labellist(path / 'labels', kind, labels)
        else:
            path = args.path / 'processed' / 'npz'
            path.mkdir(parents=True, exist_ok=True)
            np.savez_compressed(
                path / '{}.npz'.format(kind), x=images, y=labels)

    print('Processing train data ...')
    pipeline('train')

    print('Processing test data ...')
    pipeline('test')


if __name__ == '__main__':
    main()
 