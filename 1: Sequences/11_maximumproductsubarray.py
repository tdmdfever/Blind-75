def max_product(nums):  
    maxProduct = currentMax = currentMin = nums[0]
    for num in nums[1:]:
        if num < 0:
            currentMax, currentMin = currentMin, currentMax
            
        currentMax = max(num, currentMax * num)
        currentMin = min(num, currentMin * num)

        maxProduct = max(maxProduct, currentMax)

    return maxProduct
