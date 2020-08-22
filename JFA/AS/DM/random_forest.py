
from sklearn.ensemble import RandomForestClassifier


class RandomForest:
    def makeModel(self,dataset):
        print('RandomForestClassifier makeModel')
        clf=RandomForestClassifier(n_estimators=200, max_depth=300,criterion ='entropy')
        self.model = clf

    def init(self):
        print('RandomForestClassifier makeModel')
        self.model = RandomForestClassifier(n_estimators=200, max_depth=300,criterion ='entropy')

    def makeModelFit(self,dataset):
         print('RandomForestClassifier makeModelFit')
         self.model=RandomForestClassifier(n_estimators=200, max_depth=300,criterion ='entropy')
         self.model.fit(dataset.data, dataset.target)  

    def predict(self,data):
        print('RandomForestClassifier predict')
        return self.model.predict(data)


