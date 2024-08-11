def bubbleSort():
    print("Before sorting:\n",percentage)
    for i in range(num-1,0,-1):
        for j in range(i):
            if percentage[j]>percentage[j+1]:
                percentage[j],percentage[j+1]=percentage[j+1],percentage[j]
    print("After sorting:\n",percentage)
    topFiveMarks()
