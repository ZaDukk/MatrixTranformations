def getTmatrix():
    print("hello and welcome to my matrix plotter")
    print("this program takes in a 2d matrix and shows how integer points when transformed by it")
    print("please enter your matrix in the form: 11,12,21,22")
    print("where 11 represents row 1 colum 1 of the matrix, make sure its sperated by commas and not spaces!")
    print("enter your matrix now")
    niput = input().split(",")


    niput = [int(i)for i in niput]

    tMatix = [[niput[0],niput[1]],[niput[2],niput[3]]]
    print("excellent, now tell me the minimum and maximum value of x and y should be")
    print("use the format: minX,maxX,minY,maxY")
    minMax = input().split(",")
    minMax = [int(i) for i in minMax]
    return (tMatix,minMax[0],minMax[1],minMax[2],minMax[3])


