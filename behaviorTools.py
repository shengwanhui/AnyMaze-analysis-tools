import os
import numpy as np

def discriminationIndex(df, msID):
    discrimIndex_all = []
    for ms in msID:
        if df['Safe side'][ms] == 'L':
            safe_duration = df['Left : time'][ms]
            danger_duration = df['Right : time'][ms]
        elif df['Safe side'][ms] == 'R':
            safe_duration = df['Right : time'][ms]
            danger_duration = df['Left : time'][ms]
        discrimIndex = round((safe_duration-danger_duration)/(safe_duration+danger_duration), 3)
        discrimIndex_all.append(discrimIndex)
    return discrimIndex_all

def discriminationIndexByInteraction(df, msID):
    discrimIndex_all = []
    for ms in msID:
        if df['Safe side'][ms] == 'L':
            safe_duration = df['Left - interaction : time pressed'][ms]
            danger_duration = df['Right - interaction : time pressed'][ms]
        elif df['Safe side'][ms] == 'R':
            safe_duration = df['Right - interaction : time pressed'][ms]
            danger_duration = df['Left - interaction : time pressed'][ms]
        discrimIndex = round((safe_duration-danger_duration)/(safe_duration+danger_duration), 3)
        discrimIndex_all.append(discrimIndex)
    return discrimIndex_all

def get3ChamberDuration(df, msIDs):
    safe_duration_all = []
    dangerous_duration_all = []
    mid_duration_all = []
    for ms in msIDs:
        if df['Safe side'][ms] == 'L':
            safe_duration = df['Left : time'][ms]
            danger_duration = df['Right : time'][ms]
        elif df['Safe side'][ms] == 'R':
            safe_duration = df['Right : time'][ms]
            danger_duration = df['Left : time'][ms]
        safe_duration_all.append(safe_duration)   
        dangerous_duration_all.append(danger_duration)
        mid_duration_all.append(df['Mid : time'][ms])
    return safe_duration_all, mid_duration_all, dangerous_duration_all


if __name__ == "__main__":
    raise Exception("this file must be imported, not run directly")