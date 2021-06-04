import tensorflow as tf
import pandas as pd
import numpy as np
from keras_preprocessing.image import ImageDataGenerator

from tensorflow.keras.layers import Dense, Flatten, Conv2D
from tensorflow.keras import Model


# tf.keras.preprocessing.image_dataset_from_directory(
#     directory,
#     labels="inferred",
#     label_mode="int",
#     class_names=None,
#     color_mode="rgb",
#     batch_size=32,
#     image_size=(256, 256),
#     shuffle=True,
#     seed=None,
#     validation_split=None,
#     subset=None,
#     interpolation="bilinear",
#     follow_links=False,
#     smart_resize=False,
# )

def main():
    # Make numpy printouts easier to read.
    np.set_printoptions(precision=3, suppress=True)

    # https://archive.ics.uci.edu/ml/datasets/Auto+MPG
    url_train = r'F:\MOIN\hack_vertebra\Kiel-AI-Coding.Waterkant21.body-fractures-main\data\train\data.csv'
    url_validation = r'F:\MOIN\hack_vertebra\Kiel-AI-Coding.Waterkant21.body-fractures-main\data\val\data.csv'
    url_test = r'F:\MOIN\hack_vertebra\Kiel-AI-Coding.Waterkant21.body-fractures-main\data\test\data.csv'
    # column_names = ['img', 'grade']

    dataset_train = pd.read_csv(url_train, na_values='?',
                                comment='\t', sep=',', skipinitialspace=True, header=0)
    dataset_validation = pd.read_csv(url_validation, na_values='?',
                                     comment='\t', sep=',', skipinitialspace=True, header=0)
    dataset_test = pd.read_csv(url_test, na_values='?',
                               comment='\t', sep=',', skipinitialspace=True, header=0)

    dataset_train.tail()

    # print(dataset_train)

    datagen = ImageDataGenerator(rescale=1. / 65536.)
    test_datagen = ImageDataGenerator(rescale=1. / 65536.)

    train_generator = datagen.flow_from_dataframe(
        dataframe=dataset_train,
        directory=url_train,
        x_col="img",
        y_col="grade",
        batch_size=32,
        seed=42,
        shuffle=True,
        class_mode="raw",
        target_size=(32, 32))

    valid_generator = datagen.flow_from_dataframe(
        dataframe=dataset_validation,
        directory=url_validation,
        x_col="img",
        y_col="grade",
        batch_size=32,
        seed=42,
        shuffle=True,
        class_mode="raw",
        target_size=(32, 32))

    test_generator = test_datagen.flow_from_dataframe(
        dataframe=dataset_test,
        directory=url_test,
        x_col="img",
        y_col=None,
        batch_size=32,
        seed=42,
        shuffle=False,
        class_mode=None,
        target_size=(32, 32))

    # todo: clean data???
    # dataset = dataset_train.dropna()


if __name__ == '__main__':
    main()
    pass
