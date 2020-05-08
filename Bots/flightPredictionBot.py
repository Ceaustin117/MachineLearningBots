from SupervisedLearning import LinearRegression
from Utilities import FeaturesScaling, FileHandler
import math
# Driver code
# Object instantiation


class FlightPredictionBot:
    # A simple class
    # attribute
    name = "default"
    feature_scaler = FeaturesScaling.FeaturesScaling()
    file_handler = FileHandler.FileHandler()
    # the theta vector used here was output of a train process
    theta_vector = [1.004579, 5.286822]
    target_function_dictionary = {}

    def __init__(self, name=""):
        self.name = name

    def add_to_target_function_dictionary(self, target_function_name):
        if "LinearRegression" in target_function_name:
            self.target_function_dictionary[target_function_name] = LinearRegression.LinearRegressionFunction(self.theta_vector)

    # A sample method
    def fun(self):
        print("I'm a", self.name)

    def print_linear_regression(self):
        print("Linear Regression Prediction:", self.target_function_dictionary["LinearRegression"].apply([1, 2, 3]))

    def cost(self,target_function, dataset, labels):
        m = len(dataset)
        sum_squared_errors = 0.0
        # calculate the squared error ("difference") for each training example and add it to the total sum
        for x in range(0, len(m)):
            feature_vector = dataset[x]
            # predict the value and computer the error based on the real value (label)
            predicted = target_function.apply(feature_vector)
            label = labels[x]
            gap = predicted - label
            sum_squared_errors += math.pow(gap,2)
        #calculate and return the mean value of the errors ( the smaller the better)
        return (1.0/(2*m)) * sum_squared_errors

    def  train(self,target_function,dataset,labels,alpha):
        m = len(dataset)
        theta_vector = target_function.get_thetas()
        newThetaVector = [None] * len(theta_vector)
        #compute the new theta of each element of the theta array
        for x in range(0,len(theta_vector)):
            # summarize the error gap * feature
            sumErrors = 0
            for i in range(0,m):
                featureVector = dataset[i]
                error = target_function.apply(featureVector) - labels[i]
                sumErrors += error * featureVector[x]
        # compute the new theta value
            gradient = (1.0 / m) * sumErrors
            newThetaVector[x] = theta_vector[x] - (alpha * gradient)
        return LinearRegression.LinearRegressionFunction(newThetaVector)


    def run_linear_regression(self, dataset,labels,initial_thetas,learning_rate):

        # scale the extended feature list
        scaled_dataset = self.feature_scaler.create_feature_scale(dataset)

        # create hypothesis function with initial thetas and train it with learning rate 0.1
        targetFunction =  LinearRegression.LinearRegressionFunction(initial_thetas);
        for i in range(0,10000):
            targetFunction = self.train(targetFunction, scaled_dataset, labels, learning_rate)


        # make a prediction of a house with size if 600 m2
        new_vec = [1.0, 600.0, 360000.0]
        scaledFeatureVector = self.feature_scaler.apply(new_vec);
        predicted_price = targetFunction.apply(scaledFeatureVector);
        self.file_handler.print_file()
        print(predicted_price)
