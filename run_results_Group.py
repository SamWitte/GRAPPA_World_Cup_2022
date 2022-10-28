import numpy as np
import glob
import os
from master_group import *
input_dir = "input_files/"

point_per_order = 1
bonus_first = 1
bonus_all_in_group = 1

file_ini = glob.glob(input_dir + "*.dat")
final_results = []
for i in range(len(file_ini)):
    file1 = open(file_ini[i], 'r')
    Lines = file1.readlines()
    
    Point_Total = 0
    found_group = False
    for line in Lines:
        
        line_info = line.strip()
        get_chuncks = line_info.split(" ")
        if "Group" in get_chuncks:
            if len(get_chuncks[-1]) == 1:
                keyW_group = "Group " + get_chuncks[-1]
                found_group = True
                # print(keyW_group)
                count = 0
                group_points = 0
                continue
            elif len(get_chuncks[-1]) >= 3:
                print(f"ERROR: Group name is not correct in {file_ini[i]}")
        elif get_chuncks == [""]:
            continue
        
        if found_group:
            # print(count, get_chuncks[-1], master_dic[keyW_group][count])
            if get_chuncks[-1].lower() == master_dic[keyW_group][count].lower():
                group_points += point_per_order
                if count == 0:
                    group_points += bonus_first
            
            if count == 3:
                # group done
                if group_points == 4*point_per_order + bonus_first:
                    group_points += bonus_all_in_group # bonus points for all in group
                found_group = False
                Point_Total += group_points
            count += 1
            
            
    final_results.append([file_ini[i][len(input_dir):-4], Point_Total])


for i in range(len(file_ini)):
    print(final_results[i])
