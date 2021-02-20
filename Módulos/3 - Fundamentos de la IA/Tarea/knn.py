import numpy as np
from collections import Counter

class Knn:
    def __init__(self, n_neighbors, metric='minkowski', p=2, weights='uniform'):
        self.n_neighbors = n_neighbors
        if metric in ["minkowski", "manhattan", "euclidean"]:
            self.metric = metric
        else:
            raise ValueError("Métrica inválida")
        self.p = p
        self.weights = weights

    def fit(self, X, y):
        if X.shape[0] == y.shape[0]:
            self.X = X
            self.y = y
        else:
            raise ValueError("Dimensión inválida")

    def _manhattan_distance(self, point):
        return np.sum(abs(self.X - point), axis=1)

    def _euclidean_distance(self, point):
        return np.sqrt(np.sum((self.X - point)**2, axis=1))

    def _minkowski_distance(self, point):
        return np.sum(abs(self.X - point)**self.p, axis=1)**(1/self.p)

    def _uniform_weights(self, distances):
        return np.array([(1, y) for d, y in np.ndenumerate(distances)])

    def _distance_weights(self, distances):
        return np.array([((1/y) if y else 1, y) for d, y in np.ndenumerate(distances)])
        # Opción más compacta sugerida por Miguel Camacho
        # return np.array([(1/(y or 1), y) for d, y in np.ndenumerate(distances)])


    def _predict_point(self, point):
        if self.metric == 'minkowski':
            distances = self._minkowski_distance(point)
        elif self.metric == 'manhattan':
            distances = self._manhattan_distance(point)
        elif self.metric == 'euclidean':
            distances = self._euclidean_distance(point)

        #distances = [self._euclidean_distance(self, point) for point in self.X]

        # Añadimos índices al array de distancias
        dict_weights = dict(enumerate(distances.flatten(), 0))

        # Ordenamos distancias en función del item[i] (distancias)
        sorted_dict = dict(sorted(dict_weights.items(), key=lambda item: item[1]))

        # Seleccionamos las posiciones de los n_neighbors con menor distancia
        keys = list(sorted_dict.keys())[0:self.n_neighbors]

        # Obtenemos las etiquetas dichas posiciones
        votes = np.take(self.y, keys)
        labels = np.unique(votes)

        # EVALUAMOS EL CONJUNTO DE ETIQUETAS
        # Si solo hay un candidato, lo seleccionamos directamente
        if len(labels) == 1:
            value = np.unique(labels)[0]
        else:
            # Pesos en función de la distancia
            if self.weights == 'distance':

                # Obtenemos los pesos de cada elemento
                weights = self._distance_weights(distances)
                # Creamos un array de zeros con dimensión igual a la etiqueta más alta encontrada
                counts = np.zeros(max(labels)+1)

                # Recorremos los índices y hacemos un sumatorio de los pesos
                for key in keys:
                    counts[int(self.y[[key]])] += weights[key][0]

                # Seleccionamos el índice del valor más alto
                value = np.argmax(counts)

            # Pesos uniformes
            else:
                # Hacemos un conteo sencillo (=1)
                value = Counter(votes).most_common(1)[0][0]

        return value

    def predict(self, x):

        nInputs = len(x)
        labels = np.zeros(nInputs)
        labels = [self._predict_point(point) for point in x]
        return labels



