import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


class Ball:
    def __init__(self,color,width,height):
        self.color=color
        self.width=width
        self.height=height
        self.reset()
    def reset(self):
        self.x=np.random.rand()*self.width
        self.y=np.random.rand()*self.height
        self.radius=0.1
        self.wait_time=np.random.rand()*4
        self.growth_speed=0.5
        self.growth_duration=np.random.rand()*4+3
        self.growth_time=0
        self.transparency=0.1
        self.is_visible=True
        self.is_growing = False
    def update(self,dt):
        if not self.is_visible:
            self.reset()
        if not self.is_growing:
            self.wait_time-=dt
            if self.wait_time<=0:
                self.is_growing=True
        else:
            self.growth_time+=dt
            self.radius+=self.growth_speed*dt
            self.transparency=min(0.9,0.05+(self.radius/1.0)*1.0)
        if self.growth_time>=np.random.rand()*4:
            self.is_visible=False
    def draw(self,ax):
        if not self.is_visible:
            return None
        circle=plt.Circle((self.x,self.y),self.radius,
                          facecolor=self.color,fill=True,
                          alpha=self.transparency,edgecolor='none')
        ax.add_patch(circle)
        return circle
if __name__=='__main__':
    width,height=10,10
    fig,ax=plt.subplots(facecolor='black')
    ax.set_xlim(0,width)
    ax.set_ylim(0,height)
    ax.set_aspect('equal','box')
    for spine in ax.spines.values():
        spine.set_color('white')
        spine.set_linewidth(1)
    colors=['orange','green','blue','red','yellow','cyan',
            'purple','gray','brown','pink','lime','magenta']
    balls=[Ball(color,width,height)for color in colors]
    patches=[]
    def animate(frame):
        dt=0.05
        ax.clear()
        ax.set_xlim(0,width)
        ax.set_ylim(0,height)
        ax.set_facecolor('black')
        ax.set_aspect('equal','box')
        for spine in ax.spines.values():
            spine.set_color('white')
            spine.set_linewidth(1)
        patches.clear()
        for ball in balls:
            ball.update(dt)
            patch = ball.draw(ax)
            if patch:
                patches.append(patch)
        return patches
    # ani = animation.FuncAnimation(fig, animate, frames=None, interval=50, blit=True)
    ani = animation.FuncAnimation(fig, animate, frames=100, interval=50, blit=True)
    # ani.save('animation.gif', writer='pillow', fps=30)
    plt.show()