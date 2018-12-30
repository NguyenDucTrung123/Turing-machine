from transition import TransitionTwoTape
from tape import Tape, State, StateType, Direction
from turing_machine import TuringMachine
def main2():
    tape1 = Tape('101011','01')
    tape2 = Tape('','01')
    states = [
    State('qCopy', StateType.Start),
    State('qReturn', StateType.Empty),
    State('qTest', StateType.Empty),
    State('qa', StateType.Accept),
    State('qr', StateType.Reject)
    ]
    transitions = [
    TransitionTwoTape('qCopy', '$', '$', 'qCopy', '$', '$', Direction.Right, Direction.Right),
    TransitionTwoTape('qCopy', '0', '#', 'qCopy', '0', '0', Direction.Right, Direction.Right),
    TransitionTwoTape('qCopy', '1', '#', 'qCopy', '1', '1', Direction.Right, Direction.Right),
    TransitionTwoTape('qCopy', '#', '#', 'qReturn', '#', '#', Direction.Neutral, Direction.Left),
    TransitionTwoTape('qReturn', '#', '0', 'qReturn', '#', '0', Direction.Neutral, Direction.Left),
    TransitionTwoTape('qReturn', '#', '1', 'qReturn', '#', '1', Direction.Neutral, Direction.Left),
    TransitionTwoTape('qReturn', '#', '$', 'qTest', '#', '$', Direction.Left, Direction.Right),
    TransitionTwoTape('qTest', '0', '0', 'qTest', '0', '0', Direction.Left, Direction.Right),
    TransitionTwoTape('qTest', '1', '1', 'qTest', '1', '1', Direction.Left, Direction.Right),
    TransitionTwoTape('qTest', '$', '#', 'qa', '$', '#', Direction.Neutral, Direction.Neutral),
    TransitionTwoTape('qTest', '1', '0', 'qr', '1', '0', Direction.Neutral, Direction.Neutral),
    TransitionTwoTape('qTest', '0', '1', 'qr', '0', '1', Direction.Neutral, Direction.Neutral)
    ]
    tm = TuringMachine(states, transitions, tape1, tape2)
    print("\nTwo-tape Turing machine recognizes whether a binary string is a palindrome.")
    tm.process2()
    print("\nInput string:")
    print(tm.get_tape1())
    if (tm.current_state.type == StateType.Accept):
        print('\nAccepting')
    if (tm.current_state.type == StateType.Reject):
        print('\nRejecting')
    pass

if __name__ == '__main__':
	main2()