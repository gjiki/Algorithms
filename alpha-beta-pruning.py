from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def printTree(root):
    buf = deque()
    output = []
    if not root:
        print('$')
    else:
        buf.append(root)
        count, nextCount = 1, 0
        while count:
            node = buf.popleft()
            if node:
                output.append(node.value)
                count -= 1
                for n in (node.left, node.right):
                    if n:
                        buf.append(n)
                        nextCount += 1
                    else:
                        buf.append(None)
            else:
                output.append('$')
            if not count:
                print(output)
                output = []
                count, nextCount = nextCount, 0
        # print the remaining all empty leaf node part
        output.extend(['$']*len(buf))
        print(output)


def alpha_beta(node, depth, a, b, maximazing):
    if depth == 0:
        return node.value

    if maximazing:
        value = -9999999
        value = max(value, alpha_beta(node.left, depth - 1, a, b, False))
        a = max(a, value)

        if a >= b:
            return value

        value = max(value, alpha_beta(node.right, depth - 1, a, b, False))
        return value

    value = +9999999
    value = min(value, alpha_beta(node.left, depth - 1, a, b, True))
    b = min(b, value)

    if a >= b:
        return value

    value = min(value, alpha_beta(node.right, depth - 1, a, b, True))
    return value


def testAlphaBetaPruning():
    root = Node(0)

    root.left = Node(0)
    root.right = Node(0)

    root.left.left = Node(0)
    root.left.right = Node(0)
    root.right.left = Node(0)
    root.right.right = Node(0)

    root.left.left.left = Node(0)
    root.left.left.right = Node(0)
    root.left.right.left = Node(0)
    root.left.right.right = Node(0)
    root.right.left.left = Node(0)
    root.right.left.right = Node(0)
    root.right.right.left = Node(0)
    root.right.right.right = Node(0)

    root.left.left.left.left = Node(3)
    root.left.left.left.right = Node(10)
    root.left.left.right.left = Node(2)
    root.left.left.right.right = Node(9)
    root.left.right.left.left = Node(10)
    root.left.right.left.right = Node(7)
    root.left.right.right.left = Node(5)
    root.left.right.right.right = Node(9)
    root.right.left.left.left = Node(2)
    root.right.left.left.right = Node(5)
    root.right.left.right.left = Node(6)
    root.right.left.right.right = Node(4)
    root.right.right.left.left = Node(2)
    root.right.right.left.right = Node(7)
    root.right.right.right.left = Node(9)
    root.right.right.right.right = Node(1)

    print(alpha_beta(root, 4, +9999999, -9999999, True))
    printTree(root)


if __name__ == "__main__":
    testAlphaBetaPruning()
