Stock intraday data check & extract class
--------------------------------------------
- Data format: Metastock ascii (7 columns)
- Should work with all time intervals under 60 min (tested with 1-min data only !)
- test data: test.txt, A.txt

Following checks available:
- Opening time of the day (0930)
- Closing time of the day (1600)
- Gaps in time
- Price and volume checks (>=0)
- Generates error info file *_err.txt

Extract:
- Extracts data from given dates (start -> end) and creates a new data file

Public methods
---------------
checkData(file):
- Data checker
- Data from file

dataExtract(rFile, wFile, startDate, endDate):
- Data extract
- Data from rFile
- New data file wFile
- Start date startDate (format: MM/DD/YYYY)
- End date endDate (format: MM/DD/YYYY)