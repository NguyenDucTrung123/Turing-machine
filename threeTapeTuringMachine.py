from transition import TransitionThreeTape
from tape import State, StateType, Direction

class Tape:
    def __init__(self, word = None, alphabet = None):
        self.alphabet = alphabet + "#"        
        self.head_position = 0
        self.__init_tape(word)

    def __init_tape(self, word):
        tape = "#";
        for char in (c for c in word if c in self.alphabet):
            tape += char
        tape += "#";
        self._tape = list(tape)

    def write(self, character):
        if character not in self.alphabet:
            return
        self._tape[self.head_position] = character

        last_item_index = len(self._tape) - 1
        if self.head_position == last_item_index:
            self._tape += '#'
        if self.head_position == 0:
            self._tape.insert(0, '#')

    def read(self):
        if self.head_position < 0 or self.head_position > len(self._tape) - 1:
            raise Exception('Trying to read character at invalid position: ' + self.head_position)
        return self._tape[self.head_position]

    def get_tape(self):
        self._remove_trailing_sharps()
        return ''.join(self._tape)

    def move_head(self, direction):
        if direction == Direction.Right:
            self.head_position += 1
        elif direction == Direction.Left:
            self.head_position -= 1

        if self.head_position > len(self._tape) - 1:
            self._tape += '#'
        if self.head_position < 0:
            self.head_position = 0

    def get_length(self):
        return len(self._tape)

    def _remove_trailing_sharps(self):
        for i in range(0,len(self._tape) - 1):
            if self._tape[i] != '#':
                del self._tape[0:i]
                break
        for i in range(len(self._tape) - 1,-1,-1):
            if self._tape[i] != '#':
                del self._tape[i+1:]
                break
            
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
def main():
    tape1 = Tape('110101010010110p1101010101010101111','01p')
    tape2 = Tape('', '01p')
    tape3 = Tape('', '01p')
    states = [
    State('q0', StateType.Start),
    State('q1', StateType.Empty),
    State('q2', StateType.Empty),
    State('q3', StateType.Empty),
    State('q4', StateType.Empty),
    State('q5', StateType.Accept),
    State('q6', StateType.Reject)
    ]
    transitions = [
    TransitionThreeTape('q0','#','#','#','q0','#','#','#',Direction.Right,Direction.Right,Direction.Right),
    TransitionThreeTape('q0','0','#','#','q0','0','#','#',Direction.Right,Direction.Neutral,Direction.Neutral),
    TransitionThreeTape('q0','1','#','#','q0','1','#','#',Direction.Right,Direction.Neutral,Direction.Neutral),
    TransitionThreeTape('q0','p','#','#','q1','#','#','#',Direction.Right,Direction.Neutral,Direction.Neutral),
    TransitionThreeTape('q1','0','#','#','q1','#','0','#',Direction.Right,Direction.Right,Direction.Neutral),
    TransitionThreeTape('q1','1','#','#','q1','#','1','#',Direction.Right,Direction.Right,Direction.Neutral),
    TransitionThreeTape('q1','#','#','#','q2','#','#','#',Direction.Left,Direction.Left,Direction.Neutral),
    TransitionThreeTape('q2','#','0','#','q2','#','0','#',Direction.Left,Direction.Neutral,Direction.Neutral),
    TransitionThreeTape('q2','#','1','#','q2','#','1','#',Direction.Left,Direction.Neutral,Direction.Neutral),
    TransitionThreeTape('q2','1','0','#','q3','1','0','#',Direction.Neutral,Direction.Neutral,Direction.Neutral),
    TransitionThreeTape('q2','1','1','#','q3','1','1','#',Direction.Neutral,Direction.Neutral,Direction.Neutral),
    TransitionThreeTape('q2','0','1','#','q3','0','1','#',Direction.Neutral,Direction.Neutral,Direction.Neutral),
    TransitionThreeTape('q2','0','0','#','q3','0','0','#',Direction.Neutral,Direction.Neutral,Direction.Neutral),
    TransitionThreeTape('q3','1','0','#','q3','1','0','1',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q3','0','1','#','q3','0','1','1',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q3','0','0','#','q3','0','0','0',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q3','1','1','#','q4','1','1','0',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q3','#','#','#','q5','#','#','#',Direction.Neutral,Direction.Neutral,Direction.Neutral),
    TransitionThreeTape('q3','1','#','#','q3','1','#','1',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q3','0','#','#','q3','0','#','0',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q3','#','1','#','q3','#','1','1',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q3','#','0','#','q3','#','0','0',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q4','0','0','#','q3','0','0','1',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q4','0','1','#','q4','0','1','0',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q4','1','0','#','q4','1','0','0',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q4','1','1','#','q4','1','1','1',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q4','#','0','#','q3','#','0','1',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q4','#','1','#','q4','#','1','0',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q4','1','#','#','q4','1','#','0',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q4','0','#','#','q3','0','#','1',Direction.Left,Direction.Left,Direction.Left),
    TransitionThreeTape('q4','#','#','#','q5','#','#','1',Direction.Neutral,Direction.Neutral,Direction.Neutral)
    ]
    tm = TuringMachine(states, transitions, tape1, tape2, tape3)
    print("\nThree-tape Turing machine simulates the adder in the arithmetic and logic unit in the computer.")
    tm.process3()
    print("\nFirst term:")
    print(tm.get_tape1())
    print("\nSecond term:")
    print(tm.get_tape2())
    print("\nResult:")
    print(tm.get_tape3())
if __name__ == '__main__':
    main()
