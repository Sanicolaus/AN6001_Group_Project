import numpy as np
import pandas as pd # data processing, CSV file I/O
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from scipy.stats import randint
# Preprocessing
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.datasets import make_classification
from sklearn.preprocessing import binarize, LabelEncoder, MinMaxScaler
# Parameter Adjustment
from sklearn.model_selection import RandomizedSearchCV,cross_val_score
# Models
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, ExtraTreesClassifier
from keras.models import Sequential
from keras.layers import Dense, Dropout
from catboost import CatBoostClassifier
# Metrics
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import plot_confusion_matrix

#Mental Health Issue
mental=pd.read_csv(r"C:\Users\sycwd\Desktop\NTU\survey(1).csv")
# drop the irrelevant data for our model building
mental = mental.drop(['comments'], axis= 1)
mental = mental.drop(['state'], axis= 1)
mental = mental.drop(['Timestamp'], axis= 1)
mental = mental.drop(['Country'], axis= 1)
#Unify missing values
for feature in mental:
    if feature=='self_employed':
        mental[feature] = mental[feature].fillna('NaN')
    elif feature=='work_interfere':
        mental[feature] = mental[feature].fillna('NaN')

# clean column 'Gender'
mental['Gender']=mental['Gender'].str.lower()
#Select unique elements
gender = mental['Gender'].unique()

# made gender groups
male_str = ["male", "m", "male-ish", "maile", "mal", "male (cis)", "make", "male ", "man",
            "msle", "mail", "malr","cis man", "Cis Male", "cis male"]
trans_str = ["trans-female", "something kinda male?", "queer/she/they", "non-binary","nah",
             "all", "enby", "fluid", "genderqueer", "androgyne", "agender", "male leaning androgynous",
             "guy (-ish) ^_^", "trans woman", "neuter", "female (trans)", "queer",
             "ostensibly male, unsure what that really means"]
female_str = ["cis female", "f", "female", "woman",  "femake", "female ","cis-female/femme", "female (cis)", "femail"]

for (row, col) in mental.iterrows(): #row is the index, col is all the columns corresponding to that row

    if col.Gender in male_str:
        mental['Gender'].replace(to_replace=col.Gender, value='male', inplace=True)

    if col.Gender in female_str:
        mental['Gender'].replace(to_replace=col.Gender, value='female', inplace=True)

    if col.Gender in trans_str:
        mental['Gender'].replace(to_replace=col.Gender, value='trans', inplace=True)

# remove the useless values in 'Gender'
useless_list = ['a little about you', 'p']
mental = mental[~mental['Gender'].isin(useless_list)]

# clean column 'self_employed'
mental['self_employed'] = mental['self_employed'].replace('NaN', 'No')
# clean column 'work_interfere'
mental['work_interfere'] = mental['work_interfere'].replace('NaN', 'Don\'t know' )
for feature in mental:
    le = preprocessing.LabelEncoder()
    le.fit(mental[feature])
    mental[feature]=le.transform(mental[feature])
# the only variable we need to scale is Age
scaler = MinMaxScaler()
mental['Age'] = scaler.fit_transform(mental[['Age']])
mental.head()
# define X and y
feature_cols = ['Age', 'Gender', 'work_interfere', 'family_history', 'care_options','benefits', 'anonymity', 'leave']
mental_X = mental[feature_cols]
mental_y = mental.treatment

# split X and y into training and testing sets
mental_X_train, mental_X_test, mental_y_train, mental_y_test = train_test_split(mental_X, mental_y,
                                                                                test_size=0.30, random_state=0)

# model building
mental_RandomForest = RandomForestClassifier(max_depth=3, min_samples_split=8,
                                             min_samples_leaf=7,n_estimators = 20, random_state = 1)
mental_RandomForest.fit(mental_X_train, mental_y_train)

#Flu Detection
flu_community=pd.read_csv(r"C:\Users\sycwd\Desktop\NTU\Flu\clean_data(community).csv")
# split into input (X) and output (Y) variables
flu_community_X = flu_community.iloc[:,0:11]
flu_community_Y = flu_community.iloc[:,12]
# get the X and Y trainset,testset
flu_community_X_train, flu_community_X_test, flu_community_Y_train, flu_community_Y_test = train_test_split(
    flu_community_X, flu_community_Y, test_size=0.30, random_state=2020)
flu_community_model = RandomForestClassifier(n_estimators=40, max_depth=4, max_leaf_nodes=30,n_jobs=-1)
flu_community_model.fit(flu_community_X_train, flu_community_Y_train)

flu_professional=pd.read_csv(r"C:\Users\sycwd\Desktop\NTU\Flu\clean_data(professional).csv")
# split into input (X) and output (Y) variables
flu_professional_X = flu_professional.iloc[:,[0,1,2,3,4,5,6,7,8,9,10,12,13,14,15]]
flu_professional_Y = flu_professional.iloc[:,16]
# get the X and Y trainset,testset
flu_professional_X_train, flu_professional_X_test, flu_professional_Y_train, flu_professional_Y_test = train_test_split(
    flu_professional_X, flu_professional_Y, test_size=0.30, random_state=2020)
flu_professional_model = RandomForestClassifier(n_estimators=40, max_depth=4, max_leaf_nodes=30,n_jobs=-1)
flu_professional_model.fit(flu_professional_X_train, flu_professional_Y_train)

#Heart Disease
heart_raw_df = pd.read_csv(r"C:\Users\sycwd\Downloads\heart.csv")
from random import seed
seed(2020)
heart_prof_df = heart_raw_df.copy()
heart_family_df = heart_prof_df[['age', 'sex', 'cp', 'trestbps', 'thalach', 'exang', 'thal', 'target']]
heart_prof_encode_columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
#Catboost on dataset
heart_prof_y = heart_prof_df['target']
heart_prof_X = heart_prof_df[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak',
                              'slope', 'ca', 'thal']]
heart_prof_train_X, heart_prof_test_X, heart_prof_train_y, heart_prof_test_y = \
    train_test_split(heart_prof_X,heart_prof_y,test_size=0.1)
heart_prof_clf = CatBoostClassifier(iterations=150, depth=10,cat_features=heart_prof_encode_columns,learning_rate=0.05,
                                    loss_function='Logloss',auto_class_weights="Balanced",random_state=2020)
heart_prof_clf.fit(heart_prof_train_X, heart_prof_train_y)

heart_family_y = heart_prof_df['target']
heart_family_X = heart_prof_df[['age', 'sex', 'cp', 'trestbps', 'thalach', 'exang', 'thal']]
heart_family_encode_columns = ['sex', 'cp', 'exang', 'thal']
heart_family_train_X, heart_family_test_X, heart_family_train_y, heart_family_test_y = \
    train_test_split(heart_family_X,heart_family_y,test_size=0.1)
heart_family_clf = CatBoostClassifier(iterations=300, depth=10,cat_features=heart_family_encode_columns,
                                      learning_rate=0.05, loss_function='Logloss',auto_class_weights="Balanced")
heart_family_clf.fit(heart_family_train_X, heart_family_train_y)

#Save model to directory
joblib.dump(mental_RandomForest, 'C:/Users/sycwd/Desktop/NTU/save_model/mental_model.pkl')
joblib.dump(flu_community_model, 'C:/Users/sycwd/Desktop/NTU/save_model/flu_community.pkl')
joblib.dump(flu_professional_model, 'C:/Users/sycwd/Desktop/NTU/save_model/flu_professional.pkl')
heart_family_clf.save_model('C:/Users/sycwd/Desktop/NTU/save_model/heart_family_clf',format="cbm")
heart_prof_clf.save_model('C:/Users/sycwd/Desktop/NTU/save_model/heart_professional_clf',format="cbm")