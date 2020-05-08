# class for feature scaling



class FeaturesScaling:
    # A simple class
    # attribute
    name = "default"
    average = 0
    min = 0
    max = 0

    def __init__(self):
        pass

    def create_feature_scale(self, dataset):
        self.min = dataset[0][0]
        self.max = 0.0
        sum = 0
        for i in range(0, len(dataset)):
            for j in range(0,len(dataset[i])):
                if dataset[i][j] < self.min:
                    self.min = dataset[j]
                if dataset[i][j] > self.max:
                    self.max = dataset[i][j]
                sum += dataset[i][j]

        self.average = sum/ (len(dataset[0]) * len(dataset))

        for i in range(0,len(dataset)):
            for j in range(0, len(dataset[i])):
                dataset[i][j] = (dataset[i][j] - self.average) / (self.max - self.min)

        return dataset

    def apply(self,feature_vector):
        for i in range(0,len(feature_vector)):
            feature_vector[i] = (feature_vector[i] - self.average) / (self.max - self.min)

        return feature_vector
