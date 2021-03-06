from Bots import flightPredictionBot
from Utilities import FeaturesScaling

flight_prediction_bot = flightPredictionBot.FlightPredictionBot("Flight Prediction Bot")


def main():
    print("python main function")
    flight_prediction_bot.add_to_target_function_dictionary("LinearRegression")
    #create the dataset
    dataset = []

    dataset.append([1.0,  90.0,  8100.0 ])   #feature vector of house#1
    dataset.append([1.0, 101.0, 10201.0 ])   # feature vector of house#2
    dataset.append([1.0, 103.0, 10609.0 ])   #

    # create the labels
    labels = []
    labels.append(249.0)        # price label of house#1
    labels.append(338.0)        # price label of house#2
    labels.append(304.0)        # ...

    flight_prediction_bot.run_linear_regression(dataset,labels,[1.0, 1.0, 1.0],0.1)
    flight_prediction_bot.fun()
    flight_prediction_bot.print_linear_regression()


if __name__ == '__main__':
    main()
