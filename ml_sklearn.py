from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

acc = modelo.score(X_test, y_test)
print(f"Acurácia do modelo RandomForest: {acc:.2f}")