class PrintTable(object):
    '''打印99乘法表'''
    def __init__(self):
        print(u"开始打印...")
        self.print99()

    def print99(self):
        for i in range(1,10):
            for j in range(1,i+1):
                print('%dx%d=%2d\t'%(j,i,i*j),end=' ')
            print('\n')

            
if __name__=="__main__":
    pt=PrintTable()
