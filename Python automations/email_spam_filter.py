# Hypothetical Data Generation
import numpy as np
import pandas as pd

# Random seed for reproducibility
np.random.seed(42)

# Generating synthetic data: 0 = Not Spam, 1 = Spam
emails = pd.DataFrame({
    'word_count': np.random.poisson(100, 1000) + (np.random.binomial(1, 0.5, 1000) * 100),  # Spam emails might be longer
    'contains_link': np.random.binomial(1, 0.3, 1000),  # 30% chance of containing a link
    'contains_spam_words': np.random.binomial(1, 0.4, 1000),  # 40% chance of containing spam words
    'is_spam': np.random.binomial(1, 0.5, 1000)  # 50% are spam
})

# Display the first few rows
print(emails.head())


from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Features and target variable
X = emails.drop('is_spam', axis=1)
y = emails['is_spam']

# Splitting the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Training the model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Making predictions
predictions = model.predict(X_test)

# Evaluating the model
print("Accuracy:", accuracy_score(y_test, predictions))
