#minmax
import math
def minimax(cur_depth,node_index,max_trun,scores,target_depth):
    if cur_depth==target_depth:
        return scores[node_index]
    if max_trun:
        return max(minimax(cur_depth+1,node_index*2,False,scores,target_depth),
                   minimax(cur_depth+1,node_index*2+1,False,scores,target_depth))
    else:
        return min(minimax(cur_depth+1,node_index*2,True,scores,target_depth),
                   minimax(cur_depth+1,node_index*2+1,True,scores,target_depth))
    
scores=[21,3,47,9,33,34,23,24]
tree_depth=math.log(len(scores),2)    
print("the final solution of the node is:",minimax(0,0,True,scores,int(tree_depth)))