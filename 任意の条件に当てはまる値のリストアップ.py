# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:09:00 2020

@author: 戸田　康介
"""

#コメントにて、一つ求めるときと、複数求めるときを使い分け
#ball_pos_pre = copy.copy(ball_pos)    
#last_passcource_pre = copy.copy(last_passcource)
#first_freetime_1 = []
#last_freetime_1 = []
#first_freetime_2 = []
#last_freetime_2= []
#first_freetime_3 = []
#last_freetime_3= []
#first_freetime_4= []
#last_freetime_4 = []
first_passcource = []
last_passcource = []
start_passcource = []
#start_freetime_1 = None
#start_freetime_2 = None
#start_freetime_3 = None
#start_freetime_4 = None
for i in range(len(ball_pos)):
    if i != 0:
        if  ball_pos[i] != ball_pos[i-1] and start_freetime_1 != None:
            first_passcource.append(start_passcource)
#            if passcource_label_elsol1[i-1] == 0:
            last_passcource.append(passcource[i-1])
            start_passcource = None
        if  ball_pos[i] != 0 and start_passcource == None:
            start_passcource = passcource[i]
#        if  ball_pos[i] != ball_pos[i-1] and start_freetime_1 != None:
#            first_freetime_1.append(start_freetime_1)
##            if passcource_label_elsol1[i-1] == 0:
#            last_freetime_1.append(free_time_elsol1[i-1])
#            start_freetime_1 = None
#            first_freetime_2.append(start_freetime_2)
#            last_freetime_2.append(free_time_elsol2[i-1])
#            start_freetime_2 = None
#            first_freetime_3.append(start_freetime_3)
#            last_freetime_3.append(free_time_elsol3[i-1])
#            start_freetime_3= None
#            first_freetime_4.append(start_freetime_4)
#            last_freetime_4.append(free_time_elsol4[i-1])
#            start_freetime_4 = None
#        if  ball_pos[i] != 0 and start_freetime_1 == None:
#            start_freetime_1 = free_time_elsol1[i]
#            start_freetime_2= free_time_elsol2[i]
#            start_freetime_3 = free_time_elsol3[i]
#            start_freetime_4 = free_time_elsol4[i]
if start_passcource != None:
    last_passcource.append(free_time_elsol1[i])
#if start_freetime_1 != None:
#    last_freetime_1.append(free_time_elsol1[i])
#    last_freetime_2.append(free_time_elsol2[i])
#    last_freetime_3.append(free_time_elsol3[i])
#    last_freetime_4.append(free_time_elsol4[i])

            
