import logging;
from datetime import datetime;
import Utils;
import os;

class LoggerService:
    def __init__(self, programName: str, details: str, generiLogFile: str = "0_ExecutionLog", addTimeFolder: bool = True, logFormat: str = '%(asctime)s - %(message)s'):
        self.__ProgramName = programName;
        self.__LogPath = f"{self.__ProgramName.replace(' ', '_')}_Log/{details}";
       
        #if os.path.exists(self.__LogPath):
        #    raise FileExistsError("Duplicate Executions are Denied!");
        #else:
        if addTimeFolder:
            self.__LogPath += "/" + datetime.now().strftime("%Y%m%d_%H%M%S");
        os.makedirs(self.__LogPath);
       
        self.__Istance = logging; #.getLogger(self.__LogPath);
        self.__Istance.basicConfig(
            filename = f"{self.__LogPath}/{generiLogFile}.log",
            level = logging.INFO,
            format = logFormat
        );
        self.__Istance.info(f"{self.__ProgramName} START");
   
        self.__CustomTimer = datetime.now();
        self.__Timer = datetime.now();
   
    def AddLog(self, message):
        self.__Istance.info(message);

    def StartTiming(self, message):
        self.__Istance.info(message);
        self.__CustomTimer = datetime.now();

    def EndTiming(self):
        self.__Istance.info(f"\tDuration: {Utils.TimeToString(Utils.CalculateTime(self.__CustomTimer))}");
   
    def StartGenericTiming(self):
        self.__Timer = datetime.now();

    def ForceEnd(self):
        self.__Istance.info(f"Total Duration: {Utils.TimeToString(Utils.CalculateTime(self.__Timer))}");
        self.__Istance.info(f"{self.__ProgramName} FORCED END\n\n");

    def End(self):
        self.__Istance.info(f"Total Duration: {Utils.TimeToString(Utils.CalculateTime(self.__Timer))}");
        self.__Istance.info(f"{self.__ProgramName} END\n\n");

    def LogPath(self) -> str:
        return self.__LogPath;