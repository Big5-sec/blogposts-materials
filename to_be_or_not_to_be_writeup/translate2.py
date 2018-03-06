#list possible combinations ofthe language
combinations= {
    #arithmetic combinations
    "\t   ": "add",
    "\t  \t" : "substract",
    "\t \n": "multiply",
    "\t \t ": "integer division",
    "\t \t\t":"modulo",

    #stack combinations
    "  " : "push_stack",
    " \n ":"duplicate_stack",
    " \n\t":"swap stack",
    " \n\n":"discard stack",

    #heap combinations
    "\t\t ":"store",
    "\t\t\t":"retrieve",

    #flow control combinations
    "\n  ":"mark location",
    "\n \t":"call subroutine",
    "\n \n":"jump to label",
    "\n\t ":"jump if top stack is zero",
    "\n\t\t":"jump if top stack negative",
    "\n\t\n":"end subroutine",
    "\n\n\n":"end program",

    #io
    "\t\n  ":"print character",
    "\t\n \t":"print number",
    "\t\n\t ":"read character",
    "\t\n\t\t":"read number"
}

data = ""
output_data=""
with open("challenge.ws",'r') as file:
    data= file.read()

temp_string=""
i =0
bol=False
#we read the whole file, and whenever a combination is valid, get it
while i < len(data)-1:
    temp_string+=data[i]
    try:
        if combinations[temp_string] is not None:
            #some combinations require more_treatment
            #especially the following use a number after the combination
            if combinations[temp_string] == "push_stack" or combinations[temp_string] == "mark location" or combinations[temp_string]=="call subroutine" or combinations[temp_string] == "jump to label" or combinations[temp_string]=="jump if top stack is zero" or combinations[temp_string]=="jump if top stack negative":
                i+=1
                number=0
                j=0
                #first get length of the number
                k=i
                while data[k] != '\n':
                    k+=1
                l=k-i-1
                #then get the value of the number
                while data[i] != '\n':
                    if data[i] == '\t':
                        number+=(2**(l-j))
                    j+=1
                    i+=1

                #print translated combination + number
                output_data+=combinations[temp_string]
                output_data+=" "
                #we treat here the case the number associated with the command is printable
                if (number <= 122 and number >= 97) or (number>=65 and number<=90) or(number>=48 and number<=57) or (number == 58):
                    output_data+=chr(number)
                elif number==32:
                    output_data+="space"
                else:
                    output_data+=str(number)

            else :
                #just print the combination, no treatment is needed
                output_data+=combinations[temp_string]
            output_data+='\n'
            temp_string=""
    except:
        #not a valid combination for now, pass
        pass
    i+=1


print output_data
with open('human_translated.txt','w') as f:
    f.write(output_data)
