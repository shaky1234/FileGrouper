#Used to group and organize files based on year and month
from os import mkdir, path, walk, rename
import time, datetime

#Your starting directory
startpath = "C:\\Users\\guest\\Pictures"

def Move_Files(Origin,Dest):
    print("Moved file {} to {}".format(Origin,Dest))
    rename(Origin, Dest)

class FileObj:
    def __init__(self, FilePath, File):
        self.FilePath = FilePath
        self.File = File


class FileDateObj:
    def __init__(self, FileObj, Month, Year):
        self.FileObj = FileObj
        self.Month = Month
        self.Year = Year

filelist = []

for (dirpath, dirname, filenames) in walk(startpath):

    for f in filenames:filelist.append(FileObj(dirpath+"\\"+f,f))

    break

FileObjList = []
for file in filelist: 
    tempdate = datetime.datetime.strptime(time.ctime(path.getctime(file.FilePath)),  "%a %b %d %H:%M:%S %Y")
    match tempdate.month:
        case 1:
            tempMonth = "January"
        case 2:
            tempMonth = "February"
        case 3:
            tempMonth = "March"
        case 4:
            tempMonth = "April"
        case 5:
            tempMonth = "May"
        case 6:
            tempMonth = "June"
        case 7:
            tempMonth = "July"
        case 8:
            tempMonth = "August"
        case 9:
            tempMonth = "September"
        case 10:
            tempMonth = "October"
        case 11:
            tempMonth = "November"
        case 12:
            tempMonth = "December"
    FileObjList.append(FileDateObj(file, tempMonth, tempdate.year))


for x in FileObjList:
    yeardirexist = path.isdir("{}\\{}\\".format(startpath,x.Year)) 
    if not yeardirexist:
        mkdir("{}\\{}\\".format(startpath,x.Year))
        
    monthdirexist = path.isdir("{}\\{}\\{}\\".format(startpath,x.Year,x.Month)) 
    if not monthdirexist:
        mkdir("{}\\{}\\{}\\".format(startpath,x.Year,x.Month))
    
    Move_Files(x.FileObj.FilePath,"{}\\{}\\{}\\{}".format(startpath,x.Year,x.Month,x.FileObj.File))
    