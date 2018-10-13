#coding=utf-8
import wx
import time
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Calc",size = (440,560))
        panel = wx.Panel(self)
        labelAll = wx.StaticText(panel,-1,pos =(0,0))
        self.textAll = wx.TextCtrl(panel,
                                                -1,
                                               size=(400,50),
                                               pos=(10,25),
                                               style=wx.TE_MULTILINE | wx.TE_READONLY)#wx.TE_PASSWORD密文

        self.btn7 = wx.Button(panel,-1,"7",size=(100,100),pos=(10,80))
        self.btn8 = wx.Button(panel,-1,"8",size=(100,100),pos=(110,80))
        self.btn9 = wx.Button(panel,-1,"9",size=(100,100),pos=(210,80))
        self.btnDiv = wx.Button(panel,-1,"/",size=(100,100),pos=(310,80))
        self.btn4= wx.Button(panel,-1,"4",size=(100,100),pos=(10,180))
        self.btn5 = wx.Button(panel,-1,"5",size=(100,100),pos=(110,180))
        self.btn6 = wx.Button(panel,-1,"6",size=(100,100),pos=(210,180))
        self.btnMul = wx.Button(panel,-1,"*",size=(100,100),pos=(310,180))
        self.btn1 = wx.Button(panel,-1,"1",size=(100,100),pos=(10,280))
        self.btn2= wx.Button(panel,-1,"2",size=(100,100),pos=(110,280))
        self.btn3 = wx.Button(panel,-1,"3",size=(100,100),pos=(210,280))
        self.btnAdc = wx.Button(panel,-1,"-",size=(100,100),pos=(310,280))
        self.btnDown = wx.Button(panel,-1,".",size=(100,100),pos=(10,380))
        self.btn0 = wx.Button(panel,-1,"0",size=(100,100),pos=(110,380))
        self.btnResult = wx.Button(panel,-1,"=",size=(100,100),pos=(210,380))
        self.btnAdd = wx.Button(panel,-1,"+",size=(100,100),pos=(310,380))

        self.Bind(wx.EVT_BUTTON,self.OnButton7,self.btn7)
        self.Bind(wx.EVT_BUTTON,self.OnButton8,self.btn8)
        self.Bind(wx.EVT_BUTTON,self.OnButton9,self.btn9)
        self.Bind(wx.EVT_BUTTON,self.OnButtonDiv,self.btnDiv)
        self.Bind(wx.EVT_BUTTON,self.OnButton4,self.btn4)
        self.Bind(wx.EVT_BUTTON,self.OnButton5,self.btn5)
        self.Bind(wx.EVT_BUTTON,self.OnButton6,self.btn6)
        self.Bind(wx.EVT_BUTTON,self.OnButtonMul,self.btnMul)
        self.Bind(wx.EVT_BUTTON,self.OnButton1,self.btn1)
        self.Bind(wx.EVT_BUTTON,self.OnButton2,self.btn2)
        self.Bind(wx.EVT_BUTTON,self.OnButton3,self.btn3)
        self.Bind(wx.EVT_BUTTON,self.OnButtonAdc,self.btnAdc)
        self.Bind(wx.EVT_BUTTON,self.OnButtonDown,self.btnDown)
        self.Bind(wx.EVT_BUTTON,self.OnButton0,self.btn0)
        self.Bind(wx.EVT_BUTTON,self.OnButtonResult,self.btnResult)
        self.Bind(wx.EVT_BUTTON,self.OnButtonAdd,self.btnAdd)



    def OnButton7(self,event):
        userinput='7'
        self.textAll.AppendText(userinput)
    def OnButton8(self,event):
        userinput='8'
        self.textAll.AppendText(userinput)
    def OnButton9(self,event):
        userinput='9'
        self.textAll.AppendText(userinput)
    def OnButtonDiv(self,event):
        userinput='/'
        self.textAll.AppendText(userinput)
    def OnButton4(self,event):
        userinput='4'
        self.textAll.AppendText(userinput)
    def OnButton5(self,event):
        userinput='5'
        self.textAll.AppendText(userinput)
    def OnButton6(self,event):
        userinput='6'
        self.textAll.AppendText(userinput)
    def OnButtonMul(self,event):
        userinput='*'
        self.textAll.AppendText(userinput)
    def OnButton1(self,event):
        userinput='1'
        self.textAll.AppendText(userinput)
    def OnButton2(self,event):
        userinput='2'
        self.textAll.AppendText(userinput)
    def OnButton3(self,event):
        userinput='3'
        self.textAll.AppendText(userinput)
    def OnButtonAdc(self,event):
        userinput='-'
        self.textAll.AppendText(userinput)
    def OnButtonDown(self,event):
        userinput='.'
        self.textAll.AppendText(userinput)
    def OnButton0(self,event):
        userinput='0'
        self.textAll.AppendText(userinput)
    def OnButtonResult(self,event):
        userinput = self.textAll.GetValue()
        print (userinput)
        self.textAll.Clear()
        Result=eval(userinput)  #识别计算代数式字符串
        self.textAll.AppendText(str(Result))
        
    def OnButtonAdd(self,event):
        userinput='+'
        self.textAll.AppendText(userinput)
        
        #self.textAll.SetValue(userinput)#给上方窗口
    def OnButtonClear(self,event):
        self.textIn.Clear()
        
app = wx.App()
frame = MyFrame()
frame.Show()
app.MainLoop()








'''放中间会报错，不懂！！！！！！！！！
        btnSizer = wx.BoxSizer()
        btnSizer.Add(self.btn7,proportion = 0)
        btnSizer.Add(self.btn8,proportion = 0)
        btnSizer.Add(self.btn9,proportion = 0)
        btnSizer.Add(self.btnDiv,proportion = 0)
        btnSizer.Add(self.btn4,proportion = 0)
        btnSizer.Add(self.btn5,proportion = 0)
        btnSizer.Add(self.btn6,proportion = 0)
        btnSizer.Add(self.btnMul,proportion = 0)
        btnSizer.Add(self.btn1,proportion = 0)
        btnSizer.Add(self.btn2,proportion = 0)
        btnSizer.Add(self.btn3,proportion = 0)
        btnSizer.Add(self.btnAdc,proportion = 0)
        btnSizer.Add(self.btnDown,proportion = 0)
        btnSizer.Add(self.btn0,proportion = 0)
        btnSizer.Add(self.btnResult,proportion = 0)
        btnSizer.Add(self.btnAdd,proportion = 0)'''
