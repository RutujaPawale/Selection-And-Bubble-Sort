def selectionSort():
    print("Before sorting:\n", percentage)
    for i in range(num):
        min=i
        for j in range(i+1,num):
            if percentage[min]>percentage[j]:
                min=j
        percentage[i],percentage[min]=percentage[min],percentage[i]
    print("After sorting:\n",percentage)
    topFiveMarks()

def bubbleSort():
    print("Before sorting:\n",percentage)
    for i in range(num-1,0,-1):
        for j in range(i):
            if percentage[j]>percentage[j+1]:
                percentage[j],percentage[j+1]=percentage[j+1],percentage[j]
    print("After sorting:\n",percentage)
    topFiveMarks()
