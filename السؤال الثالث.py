text='C:\\Q.txt'
infile=open(text, 'r')
x=0
name= input('enter your name')
for i in range (20):
  s=infile.readline()
  l=s.split('.')
  print (l[0])
  an= input()
  a=an+'\n'
  if (l[1]==a):
      x=x+1
text2='C:\\an.txt'
result=open(text2,'w')
result.write(name)
result.write(str(x))
result.close()
infile.close()