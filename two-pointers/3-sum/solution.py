def sort(nums):
    p1 = 0
    p2 = 1
    n = len(nums)
    while p1 <= n - 2:
        if nums[p1] > nums[p2]:
            temp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = temp
        if p2 == n - 1:
            if nums[p1] > nums[p2]:
                temp = nums[p1]
                nums[p1] = nums[p2]
                nums[p2] = temp
            p1 = p1 + 1
            p2 = p1 + 1
        else:
            p2 = p2 + 1
    return nums


def isGroupValid(self, p1, p2, p3, nums):
    sum = nums[p1] + nums[p2] + nums[p3]
    return sum == 0


def appendGroup(self, p1, p2, p3, nums, output):
    isValid = self.isGroupValid(p1, p2, p3, nums)
    if isValid:
        group = [nums[p1], nums[p2], nums[p3]]
        sorted_group = self.sort(group)
        output.add(tuple(sorted_group))


def threeSum(nums):
    nums.sort()  # O(n log n) - sort once
    result = []
    n = len(nums)

    for i in range(n - 2):  # O(n)
        # Skip duplicates for first element
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left, right = i + 1, n - 1  # Two pointers

        while left < right:  # O(n) for each i
            total = nums[i] + nums[left] + nums[right]

            if total == 0:
                result.append([nums[i], nums[left], nums[right]])

                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif total < 0:
                left += 1  # Need larger sum
            else:
                right -= 1  # Need smaller sum

    return result


nums = [-1, 0, 1, 2, -1, -4]
threeSum(nums)
