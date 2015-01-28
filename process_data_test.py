line=raw_input()
line=raw_input()
cnt=0
while line:
	cnt+=1
	line = line.split(',')
	print '|',
	for i in range(1,len(line)):
		out_val=0
		for j in line[i]:
			out_val+=ord(j)
		print str(i-1)+':'+str(out_val),
	print '\n',
	line = raw_input()
