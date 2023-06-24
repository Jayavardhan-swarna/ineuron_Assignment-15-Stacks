def trap(height):
    left = 0
    right = len(height) - 1
    left_max = right_max = water = 0

    while left <= right:
        if height[left] <= height[right]:
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            left += 1
        else:
            right_max = max(right_max, height[right])
            water += right_max - height[right]
            right -= 1

    return water

height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(height1))  # Output: 6

height2 = [4, 2, 0, 3, 2, 5]
print(trap(height2))  # Output: 9
