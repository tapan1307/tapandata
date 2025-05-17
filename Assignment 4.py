print('Task 1')
file1=open('sample.ts', "r")
reader=file1.read()
print(reader)
file1.close()

print('Task 2')
file2=open('output.ts', "w")
writer=file2.write(input('Enter your text to write to the File: '))
file2.close()

file2=open('output.ts', "r")
reader=file2.read()
print(reader)
file2.close()

file2=open('output.ts', "a")
appender=file2.write(input('Enter additional text to append to the File: '))
file2.close()

file2=open('output.ts', "r")
reader=file2.read()
print(reader)
file2.close()
