class TopK:
    def __init__(self):
        self.c = {}

    def add(self, x):
        self.c[x] = self.c.get(x, 0) + 1

    def remove(self, x):
        if x in self.c:
            self.c[x] -= 1
            if self.c[x] == 0:
                del self.c[x]



    def top(self, k):
        return [x for x, _ in
                sorted(self.c.items(), key=lambda p: p[1], reverse=True)[:k]]