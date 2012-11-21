Stock intraday data check & extract class
--------------------------------------------
Following checks available:
- Opening time of the day (0930)
- Closing time of the day (1600)
- Gaps in time
- Price and volume checks (>=0)

Extract:
- Extracts data from given dates (start -> end) and creates a new data file

Public methods
---------------
checkData(file):
- data checker
- data from file

dataExtract(rFile, wFile, startDate, endDate):
- data extract
- data from rFile
- new data file wFile
- start date startDate (format: MM/DD/YYYY)
- end date endDate (format: MM/DD/YYYY)