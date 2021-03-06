from random_survival_forest import RandomSurvivalForest, concordance_index
from lifelines import datasets
from sklearn.model_selection import train_test_split
import time

rossi = datasets.load_rossi()
# Attention: duration column must be index 0, event column index 1 in y
y = rossi.loc[:, ["arrest", "week"]]
X = rossi.drop(["arrest", "week"], axis=1)
X, X_test, y, y_test = train_test_split(X, y, test_size=0.25, random_state=10)

print("RSF")
start_time = time.time()
rsf = RandomSurvivalForest(n_estimators=20, n_jobs=-1, min_leaf=10)
rsf = rsf.fit(X, y)
print("--- %s seconds ---" % (time.time() - start_time))
y_pred = rsf.predict(X_test)
c_val = concordance_index(y_time=y_test["week"], y_pred=y_pred, y_event=y_test["arrest"])
print("C-index", round(c_val, 3))
