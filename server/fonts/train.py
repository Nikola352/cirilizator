from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Assume you have features and labels for Latin and Cyrillic fonts
latin_features, latin_labels = load_latin_data()  # Replace with your function to load Latin data
cyrillic_features, cyrillic_labels = load_cyrillic_data()  # Replace with your function to load Cyrillic data

# Split the data into training and testing sets
latin_features_train, latin_features_test, latin_labels_train, latin_labels_test = train_test_split(
    latin_features, latin_labels, test_size=0.2, random_state=42
)

# Train a model on Latin data
latin_model = RandomForestClassifier()
latin_model.fit(latin_features_train, latin_labels_train)

# Evaluate the model on Latin data
latin_predictions = latin_model.predict(latin_features_test)
latin_accuracy = accuracy_score(latin_labels_test, latin_predictions)
print(f"Accuracy on Latin data: {latin_accuracy:.2f}")

# Fine-tune the model on Cyrillic data
cyrillic_features_train, cyrillic_features_test, cyrillic_labels_train, cyrillic_labels_test = train_test_split(
    cyrillic_features, cyrillic_labels, test_size=0.2, random_state=42
)

# Use the pre-trained Latin model for initialization
cyrillic_model = RandomForestClassifier()
cyrillic_model.set_params(**latin_model.get_params())
cyrillic_model.fit(cyrillic_features_train, cyrillic_labels_train)

# Evaluate the model on Cyrillic data
cyrillic_predictions = cyrillic_model.predict(cyrillic_features_test)
cyrillic_accuracy = accuracy_score(cyrillic_labels_test, cyrillic_predictions)
print(f"Accuracy on Cyrillic data: {cyrillic_accuracy:.2f}")
