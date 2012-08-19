from __future__ import print_function
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
    #PrintSequence( allnumbers )
    print(allnumbers)

def IsHappy(number, iteration, allnumbers):
    if number in allnumbers:
	allnumbers.append(number)
	return False
    allnumbers.append(number)
    if number == 1:
	return True
    if number == 0:
	return False
    characters = str(number)
    aux = 0
    for c in characters:
	newnumber = int(pow(int(c), 2))
        aux += newnumber
    return IsHappy(aux, iteration+1, allnumbers)

def PrintSequence( sequence ):
    for i in range(len(sequence)):
	number = sequence[i]
	msg = ''
	if i < len(sequence)-1:
	    msg = str(number) + " -> "
	else:
	    msg = str(number)
	print( msg, end='' )
    print()

if __name__ == "__main__":
    main()
