import psycopg2


class VMSVesselsDAL:
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

    def importLicense(self, vesselID):
            try:
                cur ,connection= self._createConn()
                db_cmd = "SELECT * FROM public.vmsvessels where \"ID\" = "+str(vesselID)
                print(db_cmd)
                cur.execute(db_cmd)
                resSQL = cur.fetchall()
                for r in resSQL:
                    return r[5]
            except (Exception, psycopg2.Error) as error :
                print ("Error while connecting to PostgreSQL", error)
            finally:
                if(connection):
                    cur.close()
                    connection.close()
            return res



