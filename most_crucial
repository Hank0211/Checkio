#判断哪个节点最重要，net是列表，users是字典类型
#net中存储拓扑结构（如：[a,b],[b,c],[c,d]）,users中存储每个节点的重要程度
#连接在一起的节点，重要程度值相加到一起后再平方，断开的节点单独算平方值，损毁的节点只计算节点的重要程度(如：(a+b+c+d)**2，如果b损坏a**2+b+(c+d)**2)
def most_crucial(net, users):
    important_node=dict()
    ilr=[]#最终返回的列表
    visted_list=[]#已访问队列
    vlp=0 #已访问队列的位置
    nlp=0 #net的位置指针
    next_node='' #下一节点
    count=0
    min_value=0
    for member in users:
        important_node[member]=0
        nlp = 0
        vlp=0
        visted_list.clear()
        visted_list+=net[nlp]
        while(nlp < len(net) ):
            count=0
            while(vlp < len(visted_list) ):
                if (visted_list[vlp] == member):#member代表当前损坏的节点
                    important_node[member]+=users[member]
                    vlp+=1
                    continue
                else:
                    next_node=visted_list[vlp]
                    for i_next_node in net: #把已访问列表中相关的节点找出来，加入到已访问列表
                        if i_next_node[0] in visted_list and i_next_node[1] in visted_list :
                            continue
                        elif next_node in i_next_node:
                           if next_node == i_next_node[0]:
                               visted_list.append(i_next_node[1])
                           elif next_node == i_next_node[1]:
                               visted_list.append(i_next_node[0])

                count+=users[visted_list[vlp]]
                vlp+=1
            important_node[member]+=count**2
            nlp+=1
    
    min_value=important_node[min(important_node,key=lambda x:important_node[x])]
    for i in important_node:
        if important_node[i]==min_value :
            ilr.append(i)
    return ilr

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert most_crucial([
            ['A', 'B'],
            ['B', 'C']
        ],{
            'A': 10,
            'B': 10,
            'C': 10
        }) == ['B'], 'First'

    assert most_crucial([
            ['A', 'B']
        ],{
            'A': 20,
            'B': 10
        }) == ['A'], 'Second'

    assert most_crucial([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['A', 'E']
        ],{
            'A': 0,
            'B': 10,
            'C': 10,
            'D': 10,
            'E': 10
        }) == ['A'], 'Third'

    assert most_crucial([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ],{
            'A': 10,
            'B': 20,
            'C': 10,
            'D': 20
        }) == ['B'], 'Forth'

    print('Nobody expected that, but you did it! It is time to share it!')
