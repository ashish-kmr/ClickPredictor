store_output=[]
line_1=1
count_id=0
count_pred=0
f=open('test.csv')
for line in f:
	if line_1==1:
		line_1=0
		continue
	temp=line.split(',')
	store_output.append([temp[0]])
	count_id+=1

f=open('p_out')
cnt=0
for line in f:
	count_pred+=1
	store_output[cnt].append(line)
	cnt+=1

print 'id,click'
for i in store_output:
	print str(i[0])+','+str(i[1]),
