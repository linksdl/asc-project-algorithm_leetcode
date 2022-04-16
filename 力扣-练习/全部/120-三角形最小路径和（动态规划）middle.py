#!/usr/bin/env 全部
# -*- coding: utf-8 -*-

# @Time        : 2021/9/16 6:55 下午
# @Author      : linksdl
# @ProjectName : futuretec-project-algorithm_leetcode
# @File        : 120-三角形最小路径和（动态规划）middle.py

'''
120. 三角形最小路径和
https://leetcode-cn.com/problems/triangle
给定一个三角形 triangle ，找出自顶向下的最小路径和。
每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
'''

class Solution:
    def minimumTotal(self, triangle) -> int:
        n = len(triangle)
        ans = [0] * n
        ans[0] = triangle[0][0]
        for i in range(1, n):
            ans[i] = ans[i - 1] + triangle[i][i]
            for j in range(i - 1, 0, -1):
                ans[j] = min(ans[j - 1], ans[j]) + triangle[i][j]
            ans[0] += triangle[i][0]

        return min(ans)
