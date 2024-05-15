import numpy as np

class MyLogReg:
    def __init__(self, max_iter=1000, learning_rate=0.01):
        self.max_iter = max_iter
        self.learning_rate = learning_rate
        self.weights = None
        self.bias = None

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for _ in range(self.max_iter):
            linear_model = np.dot(X, self.weights) + self.bias
            y_predicted = self.sigmoid(linear_model)

            dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
            db = (1 / n_samples) * np.sum(y_predicted - y)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_predicted = self.sigmoid(linear_model)
        y_predicted_cls = [1 if i > 0.5 else 0 for i in y_predicted]
        return y_predicted_cls

    def evaluate(self, X, y):
        y_predicted = self.predict(X)
        accuracy = np.mean(y_predicted == y)
        return accuracy
    
    # def confusion_matrix(self, y_true, y_pred):
    #     n_classes = len(np.unique(y_true))
    #     matrix = np.zeros((n_classes, n_classes))
    #     for i in range(len(y_true)):
    #         matrix[y_true[i], y_pred[i]] += 1
    #     return matrix
    
    # def classification_report(self, y_true, y_pred):
    #     n_classes = len(np.unique(y_true))
    #     matrix = np.zeros((n_classes, n_classes))
    #     for i in range(len(y_true)):
    #         matrix[y_true[i], y_pred[i]] += 1
    #     return matrix
    
    # def train_test_split(self, X, y, test_size=0.2, random_state=None):
    #     np.random.seed(random_state)
    #     n_samples = X.shape[0]
    #     test_size = int(n_samples * test_size)
    #     indices = np.random.permutation(n_samples)
    #     X = X[indices]
    #     y = y[indices]
    #     X_train, X_test = X[test_size:], X[:test_size]
    #     y_train, y_test = y[test_size:], y[:test_size]
    #     return X_train, X_test, y_train, y_test