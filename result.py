n=eval(raw_input("enter number of subjects:"))
sub1=['maths','english','physics','gujarti','chemistry','computer']
sub={}
for i in range(0,n):
	print "enter marks of " +sub1[i]+" :"
	#print sub1[i]
	sub[sub1[i]]=eval(raw_input())
print sub
