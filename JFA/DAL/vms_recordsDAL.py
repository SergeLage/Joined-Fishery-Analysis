import psycopg2
from Models.dataset_original import DatasetOriginal
from Models.dataset_resumed import DatasetResumed


class VMSRecordsDAL:
    _host = "localhost" 
    _port = "5433"
    _database = "JFAdb"
    _user = "postgres"
    _pwd = "1"

    def _createConn(self):
        connection = psycopg2.connect(user = self._user,
                                    password = self._pwd,
                                    host = self._host,
                                    port = self._port,
                                    database = self._database)
        cur = connection.cursor()
        return cur,connection

    def insertunique(self, data):
        print('insertVMSRecords')
        try:
            cur ,connection= self._createConn()
            #sql = "insert into vmsrecords values ( "+  str(data.ID) + ", " +  str(data.VesselID) + ", '" + str(data.utc) + "', '" + str(data.gps_id) + "', '" + str(data.Fix) + "', '" + str(data.lat) + "', '" + str(data.lon)+ "' , '" + str(data.cog) + "', '" + str(data.sog) + "', '" + str(data.fix2) + "', '" +  str(data.lat2) + "', '" +  str(data.lon2) +"')"
            sql = "insert into vmsrecords  ( vesselid, utc, pgs_id, fix, lat, lon, cog, sog, fix2, lat2, lon2)  values ( "+str(data.VesselID) + ", '" + str(data.utc) + "', '" + str(data.gps_id) + "', '" + str(data.Fix) + "', '" + str(data.lat) + "', '" + str(data.lon)+ "' , '" + str(data.cog) + "', '" + str(data.sog) + "', '" + str(data.fix2) + "', '" +  str(data.lat2) + "', '" +  str(data.lon2) +"')"
            print(sql)
            cur.execute(sql)
            connection.commit()
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
            if(connection):
                cur.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def insertList(self, list):
        print('insertVMSRecords')
        try:
            cur ,connection= self._createConn()
            for v in list:
                #sql = "insert into vmsrecords values ( "+  str(v.ID) + ", " +  str(v.VesselID) + ", '" + str(v.utc) + "', '" + str(v.gps_id) + "', '" + str(v.Fix) + "', '" + str(v.lat) + "', '" + str(v.lon)+ "' , '" + str(v.cog) + "', '" + str(v.sog) + "', '" + str(+v.fix2) + "', '" +  str(v.lat2) + "', '" +  str(v.lon2) +"')"
                sql = "insert into vmsrecords  ( vesselid, utc, pgs_id, fix, lat, lon, cog, sog, fix2, lat2, lon2) values ( "+  str(v.VesselID) + ", '" + str(v.utc) + "', '" + str(v.gps_id) + "', '" + str(v.Fix) + "', '" + str(v.lat) + "', '" + str(v.lon)+ "' , '" + str(v.cog) + "', '" + str(v.sog) + "', '" + str(+v.fix2) + "', '" +  str(v.lat2) + "', '" +  str(v.lon2) +"')"    
                print(sql)
                cur.execute(sql)
                connection.commit()
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
            if(connection):
                cur.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def importVesselData(self, vesselId, start, end):
        res = []
        try:
            cur ,connection= self._createConn()
            db_cmd = "SELECT  MAX(sog), MIN(sog), AVG(sog), AVG(lat), AVG(lon) FROM public.vmsrecords  where vesselid = "+str(vesselId)+" and utc >=\'"+str(start)+"\' and utc <= \'"+str(end)+"\' "
            print(db_cmd)
            cur.execute(db_cmd)
            resSQL = cur.fetchall()
            for r in resSQL:
                res.append(r[0])
                res.append(r[1])
                res.append(r[2])
                res.append(r[3])
                res.append(r[4])
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            if(connection):
                cur.close()
                connection.close()
        return res

    def selectResumed(self, vesselID):
            res = []
            try:
                cur ,connection= self._createConn()
                db_cmd = "SELECT * FROM datasetresumed" if  vesselID==-1 else  "SELECT * FROM datasetresumed where VesselID = "+str(vesselID)
                print(db_cmd)
                cur.execute(db_cmd)
                resSQL = cur.fetchall()
                for r in resSQL:
                    res.append(DatasetResumed(r[0],r[1],r[2],r[3],r[4],r[5],r[6],r[7],r[8],r[9],r[10],r[11],r[12],r[13], r[14]))
            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PostgreSQL", error)
            finally:
                if(connection):
                    cur.close()
                    connection.close()
            return res

    def selectFiltred(self, vesselID):
        res = []
        try:
            cur ,connection= self._createConn()
            db_cmd = "SELECT * FROM datasetfiltred" if  vesselID==-1 else  "SELECT * FROM datasetfiltred where VesselID = "+str(vesselID)
            print(db_cmd)
            cur.execute(db_cmd)
            resSQL = cur.fetchall()
            for r in resSQL:
                res.append(DatasetOriginal(r[0],r[1],r[2],r[3],r[4],r[5],r[6],"",r[7],r[8],r[9],r[10],r[11],r[12],r[13]))
        except (Exception, psycopg2.Error) as error :
            print ("Error while connecting to PostgreSQL", error)
        finally:
            #closing database connection.
            if(connection):
                cur.close()
                connection.close()
        return res