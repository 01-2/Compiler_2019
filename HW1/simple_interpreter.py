from turtle import *
import sys

# Interpreter : Engine
def interpret(pgm):
	t = Turtle()
	current_instr = ''
	instr_set = ['F','L','R']
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
		process_instr(t, target)

	t.hideturtle()
	exitonclick()

def process_instr(t, instr):
	current_instr = instr[0]
	instr_val = int(instr[1:])

	# Process instruction
	if current_instr == 'F':
		t.forward(instr_val)
	elif current_instr == 'L':
		t.left(instr_val)
	elif current_instr == 'R':
		t.right(instr_val)
	else:
		print('[ERROR/PROCESS] near "{}"'.format(instr))
		return 0

	return 1

# Interpreter : Driver
if len(sys.argv) < 2:
	print('Usage: {} {}'.format(sys.argv[0], 'Koch_pgm'))
else:
	infile = open(sys.argv[1], 'r')
	pgm = infile.readline().strip()
	interpret(pgm)
	infile.close()

