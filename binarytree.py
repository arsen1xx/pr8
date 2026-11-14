class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.length = 0

    def add(self, data):
        node = Node(data)
        self.length += 1

        if self.root is None:
            self.root = node
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left is None:
                    current.left = node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                current = current.right

    def contains(self, data):
        current = self.root
        while current is not None:
            if data == current.data:
                return True
            current = current.left if data < current.data else current.right
        return False

    def remove(self, data):
        if not self.contains(data):
            return False
        self.root = self._remove(self.root, data)
        self.length -= 1
        return True

    def _remove(self, node, data):
        if data < node.data:
            node.left = self._remove(node.left, data)
        elif data > node.data:
            node.right = self._remove(node.right, data)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            successor = node.right
            while successor.left is not None:
                successor = successor.left

            node.data = successor.data
            node.right = self._remove(node.right, successor.data)
        return node

    def min_value(self):
        if self.root is None:
            raise IndexError("Дерево порожнє")
        current = self.root
        while current.left is not None:
            current = current.left
        return current.data

    def max_value(self):
        if self.root is None:
            raise IndexError("Дерево порожнє")
        current = self.root
        while current.right is not None:
            current = current.right
        return current.data

    def count(self):
        return self.length

    def to_list(self):
        result = []

        def walk(node):
            if node is None:
                return
            walk(node.left)
            result.append(node.data)
            walk(node.right)

        walk(self.root)
        return result

    def to_string(self):
        return "[" + ", ".join(str(x) for x in self.to_list()) + "]"

    def show(self):
        def walk(node, level):
            if node is None:
                return
            walk(node.right, level + 1)
            print("    " * level + str(node.data))
            walk(node.left, level + 1)

        walk(self.root, 0)

    def __str__(self):
        return self.to_string()


if __name__ == "__main__":
    tree = BinaryTree()

    for value in (3, 1, 9, 1, 7, 10, 6, 8):
        tree.add(value)

    print("Всі елементи:", tree)
    print("Кількість:", tree.count())
    print("Найменший:", tree.min_value())
    print("Найбільший:", tree.max_value())

    print("\nДерево (корінь ліворуч, більші згори):")
    tree.show()

    print("\ncontains(7):", tree.contains(7))
    print("contains(5):", tree.contains(5))

    print("\nremove(10), листок:", tree.remove(10))
    print(tree)

    print("\nremove(1), один нащадок:", tree.remove(1))
    print(tree)

    print("\nremove(3), корінь із двома нащадками:", tree.remove(3))
    print(tree)
    tree.show()

    print("\nremove(100), якого немає:", tree.remove(100))
    print("Кількість:", tree.count())
    print("Найменший:", tree.min_value())
    print("Найбільший:", tree.max_value())