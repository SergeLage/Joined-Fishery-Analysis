from DAL.vms_recordsDAL import VMSRecordsDAL
from AS.converter import *
from AS.DM.k_means import K_Means
from AS.DM.random_forest import RandomForest
from Models.vms_resumed import VMSResumed

class Classifier:
    _model = None
    _kMeans = None

    @staticmethod
    def start():
        print('Start Classifier')
        dataset_resumed = Classifier.ImportData()
        newDataset2 = convertDatasetResumed(dataset_resumed) 
        Classifier._model = RandomForest()
        Classifier._model.makeModelFit(newDataset2) 
        print ('Classifier ok')


        #dataResumed = VMSResumed(1,5,5,5,-1)
        #cPred = Classifier.predict(dataResumed,0.555,35.0)
        #print(cPred)

    @staticmethod
    def predict( data, lat, lon):
        print('predict')
        loc_arr = np.array([lat,lon]).astype(np.float)
        data.loc = Classifier._kMeans.predict(loc_arr)
        pLicense = Classifier._model.predict([[float(data.sogAvg), float(data.sogMax), float(data.sogMin), data.loc]])
        return pLicense

    @staticmethod
    def ImportData():
        dal = VMSRecordsDAL()
        dataset_filtred = dal.selectFiltred(-1)
        dataset_resumed = dal.selectResumed(-1)
        print ('Dataset len {0}'.format(len(dataset_resumed)))
        newDatasetLoc = convertDatasetGPSResumed(dataset_filtred)
        Classifier._kMeans = K_Means()
        Classifier._kMeans.makeModel(newDatasetLoc)
        dataset_resumed = Classifier._kMeans.predict2(dataset_resumed)
        return dataset_resumed