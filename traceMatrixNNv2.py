import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Flatten, Dense

# Given data
N = 3  # Number of requirements
M = 3  # Number of test cases
traceability_matrix = np.array([[1, 0, 1], [0, 1, 0], [1, 1, 1]])  # Binary matrix indicating connections

# Placeholder vectors for requirements and test cases
requirement_vectors_data = np.random.rand(N, 10)  # Replace with actual vectors
test_case_vectors_data = np.random.rand(M, 10)  # Replace with actual vectors

# Create a tf.data.Dataset
def create_dataset():
    dataset = tf.data.Dataset.from_tensor_slices((
        {
            'requirement_input_input': np.tile(np.arange(N), M),
            'test_case_input_input': np.repeat(np.arange(M), N),
        },
        traceability_matrix.flatten()
    ))
    return dataset.shuffle(buffer_size=len(traceability_matrix)).batch(1)

# Build a simple neural network model
model = Sequential()
model.add(Embedding(input_dim=max(N, M), output_dim=5, input_length=1, name='requirement_input'))
model.add(Flatten())
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Create the dataset
dataset = create_dataset()

# Train the model
model.fit(dataset, epochs=10, steps_per_epoch=len(traceability_matrix))

# Evaluate the model
evaluation = model.evaluate(dataset, steps=len(traceability_matrix))

print("Test Loss:", evaluation[0])
print("Test Accuracy:", evaluation[1])

