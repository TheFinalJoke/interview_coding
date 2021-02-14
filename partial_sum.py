#!/usr/bin/env python3
import sys 

nums = [6,10,6,10]
if __name__ == '__main__':
    if len(nums) % 2 != 0:
        print("Can't Divide arrays ")
        sys.exit(1)
    half = int(len(nums)/2)
    num_lists = {
        "list1": nums[:half],
        "list2": nums[half:]
    }
    if sum(num_lists["list1"]) == sum(num_lists['list2']):
        print(f"{num_lists['list1']}, {num_lists['list2']}")