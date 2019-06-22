# -*- coding: utf-8 -*-
"""
Created on Sun May  5 11:47:14 2019

@author: vektorel
"""

def hanoi_tower_algorithm(n, x, y, z):
    if n == 1:
        print("Diski {} çubuğundan {} çubuğuna koy".format(x,z))
    else:
        hanoi_tower_algorithm(n-1, x, z, y)
        hanoi_tower_algorithm(1, x, y, z)
        hanoi_tower_algorithm(n-1, y, x, z)
        
def hanoi_tower_algorithm_main(ndisc):
    # ndisc = Number of Disc
    hanoi_tower_algorithm(ndisc, "1. Kule", "2. Kule", "3. Kule")

hanoi_tower_algorithm_main(4)
