nums = [1,2,3,4]

i = 1
v = (len(nums) - 1) - i
pre_product = [1] * len(nums)
suf_product = [1] * len(nums)
while i < len(nums):

    pre_product[v] = nums[v + 1] * pre_product[v + 1]
    suf_product[i] = nums[i - 1] * suf_product[i - 1]
    i += 1
    v = (len(nums) - 1) - i

    
for i, (pre, suf) in enumerate(zip(pre_product, suf_product)):
    nums[i] = pre * suf

print(nums)


