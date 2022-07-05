"""
                           ----------------------------------------
                           |          EE2703_ASSIGNMENT2          |
                           |          AYUSH RAJ                   |
                           |           EE20B019                   |
                           ---------------------------------------
"""
from sys import argv
from numpy import *
import cmath

circuit = '.circuit'
end = '.end'
AC='.ac'
Pi=3.14159265
if len(argv) != 2:
    print("enter one .netlist file at a time")
    exit()

try:
    with open(argv[1]) as file:
        lines_in_file = file.readlines()
        start = -1
        last = -2
        for line in lines_in_file:
            if circuit == line[:len(circuit)]:
                start = lines_in_file.index(line)
            elif end == line[:len(end)]:
                last= lines_in_file.index(line)
                break

        if start >= last:
            print("invalid circuit definition\n.cicuit should be defined before .end")
            exit()
        #function to analyze whether the circuit is ac or dc
        def circuit_type(lines_in_files):
            is_ac=0
            frequency=0.0


            for line in lines_in_files:
                if AC==line[:len(AC)]:
                    is_ac=1
                    frequency= 2.0*pi*float(line.split(' ')[2])
            return is_ac,frequency
        circuit_is_ac,frequency=circuit_type(lines_in_file)
        #frequecy given in thw circuit is taken as omega
        print("angular frequency is ",frequency)
        #function to solve dc circuit
        def solve_dc_circuit(lines_in_files, start, last):
            i = int(last) - 1

            t = i
            set_of_nodes = {"GND"}
            set_of_voltage = {"GND"}
            while i > start:
                line = lines_in_files[i]
                # line=line.strip('\n')
                remove_cmmnt = line.split('#')
                words_in_line = remove_cmmnt[0].strip('\n').split(' ')

                while '' in words_in_line:
                    words_in_line.remove('')
                # set formation of all the variables i.e nodes and current through voltage source
                if words_in_line[0][0] == ('V' or 'E' or 'H'):
                    set_of_voltage.add(words_in_line[0])

                set_of_nodes.add(words_in_line[1])
                set_of_nodes.add(words_in_line[2])
                i = i - 1
            i = t
            set_of_nodes = sorted(set_of_nodes)
            # print(set_of_nodes)
            list_of_nodes = list(set_of_nodes)
            # print(list_of_nodes)
            # list_of_nodes=sorted(list_of_nodes)

            list_of_voltage = list(set_of_voltage)
            list_of_voltage.remove("GND")
            # print(list_of_voltage)
            # list_of_voltage=list_of_voltage.sort()
            n = len(list_of_voltage) + len(list_of_nodes) # total no of variables
            # matrix B
            B = array([0.0 for u in range(n)])
            #matrix A
            matrix_of_element = [[0.0 for x in range(n)] for y in range(n)]
            # print(matrix_of_element)
            while i > start:
                line = lines_in_file[i]
                # line=line.strip('\n')
                remove_cmmnt = line.split('#')
                words_in_line = remove_cmmnt[0].strip('\n').split(' ')

                while '' in words_in_line:
                    words_in_line.remove('')
                #voltage source
                if words_in_line[0][0] == 'V':
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    index3 = len(list_of_nodes) + list_of_voltage.index(words_in_line[0])
                    # print((index3))
                    matrix_of_element[index3][index1] = 1.0
                    matrix_of_element[index3][index2] = -1.0
                    matrix_of_element[index1][index3] = +1.0
                    matrix_of_element[index2][index3] = -1.0
                    if words_in_line[3]=='dc':
                        B[index3] = (float(words_in_line[4]))
                    else:
                        B[index3] = (float(words_in_line[3]))
                #current source
                elif words_in_line[0][0] == 'I':
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    if words_in_line[3]=='dc':
                        B[index1] = float(words_in_line[3])
                        B[index2] = -float(words_in_line[3])
                    else:
                        B[index1] = float(words_in_line[3])
                        B[index2] = -float(words_in_line[3])
                #VCCS
                elif words_in_line[0][0] == 'G':
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    index3 = list_of_nodes.index(words_in_line[3])
                    index4 = list_of_nodes.index(words_in_line[4])
                    matrix_of_element[index1][index3] += float(words_in_line[5])
                    matrix_of_element[index1][index4] -= float(words_in_line[5])
                    matrix_of_element[index2][index3] -= float(words_in_line[5])
                    matrix_of_element[index2][index4] += float(words_in_line[5])
                #VCVS
                elif words_in_line[0][0] == 'E':
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    index3 = list_of_nodes.index(words_in_line[3])
                    index4 = list_of_nodes.index(words_in_line[4])
                    index5 = len(list_of_nodes) + list_of_voltage.index(words_in_line[0])
                    matrix_of_element[index1][index5] += 1.0
                    matrix_of_element[index2][index5] -= 1.0
                    matrix_of_element[index5][index3] -= float(words_in_line[5])
                    matrix_of_element[index5][index4] += float(words_in_line[5])
                    matrix_of_element[index5][index1] += 1.0
                    matrix_of_element[index5][index2] -= 1.0
                #cccs
                elif words_in_line[0][0] == 'F':
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    index4 = len(list_of_nodes) + list_of_voltage.index(words_in_line[3])
                    matrix_of_element[index1][index4] += float(words_in_line[4])
                    matrix_of_element[index2][index4] -= float(words_in_line[4])
                #ccvs
                elif words_in_line[0][0] == 'H':
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    index3 = len(list_of_nodes) + list_of_voltage.index(words_in_line[3])
                    index4 = len(list_of_nodes) + list_of_voltage.index(words_in_line[0])
                    matrix_of_element[index4][index1] += 1.0
                    matrix_of_element[index4][index2] -= 1.0
                    matrix_of_element[index4][index3] -= float(words_in_line[4])
                    matrix_of_element[index1][index4] += 1.0
                    matrix_of_element[index2][index4] -= 1.0
                #resistor
                else:
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    matrix_of_element[index1][index1] += (1 / (float(words_in_line[3])))
                    matrix_of_element[index1][index2] += -(1 / (float(words_in_line[3])))
                    matrix_of_element[index2][index2] += (1 / (float(words_in_line[3])))
                    matrix_of_element[index2][index1] += -(1 / (float(words_in_line[3])))
                i = i - 1
            GND_index = list_of_nodes.index("GND")
            # print(len(matrix_of_element))
            # print(GND_index)
            matrix_of_element[GND_index] = [0.0] * n
            matrix_of_element[GND_index][GND_index] = 1.0
            B[GND_index]=0.0

            return matrix_of_element, B, list_of_nodes, list_of_voltage
        #function to solve ac circuit
        def solve_ac_circuit(lines_in_file,start,last,frequency):
            i = int(last) - 1

            t = i
            set_of_nodes = {"GND"}
            set_of_voltage = {"GND"}
            while i > start:
                line = lines_in_file[i]
                # line=line.strip('\n')
                remove_cmmnt = line.split('#')
                words_in_line = remove_cmmnt[0].strip('\n').split(' ')

                while '' in words_in_line:
                    words_in_line.remove('')

                if words_in_line[0][0] == 'V' or words_in_line[0][0] == 'E'or words_in_line[0][0] == 'H':
                    set_of_voltage.add(words_in_line[0])

                set_of_nodes.add(words_in_line[1])
                set_of_nodes.add(words_in_line[2])
                i = i - 1
            i = t
            set_of_nodes = sorted(set_of_nodes)
            # print(set_of_nodes)
            list_of_nodes = list(set_of_nodes)
            # print(list_of_nodes)
            # list_of_nodes=sorted(list_of_nodes)

            list_of_voltage = list(set_of_voltage)
            list_of_voltage.remove("GND")
            # print(list_of_voltage)
            # list_of_voltage=list_of_voltage.sort()
            n = len(list_of_voltage) + len(list_of_nodes)
            B = array([0.0 for u in range(n)],dtype=complex)

            matrix_of_element = array([[0.0 for x in range(n)] for y in range(n)],dtype=complex)
            # print(matrix_of_element)
            while i > start:
                line = lines_in_file[i]
                # line=line.strip('\n')
                remove_cmmnt = line.split('#')
                words_in_line = remove_cmmnt[0].strip('\n').split(' ')

                while '' in words_in_line:
                    words_in_line.remove('')
                #voltage source
                if words_in_line[0][0] == 'V':
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    index3 = len(list_of_nodes) + list_of_voltage.index(words_in_line[0])
                    # print((index3))
                    matrix_of_element[index3][index1] = +1.0
                    matrix_of_element[index3][index2] = -1.0
                    matrix_of_element[index1][index3] = +1.0
                    matrix_of_element[index2][index3] = -1.0
                    if words_in_line[3]=='ac':
                        B[index3] = cmath.rect((float(words_in_line[4]))/2.0, (pi*float(words_in_line[5]))/180.0)
                        #divided by 2 bcs given value is peak to peakvalue
                    else:
                        B[index3]= float(words_in_line[4])
                #current source
                elif words_in_line[0][0] == 'I':
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    if words_in_line[3]=='ac':
                        B[index1] = cmath.rect((float(words_in_line[4]))/2.0, (pi*float(words_in_line[5]))/180.0)
                        B[index2] = -cmath.rect((float(words_in_line[4]))/2.0, (pi*float(words_in_line[5]))/180.0)
                    else:
                        B[index1]= float(words_in_line[4])
                        B[index2]= -float(words_in_line[4])
                #VCCS
                elif words_in_line[0][0] == 'G':
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    index3 = list_of_nodes.index(words_in_line[3])
                    index4 = list_of_nodes.index(words_in_line[4])
                    matrix_of_element[index1][index3] += float(words_in_line[5])
                    matrix_of_element[index1][index4] -= float(words_in_line[5])
                    matrix_of_element[index2][index3] -= float(words_in_line[5])
                    matrix_of_element[index2][index4] += float(words_in_line[5])
                #VCVS
                elif words_in_line[0][0] == 'E':
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    index3 = list_of_nodes.index(words_in_line[3])
                    index4 = list_of_nodes.index(words_in_line[4])
                    index5 = len(list_of_nodes) + list_of_voltage.index(words_in_line[0])
                    matrix_of_element[index1][index5] += 1.0
                    matrix_of_element[index2][index5] -= 1.0
                    matrix_of_element[index5][index3] -= float(words_in_line[5])
                    matrix_of_element[index5][index4] += float(words_in_line[5])
                    matrix_of_element[index5][index1] += 1.0
                    matrix_of_element[index5][index2] -= 1.0
                #CCCS
                elif words_in_line[0][0] == 'F':
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    index4 = len(list_of_nodes) + list_of_voltage.index(words_in_line[3])
                    matrix_of_element[index1][index4] += float(words_in_line[4])
                    matrix_of_element[index2][index4] -= float(words_in_line[4])
                #CCVS
                elif words_in_line[0][0] == 'H':
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    index3 = len(list_of_nodes) + list_of_voltage.index(words_in_line[3])
                    index4 = len(list_of_nodes) + list_of_voltage.index(words_in_line[0])
                    matrix_of_element[index4][index1] += 1.0
                    matrix_of_element[index4][index2] -= 1.0
                    matrix_of_element[index4][index3] -= float(words_in_line[4])
                    matrix_of_element[index1][index4] += 1.0
                    matrix_of_element[index2][index4] -= 1.0
                #CAPACITOR
                elif words_in_line[0][0]=='C':
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    matrix_of_element[index1][index1] += complex(0, float(float(frequency)*(float(words_in_line[3]))))
                    matrix_of_element[index1][index2] += -complex(0, float(float(frequency)*(float(words_in_line[3]))))
                    matrix_of_element[index2][index2] += complex(0, float(float(frequency)*(float(words_in_line[3]))))
                    matrix_of_element[index2][index1] += -complex(0, float(float(frequency)*(float(words_in_line[3]))))
                #INDUCTOR
                elif words_in_line[0][0]=='L':
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    matrix_of_element[index1][index1] += complex(0,-(1/float(float(frequency)*(float(words_in_line[3])))))
                    matrix_of_element[index1][index2] += -complex(0,-(1/float(float(frequency)*(float(words_in_line[3])))))
                    matrix_of_element[index2][index2] += complex(0,-(1/float(float(frequency)*(float(words_in_line[3])))))
                    matrix_of_element[index2][index1] += -complex(0,-(1/float(float(frequency)*(float(words_in_line[3])))))
                #RESISTOR
                else:
                    index1 = list_of_nodes.index(words_in_line[1])
                    index2 = list_of_nodes.index(words_in_line[2])
                    matrix_of_element[index1][index1] += (1 / (float(words_in_line[3])))
                    matrix_of_element[index1][index2] += -(1 / (float(words_in_line[3])))
                    matrix_of_element[index2][index2] += (1 / (float(words_in_line[3])))
                    matrix_of_element[index2][index1] += -(1 / (float(words_in_line[3])))
                i = i - 1
            GND_index = list_of_nodes.index("GND")
            # print(len(matrix_of_element))
            # print(GND_index)
            matrix_of_element[GND_index] = [0.0] * n
            matrix_of_element[GND_index][GND_index] = 1.0
            B[GND_index]=0.0

            return matrix_of_element, B, list_of_nodes, list_of_voltage
        #display function to print solution
        def display_solution(solution,list_of_node,list_of_current):
            i=0
            print("the voltage of GND is 0")
            while i<len(list_of_node):
                if list_of_node[i]!="GND":
                    print("the voltage of node ",list_of_node[i]," is ",solution[i])
                i+=1
            j=len(list_of_node)
            k=len(list_of_node)
            while j<len(solution):
                print("the current across ",list_of_current[j-k]," is ",solution[j])
                j=j+1

        if circuit_is_ac ==1:
            matrix_of_elements, B, list_of_node, list_of_current = solve_ac_circuit(lines_in_file, start, last,frequency)
        else:
            matrix_of_elements, B, list_of_node, list_of_current = solve_dc_circuit(lines_in_file, start, last)
        # print(matrix_of_elements,end="\n")
        solution = linalg.solve(matrix_of_elements, B)
        # print(B)
        print("matrix A is \n",matrix_of_elements)
        print("matrix B is \n",B)
        #print("list of variable \n",list_of_node+list_of_current)
        # print(solution)
        display_solution(solution,list_of_node,list_of_current)
        # print(cmath.polar(solution[4]))
        # print(cmath.polar(solution[5]))
except IOError:
    print("Invalid File")
    exit()
