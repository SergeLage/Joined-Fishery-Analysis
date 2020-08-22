
class DatasetResumed:
    def __init__(self, id, vesselID, date, lat, lon, sogAVG, sogMax, sogMin, loa, gt, hp, license, l1, l2, l3):
        self.id = id
        self.vesselID = vesselID
        self.date = date
        self.lat = float(lat)
        self.lon = float(lon)
        self.sogAVG = sogAVG
        self.sogMax = sogMax
        self.sogMin = sogMin
        self.loa = loa
        self.gt = gt
        self.hp = hp
        self.license =int( license)
        self.l1 = l1 
        self.l2 = l2
        self.l3 = l3

    #def __init__(self, lat, lon):
    #    self.lat = float(lat)
    #    self.lon = float(lon)

    def setLoc(self,loc):
        self.loc = loc

    @staticmethod
    def GetFeatureNames():
        return [ 'sogAVG', 'sogMax', 'sogMin', 'loc']

    def GetFeatureMinNames():
        return [ 'sogAVG', 'sogMin', 'loc']

    @staticmethod
    def GetFeatureSogNames():
        return [ 'sogAVG', 'sogMax', 'sogMin']

    @staticmethod
    def GetFeatureSogMaxNames():
        return [ 'sogMax']

    @staticmethod
    def GetFeatureSogAvgNames():
        return [ 'sogAVG']
