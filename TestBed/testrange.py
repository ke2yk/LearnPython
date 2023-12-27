import os

#os.system('ls -la')

os.system('clear')

#x = input('Enter your name:')
#print('Hello, ' + x)

x = input("enter start range: ")
x = int(x)

y = input("enter stop range: ")
y = int(y)

myrange = range(x,y) 

def myfunc(var):
	if var == 5: 
		print("Hello World Mo and Mo")
	else:
		print(var, "No Friggin Good")
pass

for myvar in myrange: 
 	#print(myvar)
 	myfunc(myvar)