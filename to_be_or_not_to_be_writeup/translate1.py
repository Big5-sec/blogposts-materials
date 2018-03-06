data = ""
output_data=""
with open("challenge.ws",'r') as file:
    data= file.read()

for x in data:
    if x == ' ':
        output_data+=" S"
    elif x == '\t':
        output_data+=" T"
    else :
        output_data+='N\n'

with open("challenge_first_step.txt",'w') as file2:
    file2.write(output_data)
