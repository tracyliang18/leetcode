def judge(nums):
    nums.sort()
    #print nums
    for i in range(len(nums) - 1):
        if nums[i] + 1 != nums[i+1]:
            return False
    return True

def consecutiveK(nums, k):
    min_queue = []
    max_queue = []
    if len(nums) <= 0:
        return [[]]
    for i,num in enumerate(nums[0:k-1]):
        while len(min_queue) > 0 and num <= min_queue[-1][1]:
            del min_queue[-1]
        min_queue.append((i,num))
        while len(max_queue) > 0 and num >= max_queue[-1][1]:
            del max_queue[-1]
        max_queue.append((i,num))
    ret = []
    for i in range(len(nums) - k + 1):
        num = nums[i + k - 1]
        while len(min_queue) > 0 and num <= min_queue[-1][1]:
            del min_queue[-1]
        min_queue.append((i+k-1,num))
        while len(max_queue) > 0 and num >= max_queue[-1][1]:
            del max_queue[-1]
        max_queue.append((i+k-1,num))
        curmin = min_queue[0][1]
        curmax = max_queue[0][1]
        if curmax == curmin + k - 1:
            if judge(nums[i:i+k]):
                ret.append(nums[i:i+k])
        if i == min_queue[0][0]:
            del min_queue[0]
        if i == max_queue[0][0]:
            del max_queue[0]
    return ret

print consecutiveK([6,7,4,3,2,1,9,9,9,9,9,9,9,4,5], 2)
