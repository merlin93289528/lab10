class Matrix:

    def __init__(self):
        self.matrix_el = []
        self.dimension = [0, 0]

    def enter_el(self):
        """Input of matrix elements"""
        print("Вводіть значення кожного рядка через пробіл(щоб завершити введення, введіть 0):\n")
        el = list(map(int, input().split(" ")))
        self.dimension[1] = len(el)
        self.matrix_el.append(el)
        while True:
            el = list(map(int, input().split(" ")))
            if len(el) > self.dimension[1] > len(el):
                print("Неправильна кількисть елементів рядка")
            elif el == [0]:
                break
            else:
                self.matrix_el.append(el)
        self.dimension[0] = len(self.matrix_el)

    def show_el(self):
        """Show elements"""
        for i in self.matrix_el:
            print(i)

    def maximum(self):
        """Find maximum element"""
        max_el = 0
        for el in self.matrix_el:
            if max(el) > max_el:
                max_el = max(el)
        return max_el

    def minimum(self):
        """Find minimum element"""
        min_el = 0
        for el in self.matrix_el:
            if min(el) > min_el:
                min_el = min(el)
        return min_el