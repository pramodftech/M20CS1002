import os
import pandas as pd
import numpy as np
import seaborn as sns
import pickle
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

'''
model.fit(X_train, Y_train)
# save the model to disk
filename = 'finalized_model.sav'
pickle.dump(model, open(filename, 'wb'))
'''
#forest = RandomForestClassifier(max_depth=5)
#tree = DecisionTreeClassifier(max_depth = 5)

# load the model from disk
def prediction(lst):
    #lst = [0,0,0,0,0,0,0,0,0,1,1,1,0,0,1,0]
    
    # Calling DataFrame constructor on list
    df = pd.DataFrame([lst])

    tree = pickle.load(open(os.path.join(BASE_DIR,'url/finalized_model.sav'), 'rb'))
    result = tree.predict(df)
    print("prediction = ",result)
    return result


