#!/usr/bin/env python3

import os
from time import perf_counter_ns
import sympy as sym

class Equation:
    def __init__(self, data):
        position, velocity = map(lambda x: x.strip(), data.split('@'))
        self.px, self.py, self.pz = map(lambda x: int(x.strip()), position.split(','))
        self.vx, self.vy, self.vz = map(lambda x: int(x.strip()), velocity.split(','))

def answer(input_file):
    start = perf_counter_ns()
    with open(input_file, 'r') as input:
        equations = [Equation(data) for data in input.read().split('\n')]

    px1, py1, pz1, vx1, vy1, vz1 = equations[0].px, equations[0].py, equations[0].pz, equations[0].vx, equations[0].vy, equations[0].vz
    px2, py2, pz2, vx2, vy2, vz2 = equations[1].px, equations[1].py, equations[1].pz, equations[1].vx, equations[1].vy, equations[1].vz
    px3, py3, pz3, vx3, vy3, vz3 = equations[2].px, equations[2].py, equations[2].pz, equations[2].vx, equations[2].vy, equations[2].vz

    x,y,z,a,b,c,i,j,k = sym.symbols('x,y,z,a,b,c,i,j,k')
    # XYZ = Rock starting coords, ABC = Rock XYZ velocity; IJK = Intercept time for hailstone 1,2,3
    eq1 = sym.Eq(x+(i*a),px1 + (i*vx1))
    eq2 = sym.Eq(x+(j*a),px2 + (j*vx2))
    eq3 = sym.Eq(x+(k*a),px3 + (k*vx3))
    eq4 = sym.Eq(y+(i*b),py1 + (i*vy1))
    eq5 = sym.Eq(y+(j*b),py2 + (j*vy2))
    eq6 = sym.Eq(y+(k*b),py3 + (k*vy3))
    eq7 = sym.Eq(z+(i*c),pz1 + (i*vz1))
    eq8 = sym.Eq(z+(j*c),pz2 + (j*vz2))
    eq9 = sym.Eq(z+(k*c),pz3 + (k*vz3))
    result = sym.solve([eq1,eq2,eq3,eq4,eq5,eq6,eq7,eq8,eq9],(x,y,z,a,b,c,i,j,k))

    answer = result[0][0] + result[0][1] + result[0][2]
    end = perf_counter_ns()

    print(f'The answer is: {answer}')
    print(f'{((end-start)/1000000):.2f} milliseconds')

input_file = os.path.join(os.path.dirname(__file__), 'input')
answer(input_file)
