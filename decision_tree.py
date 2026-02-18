from sklearn.tree import DecisionTreeClassifier

# Taking input dataset
n = int(input("Enter number of training samples: "))

X = []
Y = []

print("Enter features and class label:")

for _ in range(n):
    f1, f2, label = input("Enter feature1 feature2 class: ").split()
    X.append([int(f1), int(f2)])
    Y.append(label)

# Train model
model = DecisionTreeClassifier()
model.fit(X, Y)

# Prediction input
f1 = int(input("Enter feature1 for prediction: "))
f2 = int(input("Enter feature2 for prediction: "))

prediction = model.predict([[f1, f2]])

print("Predicted Class:", prediction[0])
