#덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라
## nums = [2, 7]
## target = 9
## >>> [0, 1]
from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
	nums_len = len(nums)
	for i in range(nums_len):
		for j in range(i + 1, len(nums)):
			if nums[i] + nums[j] == target:
				return [i, j]


nums = [2, 7, 11, 15]
target = 9
print( two_sum(nums, target) )