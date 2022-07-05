"""
                           ----------------------------------------
                           |          EE2703_ASSIGNMENT1          |
                           |          AYUSH RAJ                   |
                           |           EE20B019                   |
                           ---------------------------------------
"""
from sys import argv


circuit='.circuit'
end='.end'

if len(argv)!=2:
    print("enter one .netlist file at a time")
    exit()

try:
    with open(argv[1]) as file:
        lines_in_file=file.readlines()
        start=-1
        last=-2
        for line in lines_in_file:
            if circuit==line[:len(circuit)]:
                start= lines_in_file.index(line)
            elif end==line[:len(end)]:
                  last=lines_in_file.index(line)
                  break

        if start>=last :
            print("invalid circuit definition\n.cicuit should be defined before .end")
            exit()

        i=int(last)-1
        while i>start:
            line=lines_in_file[i]
            #line=line.strip('\n')
            remove_cmmnt= line.split('#')
            words_in_line=remove_cmmnt[0].strip('\n').split(' ')

            for words in reversed(words_in_line):
                if words!='':
                    print(words, end=" ")
            print("\n")
            i=i-1
        # analyzing the circuit
        def analyze_circuit(line):
            remove_cmmnt = line.split('#')
            words_in_line = remove_cmmnt[0].strip('\n').split(' ')
            while '' in words_in_line:
                words_in_line.remove('')
            # if the circuit element is R,L,C,V,I
            if len(words_in_line)==4:
                element_name=words_in_line[0]
                from_node= words_in_line[1]
                to_node= words_in_line[2]
                value= words_in_line[3]
                print("the element name is %s . it is connected from node %s to node %s and its value is %s" %(element_name,from_node,to_node,value))
            #current controlled current source or voltage source
            elif len(words_in_line)==5:
                if words_in_line[0][0]=='F':
                    element_name = words_in_line[0]
                    from_node = words_in_line[1]
                    to_node = words_in_line[2]
                    source= words_in_line[3]
                    value = words_in_line[4]
                    print("a current source is connected from node %s to node %s that generates a current %s times the current flowing through the source%s" %(from_node,to_node,value,source))
                else:
                    element_name = words_in_line[0]
                    from_node = words_in_line[1]
                    to_node = words_in_line[2]
                    source = words_in_line[3]
                    value = words_in_line[4]
                    print("a voltage source is connected from node %s to node %s that generates a voltage %s times the current flowing through the source%s" % (from_node, to_node, value, source))
            #voltage controlled voltage source or current source
            elif len(words_in_line)==6:
                if words_in_line[0][0]=='E':
                    element_name = words_in_line[0]
                    from_node = words_in_line[1]
                    to_node = words_in_line[2]
                    source_node1= words_in_line[3]
                    source_node2= words_in_line[4]
                    value = words_in_line[5]
                    print("a voltage source is connected from node %s to node %s that generates a voltage %s times the voltage across the node %s and %s" %(from_node,to_node,value,source_node1,source_node2))
                else:
                    element_name = words_in_line[0]
                    from_node = words_in_line[1]
                    to_node = words_in_line[2]
                    source_node1 = words_in_line[3]
                    source_node2=words_in_line[4]
                    value = words_in_line[5]
                    print("a current source is connected from node %s to node %s that generates a current %s times the voltage across the node %s and %s" % (from_node, to_node, value, source_node1,source_node2))


            else:
                return []

        print("this is analyzation part of the circuit")
        k=int(start)+1
        while k<last:
            line=lines_in_file[k]
            analyze_circuit(line)
            k=k+1






except IOError:
    print("Invalid File")
    exit()



