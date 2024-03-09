import matplotlib.pyplot as plt

def lineBres(x0, y0, xEnd, yEnd):
    dx = abs(xEnd - x0)
    dy = abs(yEnd - y0)
    x, y = x0, y0
    p = 2 * dy - dx
    twoDy = 2 * dy
    twoDyMinusDx = 2 * (dy - dx)

    if x0 > xEnd:
        x, y, xEnd, yEnd = xEnd, yEnd, x0, y0

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Bresenham Algorithm')
    print("Bresenham Line Points")
    plt.grid(True) 
    while x < xEnd:
        x += 1
        if p < 0:
            p += twoDy
        else:
            y += 1
            p += twoDyMinusDx
        print(f"({x},{y})")
        plt.plot([x], [y], marker='*', color='red',markersize=10)

    plt.show()

lineBres(5, 8, 9, 11)
