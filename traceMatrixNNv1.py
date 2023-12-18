
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Embedding, Flatten, Dense, concatenate

# Given data
requirement_fields = ['Requirement ID', 'Type', 'Description']
test_fields = [
    'Test case ID',
    'Test Design Status',
    'Test Execution Run and Status',
    'Unit Tests',
    'Integration Tests',
    'System Tests',
    'User Acceptance Testing Status',
    'Defects, list',
    'Defect Status',
]
traceability_matrix = np.array([[1, 0, 1], [0, 1, 0], [1, 1, 1]])  # Binary matrix indicating connections

# Placeholder vectors (replace with your actual vectors or embeddings)
requirement_vectors_data = {
    'Requirement ID': np.array([0.2, 0.4, 0.6]),
    'Type': np.array([0.1, 0.3, 0.5]),
    'Description': np.array([0.7, 0.9, 0.2]),
}

test_case_vectors_data = {
    'Test case ID': np.array([0.8, 0.6, 0.4]),
    'Test Design Status': np.array([0.9, 0.2, 0.7]),
    'Test Execution Run and Status': np.array([0.5, 0.1, 0.3]),
    'Unit Tests': np.array([0.2, 0.7, 0.5]),
    'Integration Tests': np.array([0.4, 0.8, 0.6]),
    'System Tests': np.array([0.1, 0.9, 0.4]),
    'User Acceptance Testing Status': np.array([0.3, 0.6, 0.8]),
    'Defects, list': np.array([0.7, 0.2, 0.9]),
    'Defect Status': np.array([0.8, 0.5, 0.1]),
}

# Create vectors using given values
requirement_vectors = np.array([requirement_vectors_data[field] for field in requirement_fields])
test_case_vectors = np.array([test_case_vectors_data[field] for field in test_fields])

# Define separate input layers for requirements and test cases
requirement_input = Input(shape=(1,), name='requirement_input')
test_case_input = Input(shape=(1,), name='test_case_input')

# Embedding layers for requirements and test cases
embedding_layer = Embedding(input_dim=10, output_dim=5)  # Adjust output_dim based on your data

# Apply embedding to input layers
requirement_embedding = embedding_layer(requirement_input)
test_case_embedding = embedding_layer(test_case_input)

# Flatten the embeddings
requirement_flatten = Flatten()(requirement_embedding)
test_case_flatten = Flatten()(test_case_embedding)

# Concatenate the flattened embeddings
concatenated_embeddings = concatenate([requirement_flatten, test_case_flatten])

# Dense layers for the concatenated embeddings
output_layer = Dense(1, activation='sigmoid', name='output')(concatenated_embeddings)

# Create the model with two inputs and one output
model = Model(inputs=[requirement_input, test_case_input], outputs=output_layer)

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit([np.arange(len(requirement_fields)), np.arange(len(test_fields))], traceability_matrix.flatten(), epochs=10, validation_split=0.2)

# Evaluate the model (replace with your test set)
evaluation = model.evaluate([np.arange(len(test_fields)), np.arange(len(test_fields))], traceability_matrix.flatten())
print("Test Loss:", evaluation[0])
print("Test Accuracy:", evaluation[1])

# Use the trained model to make predictions (replace with your new data)
new_requirements = np.arange(len(test_fields))
new_test_cases = np.arange(len(test_fields))
predictions = model.predict([new_requirements, new_test_cases])

# Reshape predictions to match the shape of the original traceability matrix
predicted_matrix = predictions.reshape(traceability_matrix.shape)

print("Predicted Traceability Matrix:")
print(predicted_matrix)

