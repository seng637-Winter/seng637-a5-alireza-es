import matplotlib.pyplot as plt
import pandas as pd
import math

df = pd.read_csv("failure-dataset-a5.csv")

def eq_1(k=31):
    sum = 0
    for i in range(1, k+1):
        Ni = df.iloc[i-1, 1]
        sum += (i-1) * Ni
    return sum
    
def eq_2(k=31):
    sum = 0
    for i in range(1, k+1):
        Ni = df.iloc[i-1, 1]
        sum += Ni
    
    return (k-1)/2 * sum

def eq_3(k=31):
    sum = 0
    for i in range(1, k+1):
        Ni = df.iloc[i-1, 1]
        sum += Ni
        
    ans = math.sqrt((k**2 - 1)/12 * sum)
    return ans

def main_eq(k):
    return (eq_1(k) - eq_2(k)) / eq_3(k)

    
def draw_laplace():
    final_list = []
    index = []
    for i in range(2, 32):
        final_list.append(main_eq(i))
        index.append(i)
        
    plt.scatter(index, final_list, c='blue', label='Data Points') 
    plt.plot(index, final_list, label='Line connecting dots')
    plt.xticks(index) 

    plt.title('Laplace Test Statistic')
    plt.xlabel('k')
    plt.ylabel('u(k)')
    plt.axhline(y=0, color='red', linestyle='--', label='Y = 0 Line')

    plt.grid(True)

    plt.show()

def draw_failurerate():
    final_list = [0]
    index = [1.05]
    for i in range(3, 32):
        index.append(index[-1] + df.iloc[i-1, 2])
        final_list.append(sum(df.iloc[3:i-1, 1])/index[-1])

    plt.scatter(index, final_list, c='blue', label='Data Points') 
    plt.plot(index, final_list, label='Line connecting dots')
    # plt.yticks(final_list) 

    plt.title('Failure rate')
    plt.xlabel('time (h)')
    plt.ylabel('failure rate')

    plt.show()

draw_failurerate()
