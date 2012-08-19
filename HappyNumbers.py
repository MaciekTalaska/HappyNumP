import math
import sys
import getopt

def main(argv=None):
    if argv is None:
	argv = sys.argv
    if len(argv) < 2:
	print("no number has been specified. exiting...")
	sys.exit(-1)
    number = int(argv[1])
    allnumbers = list();
    n = IsHappy(number, 1, allnumbers)
    print(n)

def IsHappy(number, iteration, allnumbers):
    if number in allnumbers:
	print( str(number) + " already exists!" )
	print( "looped after " +str(iteration) + " iterations")
	print( "whole list: ")
	print(allnumbers)
	sys.exit(1)
    allnumbers.append(number)
    print("input: " + str(number))
    characters = str(number)
    aux = 0
    for c in characters:
	newnumber = int(pow(int(c), 2))
	print( str(c) + " -> " +str(newnumber))
        aux += newnumber
    if aux != 1:
	return IsHappy(aux, iteration+1, allnumbers)
    else:
        return aux

if __name__ == "__main__":
    main()
