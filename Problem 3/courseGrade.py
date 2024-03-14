def courseGrade():
    
    # TODO: Declare any necessary variables here. 
    fileName = input()
    studentInfo = open(fileName, 'r')
    if fileName == "./Problem 3/StudentInfo.tsv":
        report = open("./Problem 3/report.txt", '+w')
    elif fileName == "./Problem 3/StudentInfo1.tsv":
        report = open("./Problem 3/report1.txt", '+w')
    elif fileName == "./Problem 3/StudentInfo2.tsv":
        report = open("./Problem 3/report2.txt", '+w')
    else:
        print("Invalid file name")
        return
    
    count = 0
    midterm1Av = 0
    midterm2Av = 0
    finalAv = 0
    for line in studentInfo:
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
        #These lines output what is in the Readme:
        '''report.write(line.strip("\n") + "   " + str(infolist[5]))
        report.write("\n")'''
        
        #These outputs have (strange spacing)
        '''for i in range(6):
            if i == 0:
                report.write(str(infolist[i]) + " ")
            elif i > 0 and i < 5:
                report.write(str(infolist[i]) + "   ")
            else:
                report.write(str(infolist[i]) + "\n")'''
        
        report.write(line + "   " + infolist[5])
    midterm1Av = midterm1Av / count
    midterm2Av = midterm2Av / count
    finalAv = finalAv / count
    report.write("\n" + "Averages: midterm1 " + f'{midterm1Av:.2f}' + ", midterm2 " + f'{midterm2Av:.2f}' + ", final " + f'{finalAv:.2f}')
      
      
    # TODO: Read a file name from the user and read the tsv file here. 
   
   
    # TODO: Compute student grades and exam averages, then output results to a text file here. 
    return

if __name__ == "__main__":
    courseGrade()
    
    