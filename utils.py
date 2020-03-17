# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-17

from typing import List, Any
from unittest import TestCase, main


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 从列表生成二叉树。列表是一个层次遍历的结果

def generate_tree(data: List[Any]):
    if len(data) == 0:
        return None
    root = TreeNode(data[0])
    stack = [root]
    for i in range(1, len(data), 2):
        item = data[i:i + 2]
        node = stack.pop(0)
        if item[0]:
            node.left = TreeNode(item[0])
            stack.append(node.left)
        if len(item) == 2 and item[1]:
            node.right = TreeNode(item[1])
            stack.append(node.right)
    return root


# 单元测试
class TestGenerateTree(TestCase):

    def test_empty_gen(self):
        self.assertEqual(generate_tree([]), None)

    def test_gen_simple(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        target = generate_tree([1, 2, 3])
        self.assertEqual(root.val, target.val)
        self.assertEqual(root.left.val, target.left.val)
        self.assertEqual(root.right.val, target.right.val)

    def test_with_null(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        target = generate_tree([1, 2, None, 3])
        self.assertEqual(root.val, target.val)
        self.assertEqual(root.left.val, target.left.val)
        self.assertEqual(root.right, target.right)
        self.assertEqual(root.left.left.val, target.left.left.val)


if __name__ == '__main__':
    main()
