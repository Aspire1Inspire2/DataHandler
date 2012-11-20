__metaclass__ = type

from datetime import datetime, time

class DataHandler:
    
    def __init__(self):
        #current line time
        self.currTime = datetime.strptime('0931', '%H%M');
        #previous line time
        self.prevTime = datetime.strptime('1600', '%H%M');
        #number of endtime errors
        self.endTimeError = 0
        #number of start time errors
        self.startTimeError = 0
        #number of gap errors
        self.gapError = 0

    #check time field of the data
    #begin time, gap and end time checks
    def __checkTime(self, time):
        #set the current time
        self.currTime = datetime.strptime(time, '%H%M');
        #find the border of the consecutive days
        if (((self.prevTime.hour == 16) or (self.prevTime.hour == 15)) and (self.currTime.hour == 9)):
            #incorrect endtime of the day
            if (self.prevTime.hour != 16):
                self.endTimeError += 1
                #print  'endTimeError: ', i
            #incorrect start time of the day
            if (self.currTime.minute != 31):
                self.startTimeError += 1
                #print 'startTimeError: ', i
        #find the gaps between data samples
        else:
            deltat = self.currTime - self.prevTime
            #if time delta between two consecutive samples != 1 min => error
            if (str(deltat).split(':')[1] != '01'):
                self.gapError += 1
                #print i
        self.prevTime = self.currTime        

    #check time, price and volume fields of the data
    def checkData(self, fName):
        file = open(fName, 'r')
        #read header
        file.readline()
        #read rest of the file
        for line in file.readlines():
            #extract the time field
            [date, time, open_, high, low, close, volume] = line.split(',')
            self.__checkTime(time)
        file.close()
        print self.endTimeError
        print self.startTimeError
        print self.gapError


