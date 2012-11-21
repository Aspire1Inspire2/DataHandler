__metaclass__ = type

from datetime import datetime, time
from config import *

class DataHandler:
    
    def __init__(self):
        #current time
        self.currTime = datetime.strptime(START_TIME, TIME_FORMAT)
        #previous time (line ago)
        self.prevTime = datetime.strptime(END_TIME, TIME_FORMAT)
        #number of endtime error
        self.endTimeError = 0
        #number of start time errors
        self.startTimeError = 0
        #number of gap errors
        self.gapError = 0
        #price and volume errors
        self.priceError = 0

    #check time field of the data
    #start time, gap and end time checks
    def __checkTime(self, time):
        #set the current time
        self.currTime = datetime.strptime(time, TIME_FORMAT)
        #find the border of the consecutive day.
        #End time of the day can be 1600 or 15** and start time is 09**
        if (((self.prevTime.hour == int(END_TIME[:2])) or (self.prevTime.hour == (int(END_TIME[:2]) - 1))) and (self.currTime.hour == int(START_TIME[:2]))):
            #incorrect endtime of the day
            if (self.prevTime.hour != int(END_TIME[:2])):
                self.endTimeError += 1
            #incorrect start time of the day
            if (self.currTime.minute != int(START_TIME[-2:])):
                self.startTimeError += 1
        #find the gaps between data samples
        else:
            deltat = self.currTime - self.prevTime
            #check time delta between two consecutive samples
            if (str(deltat).split(':')[1] > TIME_DELTA):
                self.gapError += 1
        self.prevTime = self.currTime

    #check price and volume fields
    def __checkPrice(self, dataList):
        #check if data < 0
        def checkValue(x):
            if (x <= 0):
                return 1;
            else:
                return 0;
        tmpList = map(checkValue, dataList)
        self.priceError += sum(tmpList)
        
    #check time, price and volume fields of the data
    def checkData(self, fName):
        rFile = open(fName, 'r')
        #read header
        rFile.readline()
        #read rest of the file
        for line in rFile.readlines():
            #extract the time field
            [date, time, open_, high, low, close, volume] = line.split(',')
            self.__checkTime(time)
            self.__checkPrice([float(open_), float(high), float(low), float(close), int(volume)])
        rFile.close()
        #write error file if errors found
        if ((self.endTimeError + self.startTimeError + self.gapError + self.priceError) != 0):
            wFile = open(fName.split('.')[0] + '_err.txt', 'w')
            wFile.write('endTimeErrors: ' + str(self.endTimeError) + '\n')
            wFile.write('startTimeErrors: ' + str(self.startTimeError) + '\n')
            wFile.write('gapErrors: ' + str(self.gapError) + '\n')
            wFile.write('priceErrors: ' + str(self.priceError) + '\n')

    #file split
    def dataSplit(self, rFile, wFile, startDate, endDate):
        readFile = open(rFile, 'r')
        writeFile = open(wFile, 'w')
        #start and end dates
        sDate = datetime.strptime(startDate, DATE_FORMAT)
        eDate = datetime.strptime(endDate, DATE_FORMAT)
        #print sDate
        #read header
        readFile.readline()
        #read rest of the file
        for line in readFile.readlines():
            date = datetime.strptime(line.split(',')[0], DATE_FORMAT)
            #print date
            if ((date >= sDate) and (date <= eDate)):
                #print line
                writeFile.write(line)
        readFile.close()
        writeFile.close()
        
                
                
        


