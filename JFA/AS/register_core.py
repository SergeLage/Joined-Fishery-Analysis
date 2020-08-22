from DAL.vms_recordsDAL import VMSRecordsDAL
from datetime import datetime
from datetime import timedelta
import time
from AS.pre_process_core import PreProcessCore

class RegisterCore:
    _control = {}
    _isRuning = False

    @staticmethod
    def newEntry(vms):
        VMSRecordsDAL().insertunique(vms)
        if(vms.isFishing):
            RegisterCore.fishingCore(vms)
   
    @staticmethod
    def fishingCore(vms):
        if(vms.VesselID in RegisterCore._control):
            RegisterCore._control[vms.VesselID] = [RegisterCore._control[vms.VesselID][0],datetime.now()]
        else:
            RegisterCore._control[vms.VesselID] = [datetime.now(),datetime.now()]
        if RegisterCore._isRuning == False:
            RegisterCore.runTimer()

    @staticmethod
    def runTimer():
        RegisterCore._isRuning = True
        print('runTimer Start')
        while True:
            print(RegisterCore._control)
            for r in RegisterCore._control:
                proc = RegisterCore._control[r]
                print(r ," :: ",(datetime.now() - timedelta(minutes=1)), " :: ",proc[0], " :: ", proc[1])
                if(proc[1] < (datetime.now() - timedelta(minutes=1))):
                    print(str(r))
                    args = [str(r),proc[0],proc[1]]
                    print(args)
                    PreProcessCore().processTrip(args)
                    #PreProcessCore().processTrip(str(r), proc)
            time.sleep(60)