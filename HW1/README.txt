1. 공통
	(1) 요구 환경 
		- Python 3 이상

	(2) 명령어 구조
		명령어와 숫자가 교대로 구성되는 구조
		[INSTRUCTION][NUMBER]
		
		INSTRUCTION
			F : 전진(Forward), F 이후 숫자는 전진하는 정도를 지시한다.
			    F100 -> forward(100)
			R : 우회전(turn Right), R 이후 숫자는 우회전 각도를 나타낸다.
			    R90 -> right(90)
			L : 좌회전(turn Left), L 이후 숫자는 좌회전 각도를 나타낸다.
			    L90 -> left(90)

		EX) 사각형 : F100L90F100L90F100L90F100
			forward(100)
			left(90)
			forward(100)
			left(90)
			forward(100)
			left(90)
			forward(100)

2. Interpreter
	python simple_interpreter.py [INPUT_FILE]
	Interpreter 명령을 실행하면, turtle 모듈이 명령어를 수행한다.
	turtle 창을 클릭하면 실행을 종료할 수 있다.

3. Compiler
	python simple_compiler.py [INPUT_FILE]
	컴파일러를 실행하면 결과물로 a.py 파일이 생성된다
	python a.py 명령를 통해 생성된 스크립트를 실행할 수 있다. 