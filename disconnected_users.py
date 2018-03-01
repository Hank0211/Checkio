def disconnected_users(net:list, users:dict, source:str, crushes:list):
    visted_node=[]
    if source not in crushes:
        visted_node.append(source)#添加第一个起始点
    for trace_i in visted_node:
        for loop_i in net:
            if trace_i in loop_i:
                node_check(loop_i,crushes,visted_node)
    '''
      统计有多少节点没被访问到
    '''
    count=0
    for i in users:
        if i not in visted_node:
            count+=users[i]
    return count

def node_check(node_i:list, crushes:list, visted_node:list):
    if node_i[0] not in crushes and node_i[0] not in visted_node :
        visted_node.append(node_i[0])
    elif node_i[1] not in crushes and node_i[1] not in visted_node :
        visted_node.append(node_i[1])
    else :
        return None
        
if __name__ == '__main__':
    result=disconnected_users([['A','B'],
                        ['B','C'],
                        ['C','D']],
                       {'A':10,
                        'B':20,
                        'C':30,
                        'D':40},
                        'A',['C'])
    print(result)
    '''
    第一个参数用于设置每个节点间的拓扑，
    第二个参数用于设置每个节点上的人数，
    第三个参数用于设置消息从哪个节点发出，
    第四个参数用于设置拓扑中哪个节点损坏不能发送消息。
    函数功能：遍历图结构，统计不能被遍历到的节点，一共有多少人。
    '''
