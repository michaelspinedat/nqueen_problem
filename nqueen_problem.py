#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 22:32:12 2020

@author: michael
"""

import pygame, os

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()
pygame.display.set_caption("N queens problem")

iconPath = "images/icon.ico"

if os.path.exists(iconPath):
    icon = pygame.image.load(iconPath)    
    pygame.display.set_icon(icon)

width, height = 400, 400

screen = pygame.display.set_mode((height, width))

bg = 25, 25, 25
screen.fill(bg)
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
        self.draw(positions)
            
    def draw(self, positions):
        global width, height, screen, bg
        # cell dimensions
        n = len(positions)
        dimCW = width / n
        dimCH = height / n
        
        ended = False
        while not ended:
            screen.fill(bg)
            ev = pygame.event.get()
            
            for event in ev:
                if event.type == pygame.QUIT:
                    ended = True
                    break
                    
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:                        
                        ended = True
                
            for y in range(0, n):
                for x in range(0, n):
                    poly = [(x * dimCW, y * dimCH),
                            ((x + 1) * dimCW, y * dimCH),
                            ((x + 1) * dimCW, (y + 1) * dimCH),
                            (x * dimCW, (y + 1) * dimCH)                    
                            ]
                    if positions[y].col == x:
                        pygame.draw.polygon(screen, (128, 128, 128), poly, 0) 
                    else:
                        pygame.draw.polygon(screen, (0, 0, 0), poly, 1)
            
            pygame.display.update()
                

n = 15
solver = NQueenProblem()
solver.show(solver.solve(n))
pygame.quit()
