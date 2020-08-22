import numpy as np
from Models.dataset import Dataset
from Models.dataset_resumed import DatasetResumed

def convertDatasetGPSResumed( datasetResumedList):
    data = []
    for entry in datasetResumedList:
        data.append( np.array([entry.lat,entry.lon]))
    return np.asarray(data).astype(np.float)

def convertDatasetResumed( datasetResumedList):
    data = []
    target = [] 
    for entry in datasetResumedList:
        data.append( [float(entry.sogAVG),float(entry.sogMax),float(entry.sogMin), entry.loc])
        target.append(entry.license)
    return Dataset(np.asarray(data),np.asarray(target), DatasetResumed.GetFeatureNames(), "DatasetResumed" )