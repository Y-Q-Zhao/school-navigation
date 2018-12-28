import numpy as np

def introduction():
    '''
    介绍12个景点之用
    '''

    index={'0':'丁香餐厅','1':'竹园餐厅','2':'海棠餐厅','3':'北操场',
           '4':'南操场','5':'工训中心','6':'图书馆','7':'体育馆',
           '8':'东门','9':'北门','10':'校医院','11':'大活'}
    introduce={'丁香餐厅':'丁香餐厅位于丁香公寓附近，供住在丁香公寓的学生及教职工用餐之用',
               '竹园餐厅':'竹园餐厅位于竹园公寓附近，供住在竹园公寓的学生及教职工用餐之用',
               '海棠餐厅':'海棠餐厅位于海棠公寓附近，供住在海棠公寓的学生及教职工用餐之用',
               '北操场':'北操场位于学校西北角，设有足球场和主席台，可以举行运动会',
               '南操场':'南操场位于学校西南角，设有足球场等设施',
               '工训中心':'工训中心位于学校中间位置，负责学生金工实习的教学实践任务',
               '图书馆':'图书馆位于E楼旁，供学生借阅图书及自习之用',
               '体育馆':'远望谷体育馆新建于2017年，位于学校东南面',
               '东门':'东门位于西沣路上，是学校主要的主要出口之一',
               '北门':'北门位于学校北面，是学校主要的主要出口之一',
               '校医院':'校医院位于学校东北角上，时刻关注学生健康问题',
               '大活':'大学生活动中心位于学校西面，为学生组织活动提供场所'}
    print('Now our map have 12 positions:\n0:丁香餐厅,1:竹园餐厅,2:海棠餐厅,3:北操场\n4:南操场,  5:工训中心,6:图书馆,  7:体育馆\n8:东门,    9:北门,    10:校医院, 11:大活')
    place=input('please enter the position you want to learn about:')
    list=['0','1','2','3','4','5','6','7','8','9','10','11']
    while place not in list:
        print('the position you entered  is out of range !')
        place=input('please enter the position you want to learn about:')
    print(introduce[index[place]])

def distance(i,j):
    '''
    考虑到各个点之间的实际距离比较难以测量，故在地图上通过测量两点间直线距离代替，返回的是(i,j)间的距离
    '''
    map_ori=np.array([[0   ,878 ,701 ,729 ,293 ,719 ,291 ,840 ,988 ,894 ,1100,363 ],
                  [878 ,0   ,584 ,897 ,1000,169 ,591 ,629 ,492 ,330 ,237 ,945 ],
                  [701 ,584 ,0   ,319 ,719 ,543 ,542 ,1000,1000,328 ,779 ,529 ],
                  [729 ,897 ,319 ,0   ,616 ,839 ,698 ,1200,1200,639 ,1100,416 ],
                  [293 ,1000,719 ,616 ,0   ,926 ,524 ,1100,1200,996 ,1300,203 ],
                  [719 ,169 ,543 ,839 ,926 ,0   ,430 ,528 ,458 ,398 ,394 ,825 ],
                  [291 ,591 ,542 ,698 ,524 ,430 ,0   ,631 ,730 ,650 ,823 ,484 ],
                  [840 ,629 ,1000,1200,1100,528 ,631 ,0   ,243 ,925 ,710 ,1100],
                  [988 ,492 ,1000,1200,1200,458 ,730 ,243 ,0   ,822 ,502 ,1200],
                  [894 ,330 ,328 ,639 ,996 ,398 ,650 ,925 ,822 ,0   ,480 ,823 ],
                  [1100,237 ,779 ,1100,1300,394 ,823 ,710 ,502 ,480 ,0   ,1100],
                  [363 ,945 ,529 ,416 ,203 ,825 ,484 ,1100,1200,823 ,1100,0   ]])
    map=np.array([[0   ,0   ,0   ,0   ,293 ,0   ,291 ,840 ,0   ,0   ,0   ,0   ],
                  [0   ,0   ,584 ,0   ,0   ,169 ,0   ,0   ,0   ,330 ,237 ,0   ],
                  [0   ,584 ,0   ,319 ,0   ,543 ,0   ,0   ,0   ,328 ,0   ,0   ],
                  [0   ,0   ,319 ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,416 ],
                  [293 ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,203 ],
                  [0   ,169 ,543 ,0   ,0   ,0   ,430 ,0   ,458 ,0   ,0   ,0   ],
                  [291 ,0   ,0   ,0   ,0   ,430 ,0   ,0   ,0   ,0   ,0   ,484 ],
                  [840 ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,243 ,0   ,0   ,0   ],
                  [0   ,0   ,0   ,0   ,0   ,458 ,0   ,243 ,0   ,0   ,502 ,0   ],
                  [0   ,330 ,328 ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ],
                  [0   ,237 ,0   ,0   ,0   ,0   ,0   ,0   ,502 ,0   ,0   ,0   ],
                  [0   ,0   ,0   ,416 ,203 ,0   ,484 ,0   ,0   ,0   ,0   ,0   ]])

    #检查是否为无向图
    # for i in range(12):
    #     for j in range(12):
    #         if map[i][j]!=map[j][i]:
    #             print('[%d,%d]'%(i,j))

    if i<12 and j<12 and i>=0 and j>=0:
        return(map[i][j])
    else:
        print('Sorry,the index is out of range !')
        return(0)

def shortest_path(i,j):
    '''
    通过Dijkstra算法求最短路径问题，返回的是一个包含关键点的列表
    '''

    X=[i]   #已确定距离的点
    Y=[0,1,2,3,4,5,6,7,8,9,10,11]   #未确定距离的点
    route_x=[[i,i,0]]   #起到类似邻接表的作用
    Y.remove(i) #去掉起点

    #找出最短路径
    while j not in X:
        mini_dist=1000000000
        present_point=j
        next_point=j
        for p1 in route_x:
            for p2 in Y:
                if distance(p1[1],p2)!=0 and p1[2]+distance(p1[1],p2)<=mini_dist:
                    mini_dist=p1[2]+distance(p1[1],p2)
                    present_point=p1[1]
                    next_point=p2
        X.append(next_point)
        route_x.append([present_point,next_point,mini_dist])
        Y.remove(next_point)
    # print(route_x)

    #整理出最短路径的线路
    final_distance=route_x[-1][2]
    final_point=route_x[-1][1]
    last_point=route_x[-1][0]
    the_route=[final_point,last_point]
    while last_point!=i:
        for R in route_x:
            if R[1]==last_point:
                last_point=R[0]
                the_route.append(last_point)
    the_route.reverse()
    print(the_route)

def interface_eng():
    print('Welcome to use our school navigation ststem !')
    print('Our system have two function:\n1)Introduce the sites in the school for you;\n2)Directions for you;')
    choose=int(input('Now please choose the function you want to use (1/2):'))
    while choose not in [1,2]:
        choose = int(input('Sorry your choose is beyound our ability, please choose the function you want to use again(1/2):'))
    if choose==1:
        introduction()
    elif choose==2:
        start=int(input('Please enter the starting point:'))
        if start not in range(12):
            start = int(input('This point is out of range,Please enter the ending point again:'))
        end=int(input('Please enter the starting point:'))
        if end not in range(12):
            end=int(input('This point is out of range,Please enter the ending point again:'))
        if start==end:
            print('The start is the end')
        else:
            shortest_path(start,end)

######测试区#############################################################################
# introduction()
# a=distance(12,0)
#print(a)
# minimun_distance(2,10)
# shortest_path(0,9)
interface_eng()
#########################################################################################