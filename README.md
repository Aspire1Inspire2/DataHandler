Stock intraday data checker & splitter class
--------------------------------------------
Following checks available:
- Opening time of the day (0930)
- Closing time of the day (1600)
- Gaps in time
- Price and volume checks (>=0)

Splitter:
- Extracts data from given dates and creates a new data file

Public methods
---------------
checkData(file):
- data checker
- data from file

dataSplit(rFile, wFile, startDate, endDate):
- data splitter
- data from rFile
- new data file wFile
- start date startDate (format: MM/DD/YYYY)
- end date endDate (format: MM/DD/YYYY)