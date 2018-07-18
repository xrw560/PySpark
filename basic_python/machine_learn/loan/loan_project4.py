import pandas as pd

loans = pd.read_csv("cleaned_loans2007.csv")
# print(loans.info())

"""逻辑回归(二分类)"""
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
cols = loans.columns
train_cols = cols.drop("loan_status")
features = loans[train_cols]
target = loans["loan_status"]
lr.fit(features, target)
predictions = lr.predict(features)

from sklearn.cross_validation import cross_val_predict, KFold
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators=10, class_weight="balanced", random_state=1)
# print help(RandomForestClassifier)
kf = KFold(features.shape[0], random_state=1)
predictions = cross_val_predict(rf, features, target, cv=kf)
predictions = pd.Series(predictions)

# False positives.
fp_filter = (predictions == 1) & (loans["loan_status"] == 0)
fp = len(predictions[fp_filter])

# True positives.
tp_filter = (predictions == 1) & (loans["loan_status"] == 1)
tp = len(predictions[tp_filter])

# False negatives.
fn_filter = (predictions == 0) & (loans["loan_status"] == 1)
fn = len(predictions[fn_filter])

# True negatives
tn_filter = (predictions == 0) & (loans["loan_status"] == 0)
tn = len(predictions[tn_filter])

# Rates
tpr = tp / float((tp + fn))
fpr = fp / float((fp + tn))

print(tpr)
print(fpr)
