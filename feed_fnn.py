from sklearn.neural_network import MLPClassifier

# Input training data
n = int(input("Enter number of training samples: "))

X = []
Y = []

print("Enter feature1 feature2 class (example: 1 1 Yes)")

for _ in range(n):
    while True:
        data = input("Enter data: ").split()
        if len(data) == 3:
            f1, f2, label = data
            X.append([int(f1), int(f2)])
            Y.append(label)
            break
        else:
            print("Please enter exactly 3 values!")

# Train neural network
model = MLPClassifier(hidden_layer_sizes=(3,), max_iter=1000)
model.fit(X, Y)

# Prediction
f1 = int(input("Enter feature1 for prediction: "))
f2 = int(input("Enter feature2 for prediction: "))

prediction = model.predict([[f1, f2]])

print("Predicted Class:", prediction[0])
