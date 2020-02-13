import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

file = pd.read_csv('wine_dataset.csv')

file['style'] = file['style'].replace('red', 0)
file['style'] = file['style'].replace('white', 0)

y = file['style']  # my target is predict the type of wine
# i'm excluding style column from dataset cause i want to predict the style
x = file.drop('style', axis=1)

# creating sets - training set and test set

# 30% percent of my dataset is for test and 70% to train the model
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

model = ExtraTreesClassifier()  # decision tree
model.fit(x_train, y_train)

result = model.score(x_test, y_test)  # comparing predicted with the real data
print("Accuracy", result)
