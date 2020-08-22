from sklearn.cluster import KMeans
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
from pandas import DataFrame
from AS.converter import *

from json import JSONEncoder
import json
import base64

class K_Means:
    def makeModel(self,dataset):
        #print(type(dataset))
        #print(MovementEncoder().encode(dataset[0]))
        kmeans = KMeans(n_clusters=4, random_state=0).fit(dataset)
        self.model = kmeans

    def predict(self, input):
        #return self.model.predict(input.reshape(-1,1))

        #data = [ DatasetResumed(input[0],input[1])]
        #data2 = convertDatasetGPSResumed(data)
        #print(MovementEncoder().encode(input))
        return self.model.predict([input])

    def predict2(self, data):
        data2 = convertDatasetGPSResumed(data)
        predicted = self.model.predict(data2)    
        for x in range(0, len(data)):
            data[x].setLoc(predicted[x])
        return data

class MyEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__    

class MovementEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            if obj.flags['C_CONTIGUOUS']:
                obj_data = obj.data
            else:
                cont_obj = np.ascontiguousarray(obj)
                assert(cont_obj.flags['C_CONTIGUOUS'])
                obj_data = cont_obj.data
            ## data_b64 = base64.b64encode(obj_data)
            ## converting to base64 and returning a dictionary did not work
            ## return dict(__ndarray__ = data_b64, dtype = str(obj.dtype), shape = obj.shape)
            return obj.tolist()  ## instead, utilize numpy builtin tolist() method
        try:
            my_dict = obj.__dict__   ## <-- ERROR raised here
        except TypeError:
            pass
        else:
            return my_dict
        return json.JSONEncoder.default(self, obj)