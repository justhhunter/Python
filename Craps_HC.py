# Hunter Copening
# 6/8/2022


# Craps Game Program


# This program will play one million games of craps and keep track of number of losses and wins
# It will also display percentages of wins and losses 



import random

def roll_dice():
    # rolls dice and returns as tuple

    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    return (die1, die2) # packs values into tuple

# intialize values and dictionaries
totalgames = 0


total_wins = {'win' : 0}
total_losses = {'loss' : 0}
win = {1:0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0, 15 : 0, 16 : 0, 17 : 0, 18 : 0, 19 : 0, 20 : 0, 21 : 0, 22 : 0, 23 : 0, 24 : 0, 25 : 0} 
lose = {1:0, 2 : 0, 3 : 0, 4 : 0, 5 : 0, 6 : 0, 7 : 0, 8 : 0, 9 : 0, 10 : 0, 11 : 0, 12 : 0, 13 : 0, 14 : 0, 15 : 0, 16 : 0, 17 : 0, 18 : 0, 19 : 0, 20 : 0, 21 : 0, 22 : 0, 23 : 0, 24 : 0, 25 : 0} 




# keeps programming repeating until statement true
while totalgames != 1000000:
    
    # initiates first roll
    die_values = roll_dice() 
    
    # remembers number of rolls
    totalgames += 1

    # determine game status and point, based on first roll
    sum_of_dice = sum(die_values)
    CONTINUED_rollcounter = 0
    rollcount = 0

    if sum_of_dice in (7, 11): # win
        total_wins['win'] += 1
        game_status = 'WON'
        # remembers number of wins
        
        
        # adds win roll to wins dictionary
        if game_status == 'WON':
            win[1] += 1
            

    elif sum_of_dice in (2, 3, 12): # lose
        total_losses['loss'] += 1
        game_status = 'LOST'
        
        
        
        # adds loss roll to losses dictionary
        if game_status == 'LOST':
            lose[1] += 1
            

    else: # remember point and start new counter
        game_status = 'CONTINUE'
        my_point = sum_of_dice
        CONTINUED_rollcounter = 1



   
    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        
        
            
        die_values = roll_dice()
            
        sum_of_dice = sum(die_values)
        CONTINUED_rollcounter = CONTINUED_rollcounter + 1
        if sum_of_dice == my_point: # win by making point
            game_status = 'WIN'
            total_wins['win'] += 1
            if game_status == 'WIN':
                if CONTINUED_rollcounter <= 25:
                    win[CONTINUED_rollcounter] += 1
                    



        elif sum_of_dice == 7: # lose by rolling 7
            game_status = 'LOSE'
            total_losses['loss'] += 1
            if game_status == 'LOSE':
                if CONTINUED_rollcounter <= 25:
                    lose[CONTINUED_rollcounter] += 1

# prints out percetage of wins at 1 roll

if totalgames == 1000000:
    # this will print the results in percentage form
    win_percent = total_wins['win']/1000000
    lose_percent = total_losses['loss']/1000000
    R1 = (win[1] + lose[1])/1000000
    R2 = (win[2] + lose[2])/1000000
    R3 = (win[3] + lose[3])/1000000
    R4 = (win[4] + lose[4])/1000000
    R5 = (win[5] + lose[5])/1000000
    R6 = (win[6] + lose[6])/1000000
    R7 = (win[7] + lose[7])/1000000
    R8 = (win[8] + lose[8])/1000000
    R9 = (win[9] + lose[9])/1000000
    R10 = (win[10] + lose[10])/1000000
    R11 = (win[11] + lose[11])/1000000
    R12 = (win[12] + lose[12])/1000000
    R13 = (win[13] + lose[13])/1000000
    R14 = (win[14] + lose[14])/1000000
    R15 = (win[15] + lose[15])/1000000
    R16 = (win[16] + lose[16])/1000000
    R17 = (win[17] + lose[17])/1000000
    R18 = (win[18] + lose[18])/1000000
    R19 = (win[19] + lose[19])/1000000
    R20 = (win[20] + lose[20])/1000000
    R21 = (win[21] + lose[21])/1000000
    R22 = (win[22] + lose[22])/1000000
    R23 = (win[23] + lose[23])/1000000
    R24 = (win[24] + lose[24])/1000000
    R25 = (win[25] + lose[25])/1000000

    C2 = R1 + R2
    C3 = C2 + R3
    C4 = C3 + R4
    C5 = C4 + R5
    C6 = C5 + R6
    C7 = C6 + R7
    C8 = C7 + R8
    C9 = C8 + R9
    C10 = C9 + R10
    C11 = C10 + R11
    C12 = C11 + R12
    C13 = C12 + R13
    C14 = C13 + R14
    C15 = C14 + R15
    C16 = C15 + R16
    C17 = C16 + R17
    C18 = C17 + R18
    C19 = C18 + R19
    C20 = C19 + R20
    C21 = C20 + R21
    C22 = C21 + R22
    C23 = C22 + R23
    C24 = C23 + R24
    C25 = C24 + R25

    print("""
            % Resolved              Cumulative %
Rolls       On this roll            of games resolved           Percentage of wins:  """,format(win_percent, '.2%'),""" Percentage of losses:""",format(lose_percent, '.2%'),"""
1          """,format(R1, '.2%'),"""                 """,format(R1, '.2%'),"""
2          """,format(R2, '.2%'),"""                 """,format(C2, '.2%'),"""
3          """,format(R3, '.2%'),"""                 """,format(C3, '.2%'),"""
4          """,format(R4, '.2%'),"""                 """,format(C4, '.2%'),"""
5          """,format(R5, '.2%'),"""                 """,format(C5, '.2%'),"""
6          """,format(R6, '.2%'),"""                 """,format(C6, '.2%'),"""
7          """,format(R7, '.2%'),"""                 """,format(C7, '.2%'),"""
8          """,format(R8, '.2%'),"""                 """,format(C8, '.2%'),"""
9          """,format(R9, '.2%'),"""                 """,format(C9, '.2%'),"""
10         """,format(R10, '.2%'),"""                 """,format(C10, '.2%'),"""
11         """,format(R11, '.2%'),"""                 """,format(C11, '.2%'),"""
12         """,format(R12, '.2%'),"""                 """,format(C12, '.2%'),"""
13         """,format(R13, '.2%'),"""                 """,format(C13, '.2%'),"""
14         """,format(R14, '.2%'),"""                 """,format(C14, '.2%'),"""
15         """,format(R15, '.2%'),"""                 """,format(C15, '.2%'),"""
16         """,format(R16, '.2%'),"""                 """,format(C16, '.2%'),"""
17         """,format(R17, '.2%'),"""                 """,format(C17, '.2%'),"""
18         """,format(R18, '.2%'),"""                 """,format(C18, '.2%'),"""
19         """,format(R19, '.2%'),"""                 """,format(C19, '.2%'),"""
20         """,format(R20, '.2%'),"""                 """,format(C20, '.2%'),"""
21         """,format(R21, '.2%'),"""                 """,format(C21, '.2%'),"""
22         """,format(R22, '.2%'),"""                 """,format(C22, '.2%'),"""
23         """,format(R23, '.2%'),"""                 """,format(C23, '.2%'),"""
24         """,format(R24, '.2%'),"""                 """,format(C24, '.2%'),"""
25         """,format(R25, '.2%'),"""                 """,format(C25, '.2%'),"""
""")