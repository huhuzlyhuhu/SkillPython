import re
import matplotlib.pyplot as plt
import numpy
from pylab import *

filename = sys.argv[1]
with open(filename, 'r') as f:
    rea = f.read()
    C66_0_X = []
    R5F_3_X = []
    R5F_2_X = []
    A72_X = []
    C66_0_Y = []
    R5F_3_Y = []
    R5F_2_Y = []
    A72_Y = []
    count_c66 = 0
    count_r5f2 = 0
    count_r5f3 = 0
    count_a72 = 0
    reg = '.*?TDA4_(.*?)_DEBUG.*?persent:(.*?)\n'
    res = re.findall(reg, rea)
    for ij in res:
        if ij[0] == 'C66_0':
            count_c66 += 1
            C66_0_Y.append(int(ij[1]))
            C66_0_X.append(count_c66)
        if ij[0] == 'R5F_2':
            count_r5f2 += 1
            R5F_2_Y.append(int(ij[1]))
            R5F_2_X.append(count_r5f2)
        if ij[0] == 'R5F_3':
            count_r5f3 += 1
            R5F_3_Y.append(int(ij[1]))
            R5F_3_X.append(count_r5f3)
        if ij[0] == 'A72':
            count_a72 += 1
            A72_Y.append(int(ij[1]))
            A72_X.append(count_a72)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(100, 100), dpi=55)
    plt.figure(1)
    ax1 = plt.subplot(221)
    ax1.plot(C66_0_X, C66_0_Y, color="r", linestyle="-")
    if len(C66_0_Y) != 0:
        ax1.set_title(
            'C66_0-loading\n' + 'AVERAGE : ' + str(round(mean(C66_0_Y), 3)) + '\nMAX : ' + str(
                max(C66_0_Y)) + '  MIN : ' + str(
                min(C66_0_Y)))
    else:
        ax1.set_title(
            'C66_0-loading\n' + 'AVERAGE : ' + str(round(mean(C66_0_Y), 3)))
    ax1.set_xlabel('count')
    ax1.set_ylabel('%')
    ax2 = plt.subplot(222)
    ax2.plot(R5F_2_X, R5F_2_Y, color="r", linestyle="-")
    if len(R5F_2_Y) != 0:
        ax2.set_title(
            'R5F_2-loading\n' + 'AVERAGE : ' + str(round(mean(R5F_2_Y), 3)) + '\nMAX : ' + str(
                max(R5F_2_Y)) + '  MIN : ' + str(
                min(R5F_2_Y)))
    else:
        ax2.set_title(
            'R5F_2-loading\n' + 'AVERAGE : ' + str(round(mean(R5F_2_Y), 3)))
    ax2.set_xlabel('count')
    ax2.set_ylabel('%')
    ax3 = plt.subplot(223)
    ax3.plot(R5F_3_X, R5F_3_Y, color="r", linestyle="-")
    if len(R5F_3_Y):
        ax3.set_title(
            'R5F_3-loading\n' + 'AVERAGE : ' + str(round(mean(R5F_3_Y), 3)) + '\nMAX : ' + str(
                max(R5F_3_Y)) + '  MIN : ' + str(
                min(R5F_3_Y)))
    else:
        ax3.set_title(
            'R5F_3-loading\n' + 'AVERAGE : ' + str(round(mean(R5F_3_Y), 3)))
    ax3.set_xlabel('count')
    ax3.set_ylabel('%')
    ax4 = plt.subplot(224)
    ax4.plot(A72_X, A72_Y, color="r", linestyle="-")
    if len(A72_Y) != 0:
        ax4.set_title(
            'A72-loading\n' + 'AVERAGE : ' + str(round(mean(A72_Y), 3)) + '\nMAX : ' + str(
                max(A72_Y)) + '  MIN : ' + str(
                min(A72_Y)))
    else:
        ax4.set_title(
            'A72-loading\n' + 'AVERAGE : ' + str(round(mean(A72_Y), 3)))
    ax4.set_xlabel('count')
    ax4.set_ylabel('%')
    plt.show()
    # plt.savefig('./Loading.png')
