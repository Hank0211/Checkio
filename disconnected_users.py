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
    实现的思路：
    用一个列表visted_node保存已经遍历过的节点，然后从该列表中取出节点，寻找与之相关的节点，找到相关节点后就可以断定两个节点是联通的，
    在遍历过程中不断的把相关联通的节点加入到visted_node列表中，最后判断哪些节点不在列表中，就可以统计出哪些节点没有遍历到。
    '''
