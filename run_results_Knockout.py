import numpy as np
import glob
import os
from master_knockout import *
input_dir = "GRAPPA_Knockout/"

point_scheme = [3, 6, 12, 24]
rounds = ["Round 1", "Quaters", "Semis", "Final"]

def point_assign(gameN):
    if gameN <= 8:
        return 3
    elif gameN <= 12:
        return 6
    elif gameN <= 14:
        return 12
    elif gameN == 15:
        return 24
    else:
        print("what the hell??")

file_ini = glob.glob(input_dir + "*.dat")
final_results = []
for i in range(len(file_ini)):
    file1 = open(file_ini[i], 'r')
    Lines = file1.readlines()
    
    Point_Total = 0
    game_counter = 0
    found_game = False
    done_intro = False
    for line in Lines:
        
        line_info = line.strip()
        get_chuncks = line_info.split(" ")
        
        if ("Round" in get_chuncks) and ("1" in get_chuncks):
            done_intro = True
            continue
        if not done_intro:
            continue
        
        if "Game" in get_chuncks:
            found_game = True
            game_counter += 1
            continue
        
        if found_game:
            found_game = False
            masterK = "Game {:d}".format(game_counter)
            if get_chuncks[0].lower() == master_dic[masterK].lower():
                Point_Total += point_assign(game_counter)
            else:
                continue
        
            
    final_results.append([file_ini[i][len(input_dir):-4], Point_Total])

def Sort(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li
    
final_results_sort = Sort(final_results)[::-1]
for i in range(len(file_ini)):
    print(final_results_sort[i])
