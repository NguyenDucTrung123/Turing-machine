#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 10:22:55 2018

@author: phamnhatduy
"""

import math
import re
import time
import numpy as np
from enum import Enum


class State:
    def __init__(self, id, state_type):
        self.id = id
        self.type = state_type
        
class StateType(Enum):
    Start = 1
    Final = 2
    Empty = 3

class Tape:
    def __init__(self, word, alphabet):
        self.alphabet = alphabet + "$#"
        self.__init_tape(word)
        self.head_position = 0

    def __init_tape(self, word):
        tape = "$";
        for char in (c for c in word if c in self.alphabet):
            tape += char
        tape += "#";
        self._tape = list(tape)

    def write(self, character):
        if self.head_position < 1 or character not in self.alphabet:
            return
        self._tape[self.head_position] = character

        last_item_index = len(self._tape) - 1
        if self.head_position == last_item_index:
            self._tape += '#'

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
        for i in range(len(self._tape) - 1, 1, -1):
            if self._tape[i] == '#' and self._tape[i-1] == '#':
                del self._tape[-1:]
            else:
                break

class Transition:
    def __init__(self, current_state, current_char, new_state, new_char, direction):
        self.current_state = current_state
        self.current_char = current_char
        self.new_state = new_state
        self.new_char = new_char
        self.direction = direction

class Direction(Enum):
    Left = 1
    Right = 2
    Neutral = 3
    
class TuringMachine:
    def __init__(self, states, transitions, tape, verbose=False):
        self.states = states
        self.start_state = self.get_start_state()
        self.transitions = transitions
        self.tape = tape
        self.verbose = verbose

    def get_tape(self):
        return self.tape.get_tape()

    def get_start_state(self):
        return next(state for state in self.states if state.type == StateType.Start)

    def process(self, verbose=False):
        current_state = self.start_state
        step = 0

        self._log_process(step)

        while current_state.type != StateType.Final:
            current_char = self.tape.read()
            state_id = current_state.id

            transition = next(t for t in self.transitions
                              if t.current_state == state_id
                              and t.current_char == current_char)

            current_state = next(state for state in self.states if state.id == transition.new_state)

            step += 1
            self.tape.write(transition.new_char)
            self.tape.move_head(transition.direction)
            self._log_process(step)

    def _log_process(self, step):
        if self.verbose is True:
            print('\nTape after step {0}: '.format(step))

            for i in range(0, self.tape.get_length()):
                if self.tape.head_position == i:
                    print("\033[4m" + self.tape._tape[i] + "\033[0m")
                else:
                    print(self.tape._tape[i])

            print(']')
g = { "1" : ["2", "3", "4"],
      "2" : ["1", "3"],
      "3" : ["1", "2"],
      "4" : ["1"]
}
class Graph(object):

    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({vertex, neighbour})
        return edges
    def is_connected(self, 
                     vertices_encountered = None, 
                     start_vertex=None):
        if vertices_encountered is None:
            vertices_encountered = set()
        gdict = self.__graph_dict        
        vertices = list(gdict.keys()) # "list" necessary in Python 3 
        if not start_vertex:
            # chosse a vertex from graph as a starting point
            start_vertex = vertices[0]
        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in gdict[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.is_connected(vertices_encountered, vertex):
                        return True
        else:
            return True
        return False
graph = Graph(g)
print(graph.is_connected())
        
            


    