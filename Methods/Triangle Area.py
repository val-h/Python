base = float(input('Base: '))
height = float(input('Height: '))

def TriangleArea(b, h):
    return b * height / 2

print(f'The area of the triangle is: {TriangleArea(base, height):.2f}')
