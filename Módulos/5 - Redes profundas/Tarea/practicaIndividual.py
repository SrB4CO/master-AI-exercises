import numpy as np
import random

class PerceptronSimple():
    def __init__(self,activation, learning_rate=0.1):

        # Inicialización de pesos aleatorios con valores entre -1 y 1
        self.weights = 2 * np.random.random((3, 1)) - 1
        self.activation = activation
        self.learning_rate = learning_rate

    # FUNCIONES DE ACTIVACIÓN
    def escalon(self,x):
        return 1 * (x > 0.5)
        
    def sigmoide(self,x):
        # return 1 / (1 + np.exp(-x))
        return 1 / (1 + np.e ** (-x))

    def derivadaSigmoide(self,x):
        return self.sigmoide(x) * (1 - self.sigmoide(x))
        #return x * (1 - x)

    def elu(self, x):
        return x if (x > 0) else learning_rate * (np.exp(-x) - 1)

    def derivadaElu(self, x):
        return 1 if (x > 0) else learning_rate * np.exp(-x)

    def relu(self,x):
        return np.maximum(x,0)

    def derivadaRelu(self, x):
        return 1 * (self.relu(x) > 0)

    def leakyRelu(self,x):
        return x if x > 0 else 0.01 * x

    def derivadaLeakyRelu(self, x):
        return 1 if (x > 0) else 0.01

    def tanh(self, x):
        return (np.exp(x) - np.exp(-x)) / (np.exp(x) + np.exp(-x))

    def derivadaTanh(self, x):
        return 1 - self.tanh(x)**2

    # FUNCIÓN DE COSTE
    # Error cuadrático medio - mean squared error (MSE)
    def MSE(self, y, output):
        return np.mean((y - output) ** 2)

    def derivadaMSE(self, y, output):
        return y - output


    # PASO DE LA RED HACIA DELANTE
    def forwardPass(self,X):
        result = np.dot(X, self.weights)
        activation = self.activation
        if activation == "escalon":
            output = self.escalon(result)
        elif activation == "sigmoide":
            output = self.sigmoide(result)
        elif activation == "elu":
            output = self.elu(result)
        elif activation == "relu":
            output = self.relu(result)
        elif activation == "leakyrelu":
            output = self.leakyRelu(result)
        elif activation == "tanh":
            output = self.tanh(result)
        return output

    # ENTRENAMIENTO
    def fit(self,X_train,y_train,n_epochs):

        activation = self.activation

        for epoch in range(n_epochs):
            for x,y in zip(X_train,y_train): # Para cada ejemplo de entrenamiento...
                output = self.forwardPass([x])
                error = self.derivadaMSE(y, output)

                if activation == "escalon":
                    # Siguiendo el ejemplo del manual de clase
                    if error == 1:
                        self.weights = (self.weights.T + x).T
                    elif error == -1:
                        self.weights = (self.weights.T - x).T

                    # si no hay error, no reajustamos pesos

                elif activation == "sigmoide":
                    # En este caso se utiliza la actualización proporcionada en la plantilla
                    ajuste = x * np.array(error * self.derivadaSigmoide(output)[0])
                    self.weights += ajuste.T

                elif activation == "elu":
                    ajuste = x * np.array(error * self.derivadaElu(output))
                    self.weights += ajuste.T * learning_rate

                elif activation == "relu":
                    ajuste = x * np.array(error * self.derivadaRelu(output))
                    self.weights += ajuste.T * learning_rate

                elif activation == "leakyrelu":
                    ajuste = x * np.array(error * self.derivadaLeakyRelu(output))
                    self.weights += ajuste.T * learning_rate

                elif activation == "tanh":
                    ajuste = x * np.array(error * self.derivadaTanh(output))
                    self.weights += ajuste.T * learning_rate

    # PREDICCIÓN
    def predict(self,X_new):
        predictions = [self.forwardPass(X) for X in X_new]
        return np.array(predictions)


if __name__ == "__main__":

    learning_rate = 0.01
    perceptronEscalon = PerceptronSimple("escalon")
    perceptronSigmoidal = PerceptronSimple("sigmoide")
    perceptronELU = PerceptronSimple("elu", learning_rate)
    perceptronReLU = PerceptronSimple("relu",learning_rate)
    perceptronLeakyReLU = PerceptronSimple("leakyrelu",learning_rate)
    perceptronTanh = PerceptronSimple("tanh",learning_rate)


    print("Perc. Escalon inicializado con: ")
    print(perceptronEscalon.weights)
    print("Perc. Sigmoidal inicializado con: ")
    print(perceptronSigmoidal.weights)
    print("Perc. ELU inicializado con: ")
    print(perceptronELU.weights)
    print("Perc. ReLU inicializado con: ")
    print(perceptronReLU.weights)
    print("Perc. LeakyReLU inicializado con: ")
    print(perceptronLeakyReLU.weights)
    print("Perc. Tanh inicializado con: ")
    print(perceptronTanh.weights)


    X_train = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    y_train = np.array([[0, 1, 1, 0]]).T
    
    n_epochs = 1000

    perceptronEscalon.fit(X_train,y_train,n_epochs)
    perceptronSigmoidal.fit(X_train,y_train,n_epochs)
    perceptronELU.fit(X_train,y_train,n_epochs)
    perceptronReLU.fit(X_train,y_train,n_epochs)
    perceptronLeakyReLU.fit(X_train,y_train,n_epochs)
    perceptronTanh.fit(X_train,y_train,n_epochs)

    X_test = np.array([[1,0,0], [0,0,1]])

    print("Perc. Escalon entrenado: ")
    print(perceptronEscalon.weights)
    print("Perc. Sigmoidal entrenado: ")
    print(perceptronSigmoidal.weights)
    print("Perc. ReLU entrenado: ")
    print(perceptronReLU.weights)
    print("Perc. LeakyReLU entrenado: ")
    print(perceptronLeakyReLU.weights)
    print("Perc. Tanh entrenado: ")
    print(perceptronTanh.weights)

    pred_escalon = perceptronEscalon.predict(X_test)
    print("\nPred escalon: ")
    print(pred_escalon)

    pred_sigmoide = perceptronSigmoidal.predict(X_test)
    print("\nPred sigmoide: ")
    print(pred_sigmoide)

    pred_elu = perceptronELU.predict(X_test)
    print("\nPred ELU: ")
    print(pred_elu)

    pred_relu = perceptronReLU.predict(X_test)
    print("\nPred ReLU: ")
    print(pred_relu)

    pred_leakyrelu = perceptronLeakyReLU.predict(X_test)
    print("\nPred LeakyReLU: ")
    print(pred_leakyrelu)

    pred_tanh = perceptronTanh.predict(X_test)
    print("\nPred Tanh: ")
    print(pred_tanh)