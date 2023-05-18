from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from joblib import dump, load


def train(model_name, features, labels):
    
    rfmodel = RandomForestClassifier(n_estimators=10)
    rfmodel.fit(features, labels)
    dump(rfmodel, f'{model_name}')


def predict(model_name, features, labels):

    rfmodel = load(f'{model_name}')
    preds = rfmodel.predict(features)

    return preds
