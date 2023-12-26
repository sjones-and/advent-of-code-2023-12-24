#!/usr/bin/env python3

import os
from time import perf_counter_ns
from itertools import combinations

class Equation:
    def __init__(self, data):
        position, velocity = map(lambda x: x.strip(), data.split('@'))
        self.px, self.py, _ = map(lambda x: int(x.strip()), position.split(','))
        self.vx, self.vy, _ = map(lambda x: int(x.strip()), velocity.split(','))
        self.gradient = self.vy / self.vx
        self.y_intercept = self.py - (self.gradient * self.px)

    def __repr__(self):
        return f'y = {self.y_intercept} {"-" if self.gradient < 0 else "+"} {abs(self.gradient)} x'
    
    def position_in_future(self, fx, fy):
        if self.px != fx:
            intersect_direction = (fx - self.px) / abs(fx - self.px)
            future_direction = self.vx / abs(self.vx)
        elif self.py != fy:
            intersect_direction = (fy - self.py) / abs(fy - self.py)
            future_direction = self.vy / abs(self.vy)
        return intersect_direction == future_direction

    def intersect_with(self, equation):
        if equation.gradient == self.gradient:
            return None
        x_intersect = (self.y_intercept - equation.y_intercept) / (equation.gradient - self.gradient)
        y_intersect = self.y_intercept + (self.gradient * x_intersect)
        intersect_in_future = self.position_in_future(x_intersect, y_intersect) and equation.position_in_future(x_intersect, y_intersect)
        return (x_intersect, y_intersect, intersect_in_future)

def answer(input_file):
    start = perf_counter_ns()
    with open(input_file, 'r') as input:
        equations = [Equation(data) for data in input.read().split('\n')]

    test_area = (200000000000000, 400000000000000)
    intersections = [combi[0].intersect_with(combi[1]) for combi in combinations(equations, 2)]
    intersections = [(intersection[0], intersection[1]) for intersection in intersections if intersection and intersection[2] and test_area[0] <= intersection[0] <= test_area[1] and test_area[0] <= intersection[1] <= test_area[1]]

    answer = len(intersections)
    end = perf_counter_ns()

    print(f'The answer is: {answer}')
    print(f'{((end-start)/1000000):.2f} milliseconds')

input_file = os.path.join(os.path.dirname(__file__), 'input')
answer(input_file)
