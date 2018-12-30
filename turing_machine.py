from transition import Transition, TransitionTwoTape, TransitionThreeTape
from tape import Tape, State, StateType, Direction

class TuringMachine:
    def __init__(self, states, transitions, tape1 = None, tape2 = None, tape3 =None, current_state = None):
        self.states = states
        self.start_state = self.get_start_state()
        self.transitions = transitions
        self.tape1 = tape1
        self.tape2 = tape2
        self.tape3 = tape3
        self.current_state = current_state

    def get_tape1(self):
        return self.tape1.get_tape()

    def get_tape2(self):
        return self.tape2.get_tape()

    def get_tape3(self):
        return self.tape3.get_tape()

    def get_start_state(self):
        return next(state for state in self.states if state.type == StateType.Start)

    def process1(self):
        try:
            current_state = self.start_state
    
            while current_state.type != StateType.Accept or current_state.type != StateType.Reject:
                current_char = self.tape1.read()
                state_id = current_state.id
    
                transition = next(t for t in self.transitions
                                  if t.current_state == state_id
                                  and t.current_char == current_char)
    
                current_state = next(state for state in self.states if state.id == transition.new_state)
    
                self.tape1.write(transition.new_char)
                self.tape1.move_head(transition.direction)
                self.current_state = current_state
        except StopIteration:
            self.current_state = current_state
        

    def process2(self):
        try:
            current_state = self.start_state
    
            while current_state.type != StateType.Accept or current_state.type != StateType.Reject:
                current_char1 = self.tape1.read()
                current_char2 = self.tape2.read()
                state_id = current_state.id
    
                transition = next(t for t in self.transitions
                                  if t.current_state == state_id
                                  and t.current_char1 == current_char1
                                  and t.current_char2 == current_char2)
    
                current_state = next(state for state in self.states if state.id == transition.new_state)
    
                self.tape1.write(transition.new_char1)
                self.tape1.move_head(transition.direction1)
                self.tape2.write(transition.new_char2)
                self.tape2.move_head(transition.direction2)
                self.current_state = current_state
        except StopIteration:
            self.current_state = current_state

    def process3(self):
        try:
            current_state = self.start_state
    
            while current_state.type != StateType.Accept or current_state.type != StateType.Reject:
                current_char1 = self.tape1.read()
                current_char2 = self.tape2.read()
                current_char3 = self.tape3.read()
                state_id = current_state.id
    
                transition = next(t for t in self.transitions
                                  if t.current_state == state_id
                                  and t.current_char1 == current_char1
                                  and t.current_char2 == current_char2
                                  and t.current_char3 == current_char3)
    
                current_state = next(state for state in self.states if state.id == transition.new_state)
    
                self.tape1.write(transition.new_char1)
                self.tape1.move_head(transition.direction1)
                self.tape2.write(transition.new_char2)
                self.tape2.move_head(transition.direction2)
                self.tape3.write(transition.new_char3)
                self.tape3.move_head(transition.direction3)
                self.current_state = current_state
        except StopIteration:
            self.current_state = current_state        
        pass
def main1():
    print("\nTuring machine recognizes whether or not the number of 0s is a power of 2.")
    st = '0000000000000000000000'
    tape1 = Tape(st,'0x')
    print("\nInput string:")
    print(st)
    states = [
    State('q1', StateType.Start),
    State('q2', StateType.Empty),
    State('q3', StateType.Empty),
    State('q4', StateType.Empty),
    State('q5', StateType.Empty),
    State('qa', StateType.Accept),
    State('qr', StateType.Reject)
    ]
    transitions = [
    Transition('q1', '$', 'q1', '$', Direction.Right),
    Transition('q1', '0', 'q2', '#', Direction.Right),
    Transition('q1', '#', 'qr', '#', Direction.Right),
    Transition('q1', 'x', 'qr', 'x', Direction.Right),
    Transition('q2', 'x', 'q2', 'x', Direction.Right),
    Transition('q2', '#', 'qa', '#', Direction.Right),
    Transition('q2', '0', 'q3', 'x', Direction.Right),
    Transition('q3', 'x', 'q3', 'x', Direction.Right),
    Transition('q3', '#', 'q5', '#', Direction.Left),
    Transition('q3', '0', 'q4', '0', Direction.Right),
    Transition('q4', '0', 'q3', 'x', Direction.Right),
    Transition('q4', 'x', 'q4', 'x', Direction.Right),
    Transition('q4', '#', 'qr', '#', Direction.Right),
    Transition('q5', '#', 'q2', '#', Direction.Right),
    Transition('q5', '0', 'q5', '0', Direction.Left),
    Transition('q5', 'x', 'q5', 'x', Direction.Left)
    ]
    tm = TuringMachine(states, transitions, tape1)
    tm.process1()
    if (tm.current_state.type == StateType.Accept):
        print('\nAccepting')
    if (tm.current_state.type == StateType.Reject):
        print('\nRejecting')
    pass


if __name__ == '__main__':
    main1()
