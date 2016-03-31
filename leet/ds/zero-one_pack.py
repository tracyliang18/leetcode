def solve(values,weights, V):
    assert max(weights) <= V
    ret = [0 for i in range(V+1)] #这里没有要求装满,如果是限制在装满下的最优解则初始化为无穷小
    n = len(values)
    s = sum(weights)
    for i in range(n):
        j = V
        while j >= max(V - s,weights[i]): #这里还可以优化
            ret[j] = max(ret[j], ret[j-weights[i]] + values[i])
            j -= 1
        s -= weights[i]
    return ret[V]


print solve([99,99,100],[1,2,4],4)

def zero_one_pack(v,w,V,state):
    i = V
    while i >= w:
        state[i] = max(state[i],state[i-w]+v)
        i -= 1



