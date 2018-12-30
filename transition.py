from tape import State
#3-tape Turing machine
class Transition:
    def __init__(self, current_state = None, current_char = None, new_state = None, new_char = None, direction = None):
        self.current_state = current_state
        self.current_char = current_char
        self.new_state = new_state
        self.new_char = new_char
        self.direction = direction
        pass
class TransitionTwoTape(object):
    def __init__(self, current_state = None, current_char1 = None, current_char2 = None, new_state = None, new_char1 = None, new_char2 = None, direction1 = None, direction2 = None):
        self.current_state = current_state
        self.current_char1 = current_char1
        self.current_char2 = current_char2
        self.new_state = new_state
        self.new_char1 = new_char1
        self.new_char2 = new_char2
        self.direction1 = direction1
        self.direction2 = direction2
        pass
class TransitionThreeTape(object):
    def __init__(self, current_state = None, current_char1 = None, current_char2 = None, current_char3 = None, new_state = None, new_char1 = None, new_char2 = None, new_char3 = None, direction1 = None, direction2 = None, direction3 = None):
        self.current_state = current_state
        self.current_char1 = current_char1
        self.current_char2 = current_char2
        self.current_char3 = current_char3
        self.new_state = new_state
        self.new_char1 = new_char1
        self.new_char2 = new_char2
        self.new_char3 = new_char3
        self.direction1 = direction1
        self.direction2 = direction2
        self.direction3 = direction3
        pass