import  numpy as np
import matplotlib.pyplot as plt
x = np.arange(0,1,0.01)   #0-1之内每0.01绘制一个点
y= x*x+9   #更改函数
plt.plot(x,y)
plt.show()
