import socket, threading,random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #tcp
s.bind(('127.0.0.1', 8081))
s.listen(5)#监听
print("Waiting for connection...")


date_dict={'张三':['13800000000','001','北京市'],'李四':['13800000001','002','西安市'],'王五':['13800000002','003','天津市']}#需要初始全局参数
date_dict_1={'景飞':'123','胡兵':'456','bob':'789','乔天翼':'5102333'}


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(('Welcome!\n请先输入用户名登陆').encode('utf-8'))

    
    while True:
        user = sock.recv(1024).decode()#接受用户名
        if user in date_dict_1:#判断用户名存在
            sock.send(('请输入密码').encode('utf-8'))
            if (sock.recv(1024).decode()) != date_dict_1[user]:#判断密码正确性
                sock.send(('密码错误，请重新登录\n').encode('utf-8'))
                continue
            else:
                sock.send(('登陆成功\n\n\
通讯录软件\n\
输入你想操作的目录编号\n\
1通讯录查询\n\
2通讯录添加或修改\n\
3通讯录删除\n\
4猜数字游戏\n\
5退出\n').encode('utf-8'))
                                
                while True:
                    date_num = sock.recv(1024)#接收用户请求操作目录编号
                    date_num = int(date_num)
                    
                    if date_num ==1:#通讯录查询
                        sock.send(('请输入查询昵称').encode('utf-8'))
                        date_name=sock.recv(1024).decode('utf-8')#接收用户输入的昵称
                        if date_name in date_dict:#判断昵称是否存在
                            sock.send(('请输入查询内容编号:\n0 = 手机号\n1 = 编号\n2=家庭住址\n012=全部查询').encode('utf-8'))
                            neirong = sock.recv(1024).decode('utf-8')#接收用户查询的内容字符编号
                            size = len(neirong)
                            fg = ('电话号码:\t','编号:\t','家庭住址:\t')
                            msg_list = ''
                            for i in range(size):
                                msg_list += fg[int(neirong[i])] + date_dict[date_name][int(neirong[i])]+'\n'#遍历字典内keys值的列表
                            msg_list=msg_list+'\n输入你想操作的目录编号'
                            sock.send(msg_list.encode('utf-8'))
                            
                        else:
                            sock.send(('此昵称不存在！').encode())

                    elif date_num ==2:#通讯录增加或修改
                        sock.send(('请输入添加或修改号码的昵称').encode('utf-8'))
                        date_name = sock.recv(1024).decode()
                        if not date_name in date_dict:#判断接收的昵称是否存在
                            date_dict[date_name]=['未定义','未定义','未定义']
                        #print(date_name)
                        sock.send(('请输入该昵称的号码').encode('utf-8'))
                        date_number = sock.recv(1024).decode()#接收号码
                        #print(date_number)
                        date_number = str(date_number)
                        (date_dict[date_name])[0]=date_number
                        sock.send(('请输入该昵称的编号').encode('utf-8'))
                        date_number1 = sock.recv(1024).decode()#接收编号
                        date_number1 = str(date_number1)
                        (date_dict[date_name])[1]=date_number1
                        sock.send(('请输入该昵称地址').encode('utf-8'))
                        date_ads = sock.recv(1024).decode()#接收地址
                        (date_dict[date_name])[2]=date_ads
                        #print(str(date_dict))
                        sock.send(('通讯录添加成功！\n\n输入你想操作的目录编号').encode())

                    elif date_num==3:#通讯录删除
                        sock.send(('请输入删除号码的昵称').encode('utf-8'))
                        date_name = sock.recv(1024).decode()
                        #print(date_name)
                        del date_dict[date_name]
                        #print(str(date_dict))
                        sock.send(('成功删除！\n\n输入你想操作的目录编号').encode())

                        
                    elif date_num==4:
                        sock.send(("输入猜的数字").encode())
                        number_1=random.randint(0,99)
                        cishu=0
                        while True:
                            number=sock.recv(1024).decode()
                            number=int(number)
            
                            cishu=cishu+1
                            if number > number_1:
                                sock.send(("大了").encode())
                            elif number<number_1:
                                sock.send(("小了").encode())
                            else:
                                sock.send(("恭喜你，猜对了!\n\n输入你想操作的目录编号").encode())
                                break
                        continue
                        
                    elif date_num==5:#退出
                        sock.send(('退出').encode('utf-8'))
                        break
                    else:
                        sock.send(('编号输入错误!\n\n输入你想操作的目录编号').encode('utf-8'))
                        
        
        else:
            sock.send(('无此用户').encode('utf-8'))
            continue
while True: 
    sock, addr = s.accept()#接收连接
    #print(addr[0] + '\t' + str(addr[1]))
    #tcplink(sock, addr)#单个连接直接调用函数
    t = threading.Thread(target=tcplink, args=(sock, addr))#多用户链接，调用函数
    t.start()

