# Python program to
# demonstrate instantiating
# a class


class LinearRegressionFunction:
    theta_vector = []

    def __init__(self, theta_vector = []):
        self.theta_vector = theta_vector

    def apply(self,feature_vector):
            feature_vector[0] = 1.0
            # sequential implementation
            prediction = 0
            for j in range(0, len(self.theta_vector)):
                prediction += self.theta_vector[j] * feature_vector[j]

            return prediction

    def get_thetas(self):
        return self.theta_vector
