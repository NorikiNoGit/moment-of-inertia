import numpy as np
import matplotlib.pyplot as plt

def plot_sine_waves(w_values):
    t = np.linspace(-10, 10, 5000)
    num_plots = len(w_values)
    y_sum_list=[]
    dydt_sum_list=[]

    fig, axs = plt.subplots(num_plots, 1, figsize=(8, 6*num_plots))

    for i, w in enumerate(w_values):
        y = np.sin(w * t)
        axs[i].plot(t, y)
        axs[i].set_ylim(-1, 1)
        axs[i].grid(True)
        axs[i].set_title(f'Graph of y = sin({w}t)')
        axs[i].set_xlabel('t')
        axs[i].set_ylabel('y')
        y_sum = sum(y**2)
        y_sum_list.append(y_sum)
        print('w=',w_values[i],' sum_y = ', y_sum)

        # 傾きの和を求める
        dy_dt_sum=0
        for j in t:
            dy_dt_sum += abs(w*np.cos(w*j))
        dydt_sum_list.append(dy_dt_sum)

    plt.tight_layout()
    plt.savefig('sins.png')
    plt.show()
    

    plot_ysum(w_values, y_sum_list)
    print('w_walues:', w_values)
    print('dydt_sum_list:', dydt_sum_list)
    plot_dydtsum(w_values, dydt_sum_list)
    
def plot_ysum(w_values, y_sum_list):
    plt.scatter(w_values, y_sum_list)
    plt.grid(True)
    plt.ylim(0, 3000)
    plt.xlabel('w')
    plt.ylabel('sum(y^2)')
    plt.savefig('y^2_sum.png')
    plt.show()
    
def plot_dydtsum(w_values, dydt_sum_list):
    plt.scatter(w_values, dydt_sum_list)
    plt.grid(True)
    plt.xlabel('w')
    plt.ylabel("sum|y'|")
    plt.savefig("sum|y'|.png")
    plt.show()
    

# 使用例
# w = [5, 10, 50, 100, 110, 150, 200]
w = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
plot_sine_waves(w)
