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

def topFiveMarks():
    print("Top 5 scores are : ")
    for i in range(num-1,0,-1):
        for j in range(i):
            if percentage[j]<percentage[j+1]:
                percentage[j],percentage[j+1]=percentage[j+1],percentage[j]
    print(percentage[:6])

def repeat():
    num = int(input("Enter your choice"))
    str(num).strip()
    if num == 1:
        selectionSort()
    elif num == 2:
        bubbleSort()
    else:
        print("Invalid Input!!\nEnter a valid input!")
        repeat()

percentage=[]
num = int(input("Enter number of students:"))
for i in range(num):
    per=int(input(f"Enter percentage of the student {i+1}:"))
    percentage.append(per)

print("Which sort do you want to perform?")
print("1. Selection sort")
print("2. Bubble Sort")
repeat()
