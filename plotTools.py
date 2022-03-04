import matplotlib.pyplot as plt
import numpy as np
import os

def twoGroupBarPlot(data1, data2, data1_name, data2_name, yLabel):
    """
    Display two groups of values as bar plot (mean +-SE), plot individual data. 
    """

    test_group_mean = np.mean(data1)
    control_group_mean = np.mean(data2)
    test_group_SE = np.array(data1).std()/np.sqrt(len(data1))
    control_group_SE = np.array(data2).std()/np.sqrt(len(data2))

    fig, ax = plt.subplots(figsize=(4,6))

    plt.rcParams['font.size'] = '15'
    barWidth = 0.5
    barLoc = (0.5, 1.5)
    ax.bar(barLoc, (test_group_mean,control_group_mean), width=barWidth, color = ('indianred', 'royalblue'), 
           yerr = (test_group_SE, control_group_SE ),capsize = 12, tick_label = (data1_name, data2_name), alpha = 0.7)

    ax.set(xlim=(0, 2), ylim=(-1, 1))
    ax.set_xlabel('Groups', fontsize = 15)
    ax.set_ylabel(ylabel = yLabel, fontsize = 15)
    plt.axhline(y=0, color='black', linestyle='-')


    color = ('red', 'blue')
    y=(data1, data2)

    for i in range(len(barLoc)):
        ax.scatter(barLoc[i] + np.random.random(len(y[i])) * barWidth - barWidth / 2, y[i], color=color[i])

    #ax.scatter((0.5, 1.5), (test_group.values(), control_group.values()), s=2, c=('red', 'blue'), vmin=0, vmax=100)

    plt.show()

def threeGroupBarPlot(data1, data2, data3, data1_name, data2_name, data3_name, yLabel):
    """
    Display two groups of values as bar plot (mean +-SE), plot individual data. 
    """

    test_group_mean = np.mean(data1)
    control_group_mean = np.mean(data2)
    control2_group_mean = np.mean(data3)
    test_group_SE = np.array(data1).std()/np.sqrt(len(data1))
    control_group_SE = np.array(data2).std()/np.sqrt(len(data2))
    control2_group_SE = np.array(data3).std()/np.sqrt(len(data3))

    fig, ax = plt.subplots(figsize=(5,6))

    plt.rcParams['font.size'] = '15'
    barWidth = 0.5
    barLoc = (0.5, 1.5, 2.5)
    ax.bar(barLoc, (test_group_mean,control_group_mean, control2_group_mean ), width=barWidth, color = ('indianred', 'royalblue', 'grey'), 
           yerr = (test_group_SE, control_group_SE, control2_group_SE ),capsize = 12, tick_label = (data1_name, data2_name, data3_name), alpha = 0.7)

    ax.set(xlim=(0, 3), ylim=(-1, 1))
    ax.set_xlabel('Groups', fontsize = 15)
    ax.set_ylabel(ylabel = yLabel, fontsize = 15)
    plt.axhline(y=0, color='black', linestyle='-')


    color = ('red', 'blue', 'grey')
    y=(data1, data2, data3)

    for i in range(len(barLoc)):
        ax.scatter(barLoc[i] + np.random.random(len(y[i])) * barWidth - barWidth / 2, y[i], color=color[i])

    #ax.scatter((0.5, 1.5), (test_group.values(), control_group.values()), s=2, c=('red', 'blue'), vmin=0, vmax=100)

    plt.show()

def fourGroupBarPlot(y1, y2, y3, y4, y1_name, y2_name, y3_name, y4_name, yLabel):
    """
    Display two groups of values as bar plot (mean +-SE), plot individual data. 
    """

    y1_mean = np.mean(y1)
    y2_mean = np.mean(y2)
    y3_mean = np.mean(y3)
    y4_mean = np.mean(y4)
    y1_SE = np.array(y1).std()/np.sqrt(len(y1))
    y2_SE = np.array(y2).std()/np.sqrt(len(y2))
    y3_SE = np.array(y3).std()/np.sqrt(len(y3))
    y4_SE = np.array(y4).std()/np.sqrt(len(y4))



    fig, ax = plt.subplots(figsize=(6,6))

    plt.rcParams['font.size'] = '15'
    barWidth = 0.5
    barLoc = (0.5, 1.5, 2.5, 3.5)
    ax.bar(barLoc, (y1_mean,y2_mean, y3_mean, y4_mean), width=barWidth, color = ('indianred', 'royalblue', 'green','purple'), 
           yerr = (y1_SE, y2_SE, y3_SE, y4_SE),capsize = 12, tick_label = (y1_name, y2_name, y3_name, y4_name), alpha = 0.7)

    ax.set(xlim=(0, 4), ylim=(-1, 1))
    ax.set_xlabel('Groups', fontsize = 15)
    ax.set_ylabel(ylabel = yLabel, fontsize = 15)
    plt.axhline(y=0, color='black', linestyle='-')


    color = ('red', 'blue', 'green','purple')
    y=(y1, y2, y3, y4)

    for i in range(len(barLoc)):
        ax.scatter(barLoc[i] + np.random.random(len(y[i])) * barWidth - barWidth / 2, y[i], color=color[i])

    #ax.scatter((0.5, 1.5), (test_group.values(), control_group.values()), s=2, c=('red', 'blue'), vmin=0, vmax=100)

    plt.show()

def plot3ChamberDuration(ys1, ys2, ys3, ys1_name, ys2_name, ys3_name, ylabel, title):
    """
    Display three arrays of values as a connected scatter plot
    """
    plt.figure(figsize=(4, 5))
    for i in range(len(ys1)):
        plt.plot(1, ys1[i], 'b.', ms=10)
        plt.plot(2, ys2[i], 'b.', ms=10)
        plt.plot(3, ys3[i], 'b.', ms=10)
        lineXs = [1, 2, 3]
        lineYs = [ys1[i], ys2[i], ys3[i]]
        plt.plot(lineXs, lineYs, 'k', alpha=.5)
    
    plt.title(title)
    plt.axis([.5, 3.5, 0, 280])
    tickPositions = [1, 2, 3]
    tickLabels = [ys1_name, ys2_name, ys3_name]
    plt.xticks(tickPositions, tickLabels)
    plt.ylabel(ylabel)
    plt.show()

def twoGroupConnectedScatter(ys1, ys2, ys1_name, ys2_name, ylabel, title):
    """
    Display 2 arrays of values as a connected scatter plot
    """
    plt.figure(figsize=(3, 5))
    for i in range(len(ys1)):
        plt.plot(1, ys1[i], 'b.', ms=10)
        plt.plot(2.5, ys2[i], 'b.', ms=10)

        lineXs = [1, 2.5]
        lineYs = [ys1[i], ys2[i]]
        plt.plot(lineXs, lineYs, 'k', alpha=.5)
    
    plt.title(title)
    plt.axis([.5, 3, 0, 500])
    tickPositions = [1, 2.5]
    tickLabels = [ys1_name, ys2_name]
    plt.xticks(tickPositions, tickLabels)
    plt.ylabel(ylabel)
    plt.show()



if __name__ == "__main__":
    raise Exception("this file must be imported, not run directly")