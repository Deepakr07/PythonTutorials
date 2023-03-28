import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def calculate_coeff(x , y):
    n = np.size(x)
    m_x = np.mean(x)
    m_y = np.mean(y)
    S_xy = np.sum(y*x)-n*m_y*m_x
    S_xx = np.sum(x*x)-n*m_x*m_x
    b_1 = S_xy/S_xx 
    b_0 = m_y - b_1*m_x
    return(b_0,b_1)


def plotResults(x,y,b):
    plt.scatter(x,y,color = 'm',marker="o",s = 30)
    y_pred = b[0]+b[1]*x
    plt.plot(x,y_pred,color = "g")
    plt.xlabel("Area")
    plt.ylabel("price")
    plt.show()
    
def main():
    data = pd.read_csv("Housing (1).csv")
    x= data["area"]
    y = data["price"]
    b= calculate_coeff(x,y)
    print("The estimated coeficients are \n b_0 = {}\\n b_1 = {}\n".format(b[0],b[1]))
    plotResults(x,y,b)
if __name__ == "__main__":
    main()    	