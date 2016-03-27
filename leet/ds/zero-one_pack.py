def solve(values,weights, V):
    assert max(weights) <= V
    ret = [0 for i in range(V+1)]
    n = len(values)
    for i in range(n):
        j = V
        while j >= weights[i]:
            ret[j] = max(ret[j], ret[j-weights[i]] + values[i])
            j -= 1
    return ret[V]


print solve([99,99,100],[1,2,4],4)
