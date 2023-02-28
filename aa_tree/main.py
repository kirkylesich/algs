#!/usr/bin/env python3

class Node:
    def __init__(self, x, left, right, level=1):
        self.val = x
        self.left = left
        self.right = right
        self.level = level


class Tree:
    def __init__(self):
        self.root = None
    def insert(self, x):
        """inserts x into tree"""
        if self.root is None:
            self.root = Node(x, None, None)
        else:
            p = self.root
            q = self.root
            while p is not None:
                q = p
                if x < p.val:
                    p = p.left
                else:
                    p = p.right
            if x < q.val:
                q.left = Node(x, None, None)
            else:
                q.right = Node(x, None, None)
    def lookup(self, x) -> bool:
        """returns, whether x is in tree"""
        p = self.root
        while p is not None:
            if p.val == x:
                return True
            elif x < p.val:
                p = p.left
            else:
                p = p.right
        return False

    def print_tree(self):
        """
        print_tree outputs a tree in the following format:

        3
          2
            1
              None
              None
            None
          5
            4
              None
              None
            6
              None
              None
        """
        stack = list()
        stack.append({'node': self.root, 'level': 0})
        while len(stack) > 0:
            cur = stack.pop()
            level = cur['level']
            node = cur['node']
            indentation = ''.join([' ' for _ in range(2*level)])
            if node is not None:
                print(indentation, node.val)
                stack.append({'node': node.right, 'level': level+1})
                stack.append({'node': node.left, 'level': level+1})
            else:
                print(indentation, 'None')

class AATree(Tree):
    def __init__(self):
        self.root = None

    def skew(self, node):
        if node is None or node.left is None:
            return node
        if node.level == node.left.level:
            temp = node.left
            node.left = temp.right
            temp.right = node
            return temp
        return node

    def split(self, node):
        if node is None or node.right is None or node.right.right is None:
            return node
        if node.level == node.right.right.level:
            temp = node.right
            node.right = temp.left
            temp.left = node
            temp.level += 1
            return temp
        return node

    def insert(self, x):
        def insert_helper(node, x):
            if node is None:
                return Node(x, None, None, 1)

            if x < node.val:
                node.left = insert_helper(node.left, x)
            else:
                node.right = insert_helper(node.right, x)

            node = self.skew(node)
            node = self.split(node)

            return node

        self.root = insert_helper(self.root, x)

    def delete(self, x):
        def delete_helper(node, x):
            if node is None:
                return node

            if x < node.val:
                node.left = delete_helper(node.left, x)
            elif x > node.val:
                node.right = delete_helper(node.right, x)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                min_node = node.right
                while min_node.left is not None:
                    min_node = min_node.left

                node.val = min_node.val
                node.right = delete_helper(node.right, min_node.val)

            if node is not None:
                if node.left is not None and node.right is not None:
                    if node.left.level < node.level - 1 or node.right.level < node.level - 1:
                        node.level -= 1
                        if node.right.level > node.level:
                            node.right.level = node.level
                        node = self.skew(node)
                        node.right = self.skew(node.right)
                        node.right.right = self.skew(node.right.right)
                        node = self.split(node)
                        node.right = self.split(node.right)

            return node

        self.root = delete_helper(self.root, x)

    def lookup(self, x) -> bool:
        """Returns whether x is in tree"""
        p = self.root
        while p is not None:
            if p.val == x:
                return True
            elif x < p.val:
                p = p.left
            else:
                p = p.right
        return False

    def min(self):
        """Returns the minimum value in the tree"""
        if self.root is None:
            return None

        p = self.root
        while p.left is not None:
            p = p.left

        return p.val

    def max(self):
        """Returns the maximum value in the tree"""
        if self.root is None:
            return None

        p = self.root
        while p.right is not None:
            p = p.right

        return p.val
    
    def pred(self, x):
        """Returns the predecessor of x"""
        pred_val = None
        p = self.root

        while p is not None:
            if x <= p.val:
                p = p.left
            else:
                pred_val = p.val
                p = p.right

        return pred_val

    def succ(self, x):
        """Returns the successor of x"""
        succ_val = None
        p = self.root

        while p is not None:
            if x >= p.val:
                p = p.right
            else:
                succ_val = p.val
                p = p.left

        return succ_val



if __name__ == '__main__':
    tree = AATree()

    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(1)
    tree.insert(9)

    tree.print_tree()

    print(tree.lookup(7))  # True
    print(tree.lookup(10)) # False

    print(tree.min()) # 1
    print(tree.max()) # 9

    print(tree.pred(5)) # 3
    print(tree.succ(5)) # 7

    tree.delete(5)

    print("New tree")
    tree.print_tree()