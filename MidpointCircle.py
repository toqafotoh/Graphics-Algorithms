import matplotlib.pyplot as plt

def draw_circle(radius):

    x, y = 0, radius
    d = 1 - radius


    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axhline(0, color='black')
    ax.axvline(0, color='black')

    # Add grid cells
    for i in range(-radius, radius+1):
        ax.axhline(i, color='gray', lw=0.7, ls='-')
        ax.axvline(i, color='gray', lw=0.7, ls='-')

    while y >= x:
        ax.scatter(x, y, color='red', s=20)
        ax.scatter(y, x, color='red', s=20)   
        ax.scatter(y, -x, color='red', s=20) 
        ax.scatter(x, -y, color='red', s=20) 
        ax.scatter(-x, -y, color='red', s=20) 
        ax.scatter(-y, -x, color='red', s=20)
        ax.scatter(-y, x, color='red', s=20)  
        ax.scatter(-x, y, color='red', s=20)  


        # Update x based on the decision parameter
        # if d < 0:
        #     d += 2*x +3
        # else:
        #     d += 2*(x-y)+5
        #     y -= 1

        # x += 1        
        if d < 0:
            d += 2*x +1
        else:
            d += 2*x + 1 - 2*y
            y -= 1

        x += 1


    plt.plot([0, radius], [0, -radius], color='black', lw=0.7) 
    plt.plot([0, -radius], [0,-radius], color='black', lw=0.7)  
    plt.plot([0, radius], [0, radius], color='black', lw=0.7)  
    plt.plot([0, -radius], [0,radius], color='black', lw=0.7)  

    circle = plt.Circle((0, 0), radius, color='black', fill=False)
    ax.add_artist(circle)


 
    plt.show()

radius = 15
draw_circle(radius)
