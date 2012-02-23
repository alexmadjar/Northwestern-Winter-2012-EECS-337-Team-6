input_path = raw_input('provide path of non-dict meats file\n')
output_path = raw_input('provide path of desired dict meat subs file\n')

output_file = open(output_path,'w')
input_file = open(input_path,'r')
output_file.write('{')
for line in input_file.readlines():
    line = line.strip()
    output_file.write("\'"+line+"\' : \'"+line+"sub\',\n")
output_file.write('}')
    
input_file.close()
output_file.close()