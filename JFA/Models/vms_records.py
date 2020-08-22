class VMSRecords:
    def __init__(self, ID, VesselID, utc, gps_id, Fix, lat, lon, cog, sog, fix2, lat2,lon2,isFishing):
        self.ID = ID
        self.VesselID = VesselID
        self.utc = utc
        self.gps_id = gps_id
        self.Fix = Fix
        self.lat = lat
        self.lon = lon
        self.cog = cog
        self.sog = sog
        self.fix2 = fix2
        self.lat2 = lat2
        self.lon2 = lon2
        self.isFishing = isFishing

    def __init__(self, VesselID, utc, gps_id, Fix, lat, lon, cog, sog, fix2, lat2,lon2, isFishing):
        self.VesselID = VesselID
        self.utc = utc
        self.gps_id = gps_id
        self.Fix = Fix
        self.lat = lat
        self.lon = lon
        self.cog = cog
        self.sog = sog
        self.fix2 = fix2
        self.lat2 = lat2
        self.lon2 = lon2
        self.isFishing = isFishing

    def serialize(self):
        return {
            'VesselID': self.VesselID, 
            'utc': self.utc,
            'gps_id': self.gps_id,
            'Fix': self.Fix,
            "lat": self.lat,
            "lon": self.lon,
            "sog": self.sog,
            "isFishing": self.isFishing
        }