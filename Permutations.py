from typing import List
from pprint import pprint


class Permutations:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.level = 2
        self.pointer = 0
        self.permutations: List[List[int]] = []
        self.temp: List[List[int]] = []
        self.temp_2: List[List[int]] = []

    def permutate(self, int_list) -> List[List[int]]:
        """Perform the permutations"""
         if len(int_list) == 1:
            self.temp = [int_list]
            return self.temp
        if len(int_list) == 0:
            return self.temp
        if len(self.temp) == 0:
            for k, v in enumerate(self.nums):
                t = [[v, j] for j in self.nums if j != v]
                for p in t:
                    self.temp.append(p)
            return self.permutate(int_list=self.temp)
        else:
            while len(self.temp[-1]) != len(self.nums):
                for s in self.temp:
                    t = [j for j in self.nums if j not in s]
                    tt = [[*s, t[i]] for i, _ in enumerate(t)]
                    for p in tt:
                        self.temp_2.append(p)
                self.temp = self.temp_2
                self.temp_2 = []
                return self.permutate(int_list=self.temp)
