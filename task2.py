inputFile=open('input2.txt','r')
f_line=int(inputFile.readline())
list1=list(map(int,inputFile.read().split(" ")))
def bubbleSort(list1):
  swapped=False
  for i in range(f_line-1):
    for j in range(f_line-i-1):
      if list1[j] > list1[j+1]:
        list1[j], list1[j+1] = list1[j+1], list1[j]
        swapped=True
    if swapped==False:
      break
bubbleSort(list1)
outputFile=open('output2.txt',mode='w')
outputFile.writelines(' '.join(map(str,list1)))
inputFile.close()
outputFile.close()
#The key to achieving θ(n) time complexity in the best-case scenario (when the input array is already sorted) is to add a flag that checks if a swap has occurred in the inner loop. If no swap has occurred, it means the array is already sorted and we can break out of the loop early.