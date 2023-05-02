from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.calibration import CalibratedClassifierCV
from imblearn.over_sampling import RandomOverSampler

# Load the data
X, y = load_data()

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Upsample the minority class using RandomOverSampler from imbalanced-learn
oversampler = RandomOverSampler(random_state=42)
X_train_resampled, y_train_resampled = oversampler.fit_resample(X_train, y_train)

# Train a logistic regression classifier on the resampled data
classifier = LogisticRegression(random_state=42)
classifier.fit(X_train_resampled, y_train_resampled)

# Evaluate the classifier on the test data
y_pred = classifier.predict(X_test)
print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

# Calibrate the classifier using CalibratedClassifierCV
calibrated_classifier = CalibratedClassifierCV(classifier, cv=5, method='sigmoid')
calibrated_classifier.fit(X_train_resampled, y_train_resampled)

# Evaluate the calibrated classifier on the test data
y_pred_calibrated = calibrated_classifier.predict(X_test)
print(classification_report(y_test, y_pred_calibrated))
print(confusion_matrix(y_test, y_pred_calibrated))
