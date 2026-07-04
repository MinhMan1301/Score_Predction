#1 Import Libraries
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import (StandardScaler, OneHotEncoder, OrdinalEncoder )
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor

#2 Load datasets
df = pd.read_csv("../data/data.csv")

#3 EDA
# # stats = df.describe()
# # df.info()
# null_value = df.isnull()
# print(null_value)
# # print(stats)


#4 Visualization
outline_target = sn.histplot(data= df, x = "exam_score")
plt.title("Histogram of exam score")
plt.savefig("histogram.png")



#5 Split data
target = "exam_score"
x = df.drop(columns =[target,"student_id"])
y = df[target]
xtrain, xtest, ytrain, ytest = train_test_split(x,y,test_size = 0.2, random_state = 42)


#6 Encoding & Scaling & cleaning (Nominal and Ordinal included)
sleep_quality = ["poor","average","good"]
facility_rating = ["low","medium","high"]
exam_difficulty = ["easy","moderate","hard"]
all_categories = [sleep_quality,facility_rating,exam_difficulty]

ord_trans = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder",OrdinalEncoder(categories = all_categories)),
    ("scaler",StandardScaler())
])

nom_trans = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="constant",fill_value="missing")),
    ("onehot",OneHotEncoder(handle_unknown="ignore"))
])

num_trans = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler",StandardScaler())
])

#7 Train model

preprocessor = ColumnTransformer(transformers=[
    ("num",num_trans,["age","study_hours","class_attendance","sleep_hours"]),
    ("ordi",ord_trans,["sleep_quality","facility_rating","exam_difficulty"]),
    ("nom",nom_trans,["gender","course","internet_access","study_method"])
],remainder="passthrough")

reg = Pipeline(steps=[
    ("preprocessor",preprocessor),
    ("regressor",RandomForestRegressor(n_estimators=100,random_state=42)),
])
train = reg.fit(xtrain, ytrain)

#8 Test
score = reg.score(xtest, ytest)

#9 Predict
y_predict = reg.predict(xtest)

#10 Evaluation
#Comparision
for a,b in zip(y_predict, ytest):
    print("Predicted: {}, Actual: {}, Error: {} %".format(a,b,abs(((b-a)/a) * 100)))

