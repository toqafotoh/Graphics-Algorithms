import matplotlib.pyplot as plt
def lineDDA(x0, y0, xEnd, yEnd):
    
    dx = xEnd - x0
    dy = yEnd - y0
    x, y = x0, y0

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)
    xIncrement = dx / steps
    yIncrement = dy / steps

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('DDA Algorithm')
    plt.grid(True) 
    print("DDA Line Points")
    for _ in range(steps):
        x += xIncrement
        y += yIncrement
        round_x,round_y= round(x),round(y)
        print(f"({round_x},{round_y})")
        plt.plot([round_x], [round_y], marker='*', color='red',markersize=10)

    plt.show()

lineDDA(2, 3, 9, 8)