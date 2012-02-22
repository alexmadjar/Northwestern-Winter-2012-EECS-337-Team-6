output_file = open("C:\Users\Ben\Northwestern-Winter-2012-EECS-337-Team-6\meat_subs.txt",'w')
input_file = open("C:\Users\Ben\Northwestern-Winter-2012-EECS-337-Team-6\meats.txt",'r')
output_file.write('{')
for line in input_file.readlines():
    line = line.strip()
    output_file.write("\'"+line+"\' : \'"+line+"sub\',\n")
output_file.write('}')
    
input_file.close()
output_file.close()