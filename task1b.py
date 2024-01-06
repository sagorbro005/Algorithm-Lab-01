
inputFile=open('input1b.txt','r')
f_line=inputFile.readline()
out=[]
for i in range(int(f_line)):
  list1=inputFile.readline().split(" ")
  if list1[2]=="+":
    result=f'The result of {int(list1[1])} + {int(list1[3])} is {int(list1[1])+int(list1[3])}\n'
  elif list1[2]=="-":
    result=f'The result of {int(list1[1])} - {int(list1[3])} is {int(list1[1])-int(list1[3])}\n'
  elif list1[2]=="*":
    result=f'The result of {int(list1[1])} * {int(list1[3])} is {int(list1[1])*int(list1[3])}\n'
  elif list1[2]=="/":
    result=f'The result of {int(list1[1])} / {int(list1[3])} is {int(list1[1])/int(list1[3])}\n'
  out.append(result)
outputFile=open('output1b.txt',mode='w')
outputFile.writelines(out)
inputFile.close()
outputFile.close()