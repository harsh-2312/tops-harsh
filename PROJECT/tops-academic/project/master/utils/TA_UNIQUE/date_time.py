from datetime import datetime

class currentdatetime:
    currentdate = datetime.now()

    def __init__(self):
        self.month = currentdatetime.currentdate.strftime("%m")
        self.year = currentdatetime.currentdate.strftime("%y")

CURRENT_DATETIME = currentdatetime()
print(CURRENT_DATETIME.month) 
