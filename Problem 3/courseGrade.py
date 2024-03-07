def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    allInfo = []
    allReports = []
    fileNames = input().split("\n")
    tableNum = len(fileNames)
    studentInfo = open(fileNames[0], 'r')
    allInfo.append(studentInfo)
    report = open("report.txt", 'a')
    allReports.append(report)
    if tableNum >= 2:
        studentInfo1 = open(fileNames[1], 'r')
        allInfo.append(studentInfo1)
        report1 = open("report1.txt", 'a')
        allReports.append(report1)
    if tableNum == 3:
        studentInfo2 = open(fileNames[2], 'r')
        allInfo.append(studentInfo1)
        report2 = open("report2.txt", 'a')
        allReports.append(report2)
    
    i = 0
    while i < tableNum:
        count = 0
        midterm1Av = 0
        midterm2Av = 0
        finalAv = 0
        for line in allInfo[i]:
            infolist = line.split()
            count += 1
            midterm1Av += float(infolist[2])
            midterm2Av += float(infolist[3])
            finalAv += float(infolist[4])
            if ((float(infolist[2]) + float(infolist[3]) + float(infolist[4])) / 3) >= 90:
                grade = "A"
                infolist.append(grade)
            elif ((float(infolist[2]) + float(infolist[3]) + float(infolist[4])) / 3) >= 80:
                grade = "B"
                infolist.append(grade)
            elif ((float(infolist[2]) + float(infolist[3]) + float(infolist[4])) / 3) >= 70:
                grade = "C"
                infolist.append(grade)
            elif ((float(infolist[2]) + float(infolist[3]) + float(infolist[4])) / 3) >= 60:
                grade = "D"
                infolist.append(grade)
            else:
                grade = "F"
                infolist.append(grade)
            for j in range(6):
                allReports[i].write(str(infolist[j]) + " ")
            allReports[i].write("\n")
        midterm1Av = midterm1Av / count
        midterm2Av = midterm2Av / count
        finalAv = finalAv / count
        allReports[i].write("Averages: midterm1 " + f'{midterm1Av:.2f}' + ", midterm2 " + f'{midterm2Av:.2f}' + ", final " + f'{finalAv:.2f}')
        i += 1
      
      
    # TODO: Read a file name from the user and read the tsv file here. 
   
   
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    return

if __name__ == "__main__":
    courseGrade()
    
    