inputFile=open('input1a.txt','r')
f_line=inputFile.readline()
out=[]
for i in range(int(f_line)):
  num=int(inputFile.readline())
  if num%2==0:
    result=f"{num} is an Even number\n"
  else:
    result=f"{num} is an Odd number\n"
  out.append(result)
outputFile=open('output1a.txt',mode='w')
outputFile.writelines(out)
inputFile.close()
outputFile.close()