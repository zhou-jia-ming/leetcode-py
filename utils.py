# coding:utf-8
# Created by: Jiaming
# Created at: 2020-03-17

from typing import List, Any
from unittest import TestCase, main

null = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def generate_list(data: List[Any]):
    head = cur_node = ListNode(data[0])
    for item in data[1:]:
        cur_node.next = ListNode(item)
        cur_node = cur_node.next
    return head


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
        target = generate_tree([1, 2, null, 3])
        self.assertEqual(root.val, target.val)
        self.assertEqual(root.left.val, target.left.val)
        self.assertEqual(root.right, target.right)
        self.assertEqual(root.left.left.val, target.left.left.val)


# 层次遍历一棵树，返回一维数组
def levelOrder(root: TreeNode):
    res = []
    if not root:
        return res
    my_stack = [root]
    while my_stack:
        new_stack = []
        if set(my_stack) == set([None]):
            break
        for node in my_stack:
            if node:
                res.append(node.val)
                if node.left:
                    new_stack.append(node.left)
                else:
                    new_stack.append(None)
                if node.right:
                    new_stack.append(node.right)
                else:
                    new_stack.append(None)
            else:
                res.append(null)
        my_stack = new_stack
    while res[-1] is None:
        res.pop()
    return res


# 使用Morris算法中序遍历一棵二叉树
def morris_inorder(root: TreeNode) -> List[Any]:
    res = []
    while root:
        if root.left:
            predecessor = root.left
            while predecessor.right and predecessor.right != root:
                predecessor = predecessor.right
            if predecessor.right is None:
                # create link ,then go to left
                predecessor.right = root
                root = root.left
            else:
                # cut link, go right
                predecessor.right = None
                res.append(root.val)
                root = root.right
        else:
            # no left , go right
            res.append(root.val)
            root = root.right
    return res

class TestMorrisInOrder(TestCase):
    def test_simple(self):
        root = generate_tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        self.assertEqual(morris_inorder(root), [8, 4, 9, 2, 10, 5, 1, 6, 3, 7])


class TestLevelOrder(TestCase):
    def test_simple(self):
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)
        target = levelOrder(root)
        self.assertEqual(target, [0, 1, 2])

    def test_none(self):
        root = None
        target = levelOrder(root)
        self.assertEqual(target, [])

    def test_with_null(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        target = levelOrder(root)
        self.assertEqual(target, [1, null, 2])

    def test_complex(self):
        root = TreeNode(1)
        root.left = TreeNode(401)
        root.left.left = TreeNode(349)
        root.left.right = TreeNode(88)
        root.left.left.left = TreeNode(90)

        target = levelOrder(root)
        self.assertEqual(target, [1, 401, null, 349, 88, 90])


if __name__ == '__main__':
    main()
