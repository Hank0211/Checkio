def subnetworks(net:list, crushes:list):
    visted_node=[]#当前子网的节点有哪些
    cur_node=[]#当前拓扑
    sub_net=0#有多少子网
    
    while net:
        times=0
        net_length = len(net)
        while times < net_length:
            if net :
                cur_node=net.pop()
                temp=crush_check(cur_node, crushes)
                if temp == "NO" :
                    if len(visted_node)==0 :
                        visted_node.append(cur_node)#将当前拓扑添加到已查节点
                    else :
                        if node_check(cur_node[0],visted_node)==0 or node_check(cur_node[1],visted_node)==0:#如果cur_node和已经访问过的节点有关联，那么将它添加到visted_node中
                            visted_node.append(cur_node)
                        else:
                            net.insert(0,cur_node)#否则重新插回net中
                elif temp == "YES" :
                    break
                else :
                    if node_check(temp, net)==0 or node_check(temp, visted_node)==0:
                        pass
                    elif node_check(temp, visted_node)==1 and node_check(temp, net)==1 :
                        #如果和已访问列表还有拓扑表中都无关，那么说明该节点是一个独立的子
                        sub_net+=1 
            times+=1
        times=0
        if temp != "YES" :
            sub_net+=1
        visted_node.clear()
    return sub_net

def crush_check(node_i:'list元素是列表', crushes:'list元素是字符')->'检查节点是否CRUSHED':
    if node_i[0] not in crushes and node_i[1] not in crushes:
        return "NO"
    elif node_i[0] in crushes and node_i[1] in crushes:
        return "YES"
    elif node_i[0] in crushes:
        return node_i[1]#如果和任何节点都没有关联那么它自己是一个子网
    elif node_i[1] in crushes:
        return node_i[0]#如果和任何节点都没有关联那么它自己是一个子网
    return None

def node_check(node_s:'是单个节点', node_i:'list元素是列表,参数是net')->'检查单个节点是否在拓扑中和其它节点有关联':
    for i in node_i:
        if node_s in i:
            return 0
    return 1
    

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['B']) == 2, "First"
    assert subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']) == 3, "Second"
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')
