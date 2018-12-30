from threeTapeTuringMachine import Tape, TuringMachine
from transition import TransitionThreeTape
from tape import State, StateType, Direction
def main():
    st1 = '1'
    st2 = '10'
    tape1 = Tape(st1+ 'p'+ st2,'01p')
    tape2 = Tape('', '01p')
    tape3 = Tape('', '01p')
    states = [
    State('q0', StateType.Start),
    State('q1', StateType.Empty),
    State('q2', StateType.Empty),
    State('q3', StateType.Empty),
    State('q4', StateType.Empty),
    State('q5', StateType.Empty),
    State('q6', StateType.Empty),
    State('q7', StateType.Empty),
    State('q8', StateType.Empty),
    State('q9', StateType.Empty),
    State('q10', StateType.Accept),
    State('q11', StateType.Reject)
    ]
    transitions = [
    TransitionThreeTape('q0','#','#','#','q0','#','#','#',Direction.Right,Direction.Right,Direction.Right),        
	TransitionThreeTape('q0','0','#','#','q0','0','#','#',Direction.Right,Direction.Neutral,Direction.Neutral),
	TransitionThreeTape('q0','1','#','#','q0','1','#','#',Direction.Right,Direction.Neutral,Direction.Neutral),
	TransitionThreeTape('q0','p','#','#','q1','#','#','#',Direction.Right,Direction.Neutral,Direction.Neutral),
	TransitionThreeTape('q1','0','#','#','q1','#','0','#',Direction.Right,Direction.Right,Direction.Neutral),
	TransitionThreeTape('q1','1','#','#','q1','#','1','#',Direction.Right,Direction.Right,Direction.Neutral),
	TransitionThreeTape('q1','#','#','#','q2','#','#','#',Direction.Left,Direction.Neutral,Direction.Neutral),
	TransitionThreeTape('q2','#','#','#','q2','#','#','#',Direction.Left,Direction.Neutral,Direction.Neutral),
	TransitionThreeTape('q2','0','#','#','q3','0','#','#',Direction.Neutral,Direction.Neutral,Direction.Neutral),
	TransitionThreeTape('q2','1','#','#','q3','1','#','#',Direction.Neutral,Direction.Neutral,Direction.Neutral),
	TransitionThreeTape('q3','0','#','#','q4','0','#','#',Direction.Neutral,Direction.Neutral,Direction.Neutral),
	TransitionThreeTape('q3','1','#','#','q5','1','#','#',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q3','#','#','#','q6','#','#','#',Direction.Right,Direction.Neutral,Direction.Neutral),
	TransitionThreeTape('q4','0','#','#','q3','0','0','#',Direction.Left,Direction.Right,Direction.Neutral),
	TransitionThreeTape('q4','1','#','#','q3','1','0','#',Direction.Left,Direction.Right,Direction.Neutral),
	TransitionThreeTape('q5','1','0','0','q5','1','0','0',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q5','1','0','1','q5','1','0','1',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q5','1','1','0','q5','1','1','1',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q5','1','1','1','q8','1','1','0',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q5','1','0','#','q5','1','0','0',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q5','1','1','#','q5','1','1','1',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q5','1','#','0','q5','1','#','0',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q5','1','#','1','q5','1','#','1',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q5','1','#','#','q7','1','#','#',Direction.Neutral,Direction.Right,Direction.Right),
	TransitionThreeTape('q8','1','1','1','q8','1','1','1',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q8','1','1','0','q8','1','1','0',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q8','1','0','1','q8','1','0','0',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q8','1','0','0','q5','1','0','1',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q8','1','0','#','q5','1','0','1',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q8','1','1','#','q8','1','1','0',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q8','1','#','0','q5','1','#','1',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q8','1','#','1','q8','1','#','0',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q8','1','#','#','q5','1','#','1',Direction.Neutral,Direction.Left,Direction.Left),
	TransitionThreeTape('q7','1','#','0','q7','1','#','0',Direction.Neutral,Direction.Right,Direction.Right),
	TransitionThreeTape('q7','1','#','1','q7','1','#','1',Direction.Neutral,Direction.Right,Direction.Right),
	TransitionThreeTape('q7','1','0','#','q7','1','0','#',Direction.Neutral,Direction.Right,Direction.Right),
	TransitionThreeTape('q7','1','1','#','q7','1','1','#',Direction.Neutral,Direction.Right,Direction.Right),
	TransitionThreeTape('q7','1','0','0','q7','1','0','0',Direction.Neutral,Direction.Right,Direction.Right),
	TransitionThreeTape('q7','1','0','1','q7','1','0','1',Direction.Neutral,Direction.Right,Direction.Right),
	TransitionThreeTape('q7','1','1','0','q7','1','1','0',Direction.Neutral,Direction.Right,Direction.Right),
	TransitionThreeTape('q7','1','1','1','q7','1','1','1',Direction.Neutral,Direction.Right,Direction.Right),
	TransitionThreeTape('q7','1','#','#','q4','1','#','#',Direction.Neutral,Direction.Neutral,Direction.Neutral),
	TransitionThreeTape('q6','0','#','#','q6','#','#','#',Direction.Right,Direction.Neutral,Direction.Neutral),
	TransitionThreeTape('q6','1','#','#','q6','#','#','#',Direction.Right,Direction.Neutral,Direction.Neutral),
	TransitionThreeTape('q6','#','#','#','q9','#','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','0','0','0','q9','0','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','0','0','1','q9','1','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','0','1','0','q9','0','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','0','1','1','q9','1','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','1','0','0','q9','0','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','1','0','1','q9','1','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','1','1','0','q9','0','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','1','1','1','q9','1','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','0','#','#','q9','#','#','#',Direction.Left,Direction.Neutral,Direction.Neutral),
	TransitionThreeTape('q9','1','#','#','q9','#','#','#',Direction.Left,Direction.Neutral,Direction.Neutral),
	TransitionThreeTape('q9','#','0','#','q9','#','#','#',Direction.Neutral,Direction.Left,Direction.Neutral),
	TransitionThreeTape('q9','#','1','#','q9','#','#','#',Direction.Neutral,Direction.Left,Direction.Neutral),
	TransitionThreeTape('q9','#','#','0','q9','0','#','#',Direction.Left,Direction.Neutral,Direction.Left),
	TransitionThreeTape('q9','#','#','1','q9','1','#','#',Direction.Left,Direction.Neutral,Direction.Left),
	TransitionThreeTape('q9','0','0','#','q9','#','#','#',Direction.Left,Direction.Left,Direction.Neutral),
	TransitionThreeTape('q9','0','1','#','q9','#','#','#',Direction.Left,Direction.Left,Direction.Neutral),
	TransitionThreeTape('q9','1','0','#','q9','#','#','#',Direction.Left,Direction.Left,Direction.Neutral),
	TransitionThreeTape('q9','1','1','#','q9','#','#','#',Direction.Left,Direction.Left,Direction.Neutral),
	TransitionThreeTape('q9','0','#','0','q9','0','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','1','#','0','q9','0','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','0','#','0','q9','0','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','0','#','1','q9','1','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','1','#','1','q9','1','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','#','0','0','q9','0','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','#','0','1','q9','1','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','#','1','0','q9','0','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','#','1','1','q9','1','#','#',Direction.Left,Direction.Left,Direction.Left),
	TransitionThreeTape('q9','#','#','#','q10','#','#','#',Direction.Neutral,Direction.Neutral,Direction.Neutral)
    ]
    tm = TuringMachine(states, transitions, tape1, tape2, tape3)
    print("\nThree-tape Turing machine simulates the multiplier in the arithmetic and logic unit in the computer.")
    tm.process3()
    print("\nFirst term:")
    print("\n"+st1)
    print("\nSecond term:")
    print("\n"+st2)
    print("\nResult:")
    print(tm.get_tape1())
if __name__ == '__main__':
    main()
