#Task-3
inputFile=open('input3.txt','r')
f_line=int(inputFile.readline())
id=list(map(int,(inputFile.readline().split(" "))))
marks=list(map(int,(inputFile.readline().split(" "))))
out=[]
def selectionSort(students):
  for i in range(f_line-1):
    min_index=i
    for j in range(i+1,f_line):
      if students[min_index][1]<students[j][1]:
        min_index=j
      if students[min_index][1]==students[j][1]:
        if students[j][0]<students[min_index][0]:
          min_index=j
    students[i],students[min_index]=students[min_index],students[i]
students=list(zip(id,marks))
selectionSort(students)
for j in students:
  result=f'ID: {j[0]} Mark: {j[1]}\n'
  out.append(result)
outputFile=open('output3.txt','w')
outputFile.writelines(out)
inputFile.close()
outputFile.close()