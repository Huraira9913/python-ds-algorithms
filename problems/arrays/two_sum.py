"""
Two Sum - Classic array / hashing problem.
Useful for understanding hash maps in data processing pipelines.
"""

from typing import List, Dict


def two_sum_bruteforce(nums: List[int], target: int) -> List[int]:
    """O(n²) solution."""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_hashmap(nums: List[int], target: int) -> List[int]:
    """O(n) time, O(n) space using hash map."""
    seen: Dict[int, int] = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum_hashmap(nums, target) == [0, 1]
    assert two_sum_bruteforce(nums, target) == [0, 1]
    print("All tests passed.")
    print(f"two_sum_hashmap({nums}, {target}) = {two_sum_hashmap(nums, target)}")
