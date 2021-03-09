def swappingFileData():
    ogFile=input("Enter the file name\t")
    swappedFile=input("Enter another file name\t")

    with open(ogFile,'r') as a:
        data_a=a.read()

    with open(swappedFile,'r') as b:
        data_b=b.read()
    # print("Oringinal File's Text: ",data_a,"\n","Prank File's Text",data_b)

    with open(ogFile,'w') as c:
        c.write(data_b)

    with open(swappedFile,'w') as d:
        d.write(data_a)

    print("Original File: ",data_a)
    print("Prank File: ",data_b)
    

swappingFileData()