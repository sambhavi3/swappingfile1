def swapFileData():
    fileName =  input("Enter the file name to swap:- ")
    
    with open(file1, 'w') as a:
        a.write(data_b)

    with open(file1, 'r') as a:
        data_a = a.read()


swapFileData()