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
    n = is_happy(number, allnumbers)
    print(n)
    print_sequence(allnumbers) 
    #print(allnumbers)

def is_happy(number, allnumbers):
    if number in allnumbers:
	allnumbers.append(number)
	return False
    allnumbers.append(number)
    if number == 1:
	return True
    if number == 0:
	return False
    characters = str(number)
    newnumber = 0
    for c in characters:
	partial = int(pow(int(c), 2))
        newnumber += partial
    return is_happy(newnumber, allnumbers)

def print_sequence( sequence ):
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
