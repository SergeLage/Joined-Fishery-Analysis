from DAL.vms_recordsDAL import VMSRecordsDAL
from AS.classifier import Classifier
from DAL.vms_vesselsDAL import VMSVesselsDAL
from Models.vms_resumed import VMSResumed

class PreProcessCore:
    licenseDic = {
        "Armadilhas / De abrigo / Alcatruzes" : 0,
        "Arrasto / De fundo de portas" : 1,
        "Arrasto / De fundo de portas / Crustáceos (2002-2017)":2,
        "Arrasto / Pelágico / Com portas (2008-2017)":3,
        "Cerco / para bordo / Tipo americano" : 4,
        "Emalhar de 1 pano / De deriva / Grandes Pelágicos (1993-2017)":5,
        "Arrasto / De fundo de portas (1993-2017)":6,
        "Pesca à linha / Cana e linha de mão (2014 - 2017)":7,
        "Emalhar de 1 pano / De fundo" : 8,
        "Pesca à linha / Palangre de Fundo + Cana e linha de mão (2008-2017)":9,
        "Pesca à linha / Palangre de superfície / Grandes Migradores (2014-2017)":10
        }

    #def processTrip(vesselId, start, end):
    def processTrip(self,args):
        vesselId = args[0]
        start = args[1]
        end = args[2]
        print('process ', str(vesselId))
        data = VMSRecordsDAL().importVesselData(vesselId, start, end)
        
        dataResumed = VMSResumed(vesselId,data[1],data[0],data[2],-1)

        cPred = Classifier.predict(dataResumed,data[3],data[4])

        cVessel= VMSVesselsDAL().importLicense(vesselId)
        if(cVessel in PreProcessCore.licenseDic):
            license = PreProcessCore.licenseDic[cVessel]
            if(cPred != license):
                print('alert')
        else:
            print(str(cVessel)+' not in licenseDic')
        print(str(cVessel)+' Done '+ str(cPred))


