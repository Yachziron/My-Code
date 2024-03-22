class Circle:
    pi = 3.14

    def calculate_area(self, radius):
        self.radius = radius
        self.S = self.pi * radius ** 2
        return self.S


code = []
while data := input():
    code.append(data)
code = "\n".join(code)
exec(code)
