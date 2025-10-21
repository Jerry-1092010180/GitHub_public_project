import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
class Planet:
    def __init__(self,name,dkm,t_day,orbit_r,color):
        self.name=name
        self.dkm=dkm
        self.t_day=t_day
        self.orbit_r=orbit_r
        self.color=color
        self.omega=2*np.pi/self.t_day
        self.angle=0.0
    def position(self,days):
        angle=self.omega*days
        x=self.orbit_r*np.cos(angle)
        y=self.orbit_r*np.sin(angle)
        return x,y
class SolarSystem:
    def __init__(self):
        names=["Mercury", "Venus", "Earth", "Mars",
               "Jupiter", "Saturn", "Uranus", "Neptune"]
        dkm=[4880, 12140, 12756, 6796,
             142984, 120536, 51118, 49576]
        t_day=[88, 224, 365, 687,
               4307, 10767, 30660, 60152]
        orbit_r=[1, 3, 5, 7,
                 9, 11, 13,15 ]
        colors = ["darkgray", "goldenrod", "royalblue", "orangered",
                  "sandybrown", "khaki", "skyblue", "cornflowerblue"]
        self.planets=[Planet(n,d,t,o,c)for n,d,t,o,c in zip(names,dkm,t_day,orbit_r,colors)]
        self.max_orbit=max(orbit_r)
        self.fig,self.ax=plt.subplots(figsize=(8,8))
        self.ax.set_facecolor('black')
        self.ax.set_aspect('equal','box')
        self.sun=plt.Circle((0,0),0.3,color='red')
        self.ax.add_patch(self.sun)
        theta=np.linspace(0,2*np.pi,666)
        for planet in self.planets:
            r=planet.orbit_r
            self.ax.plot(r*np.cos(theta),r*np.sin(theta),color='white',alpha=0.8)
        xs=[p.orbit_r for p in self.planets]
        ys=[0 for _ in self.planets]
        sizes=[p.dkm /500 for p in self.planets]
        colors=[p.color for p in self.planets]
        self.scat=self.ax.scatter(xs,ys,s=sizes,c=colors,edgecolors='k')
        self.texts=[self.ax.text(xs[i], ys[i], " "+self.planets[i].name, color='white', fontsize=8)
              for i in range(len(self.planets))]
    def update(self,frame):
        days=frame*10
        xs,ys=[],[]
        for i,planet in enumerate(self.planets):
            x,y=planet.position(days)
            xs.append(x)
            ys.append(y)
            self.texts[i].set_position((x + 0.06 * (1 if x >= 0 else -1), y + 0.06))
            self.scat.set_offsets(np.c_[xs, ys])
        return self.scat, *self.texts
if __name__ == "__main__":
    system = SolarSystem()
    ani = FuncAnimation(system.fig, system.update, frames=1000, interval=50, blit=True)
    plt.show()
