line=raw_input()
line=raw_input()
cnt=0
while line:
	cnt+=1
	line = line.split(',')
	print str(line[1]),'|',
	for i in range(2,len(line)):
		out_val=0
		for j in line[i]:
			out_val+=ord(j)
		print str(i-2)+':'+str(out_val),
	print '\n',
	line = raw_input()
