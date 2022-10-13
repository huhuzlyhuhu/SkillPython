import re
import matplotlib.pyplot as plt
import numpy
from pylab import *

# filename = sys.argv[1]
filename = "ALL.log"
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


    def draw_chart(nucleus_name, position_id, data_x, data_y):
        ax = plt.subplot(position_id)
        ax.plot(data_x, data_y, color="r", linestyle="-")
        if len(data_y) != 0:
            ax.set_title(
                '{}-loading\n'.format(nucleus_name) + 'AVERAGE : ' + str(round(mean(data_y), 3)) + '\nMAX : ' + str(
                    max(data_y)) + '  MIN : ' + str(
                    min(data_y)))
        else:
            ax.set_title(
                '{}-loading\n'.format(nucleus_name) + 'AVERAGE : ' + str(round(mean(data_y), 3)))
        ax.set_xlabel('count')
        ax.set_ylabel('%')


    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.figure(figsize=(100, 100), dpi=55)
    plt.figure(1)
    draw_chart('A72', 221, A72_X, A72_Y)
    draw_chart('C66_0', 222, C66_0_X, C66_0_Y)
    draw_chart('R5F_2', 223, R5F_2_X, R5F_2_Y)
    draw_chart('R5F_3', 224, R5F_3_X, R5F_3_Y)
    plt.show()
    # plt.savefig('./Loading.png')
