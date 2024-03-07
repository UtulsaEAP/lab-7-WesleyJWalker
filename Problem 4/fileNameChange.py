def fileNameChange():
    #type your code here
    with open(input(), '+r') as ParkPhotos:
        for line in ParkPhotos:
            toprint = line.replace("_photo.jpg", "_info.txt")
            print(toprint.strip("\n"))
    return

if __name__ == '__main__':
    fileNameChange()