# Compiler : Set-up Code
prologue = '''
from turtle import *
def main():
	t = Turtle()
'''

epilogue = '''
	t.hideturtle()
	turtle.exitonclick()
main()
'''

def translate(o, pgm):
	current_instr = ''
	instr_set = ['F', 'L', 'R']
	target_list = [ ]

	for instr in pgm:
		instr_len = len(current_instr)
		if(instr.isdigit()):
			if(0 == instr_len):
				print('[ERROR/ZERO+DIGIT] near "{}"'.format(instr))
				target_list.clear()
				return
			else:
				current_instr += instr
		else:
			if((0 != instr_len) and (instr in instr_set)):
				target_list.append(current_instr)
				current_instr = instr
			elif((0 == instr_len) and (instr in instr_set)):
				current_instr = instr
			else:
				print('[ERROR/ETC] near "{}"'.format(instr))
				target_list.clear()
				return
	
	if(0 != len(current_instr)):
		target_list.append(current_instr)
	
	for target in target_list:
		o.write(process_instr(target))

def process_instr(instr):
	current_instr = instr[0]
	instr_val = int(instr[1:])

	# Process instruction
	if current_instr == 'F':
		return '	t.forward(' + str(instr_val) + ')\n'
	elif current_instr == 'L':
		return '	t.left(' + str(instr_val) + ')\n'
	elif current_instr == 'R':
		return '	t.right(' + str(instr_val) + ')\n'
	else:
		print('[ERROR/PROCESS] near "{}"'.format(instr))
		return '0'

# Compiler : Driver
import sys
if len(sys.argv) < 2:
	print('Usage: {} {}'.format(sys.argv[0], 'Koch_pgm'))
else:
	ifile = open(sys.argv[1], 'r')
	ofile = open('a.py', 'w')
	pgm = ifile.readline().strip()
	ofile.write(prologue)
	translate(ofile, pgm)
	ofile.write(epilogue)
	ofile.close()
	ifile.close()

