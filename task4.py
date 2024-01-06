#Task-4
inputFile=open('input4.txt','r')
f_line=int(inputFile.readline())
train_names=[]
dep_time=[]
dest=[]
out=[]
for i in range(f_line):
  line=inputFile.readline()
  train_name=line.split(" will departure for ")[0]
  train_names.append(train_name)
  schedule=line.split(" at ")[1]
  dep_time.append(schedule)
  loc=line.split(" ")[4]
  dest.append(loc)
def selectionSort(train):
  for i in range(f_line-1):
    min_index=i
    for j in range(i+1,f_line):
      if train[j][0]<train[min_index][0]:
        min_index=j
      if train[j][0]==train[min_index][0]:
        if train[j][1]>train[min_index][1]:
          min_index=j
    train[i],train[min_index]=train[min_index],train[i]
train=list(zip(train_names,dep_time,dest))
selectionSort(train)
for j in train:
  result=f'{j[0]} will departure for {j[2]} at {j[1]}'
  out.append(result)
outputFile=open('output4.txt','w')
outputFile.writelines(out)
inputFile.close()
outputFile.close()