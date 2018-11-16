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


def minimax(node, depth, maximazing):
        if depth == 0:
            return node.value

        if maximazing:
            bestValue = -9999999
            val =  minimax(node.left, depth - 1, False)
            bestValue = max(bestValue, val)
            val = minimax(node.right, depth - 1, False)
            bestValue = max(bestValue, val)
            return bestValue

        bestValue = +9999999
        val = minimax(node.left, depth - 1, True)
        bestValue = min(bestValue, val)
        val = minimax(node.right, depth - 1, True)
        bestValue = min(bestValue, val)
        return bestValue


def testMiniMax():
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

    print(minimax(root, 4, True))
    printTree(root)
    print()


if __name__ == "__main__":
    testMiniMax()
