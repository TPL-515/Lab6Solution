from dagster import asset, get_dagster_logger, Output
from sklearn.metrics import accuracy_score
from lab6.models.randomforest import train, predict
from lab6.assets.dataingest import pull_data
import pandas as pd
import numpy as np

# Get our Logger
logger = get_dagster_logger()


@asset(description="This allows the user to train the static model that we will be using.")
def train_static(pull_data):
    print(pull_data)
    pull_data = pull_data.head(10)
    logger.info('begin training for the static model')
    labels = np.array(pull_data['label'])
    features = np.array(pull_data[['feature1', 'feature2']])
    train('rfmodel1', features, labels)

@asset(description="This allows the user to make a prediction using the static model")
def predict_static(pull_data):

    logger.info('making predictions on data')
    labels = np.array(pull_data['label'])
    features = np.array(pull_data[['feature1', 'feature2']])

    preds = predict('rfmodel1', features, labels)
    acc = accuracy_score(labels, preds)

    return acc

@asset(description="This allows a user to retrain the recurring model and update it")
def train_recurring(pull_data):
    
    logger.info('begin training for the recurring model')
    labels = np.array(pull_data['label'])
    features = np.array(pull_data[['feature1', 'feature2']])
    train('rfmodel2', features, labels)

@asset(description="This allows the user to make a prediction on the data using the constantly retraining model")
def predict_recurring(pull_data):

    logger.info('making predictions on data using recurring model')
    labels = np.array(pull_data['label'])
    features = np.array(pull_data[['feature1', 'feature2']])

    preds = predict('rfmodel2', features, labels)
    acc = accuracy_score(labels, preds)

    return acc

@asset(description="This allows the user to compare model results for our recurring versions.")
def compare_models(predict_static, predict_recurring, pull_data):
    
    logger.info('comparing models')
    return Output(None, metadata={"static_model_accuracy": predict_static, "recurring_model_accuracy": predict_recurring, "data_size": pull_data.shape[0]})