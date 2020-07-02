#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:32:12 2020

@author: michael
"""

class Position:
    
    def __init__(self, row, col):
        self.row = row
        self.col = col

class NQueenProblem:
    
    
    def solve(self, n):
        positions = [None] * n
        has_solution = self.solve_nqueen(n, 0, positions)
        if has_solution:
            return positions
        else:
            return None
        
    def solve_nqueen(self, n, row, positions):
        if n == row:
            return True
        
        for col in range(0, n):
            foundSafe = True
            # check if this row and col is not under attack from any previous queen.
            for queen in range(0, row):
                if (positions[queen].col == col
                    or positions[queen].row - positions[queen].col == row - col 
                    or positions[queen].row + positions[queen].col == row + col):
                    foundSafe = False
                    break
            
            if foundSafe:
                positions[row] = Position(row, col)
                if self.solve_nqueen(n, row + 1, positions):
                    return True        
        return False
                
    def show(self, positions):
        for p in positions:
            print(p.row, "-", p.col)
            
solver = NQueenProblem()
solver.show(solver.solve(8))