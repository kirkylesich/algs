class Elem:
    def __init__(self, x: int, p):
        self.val = x
        self.next = p

class List:
    def __init__(self):
        self.head = None
        self.last = None

    def prepend(self, x: int):
        self.head = Elem(x, self.head)
        if self.last is None:
            self.last = self.head

    def append(self, x: int):
        if self.head is None:
            self.head = Elem(x, None)
            self.last = self.head
        else:
            self.last.next = Elem(x, None)
            self.last = self.last.next

    def __str__(self):
        delimiter = " "
        values = []
        p = self.head
        while p is not None:
            values.append(str(p.val))
            p = p.next
        return delimiter.join(values)

    def length(self) -> int:
        n = 0
        p = self.head
        while p is not None:
            n = n+1
            p = p.next
        return n