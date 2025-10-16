import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
class Planet:
    def __init__(self, name, diameter_km, period_days, orbit_au, color):
        self.name = name
        self.diameter_km = diameter_km
        self.period_days = period_days
        self.orbit_au = orbit_au
        self.color = color
        self.omega = 2 * np.pi / self.period_days
        self.angle = 0.0
        self.size = (np.sqrt(self.diameter_km) * 0.02) ** 2
    def position(self, days):
        angle = self.omega * days
        x = self.orbit_au * np.cos(angle)
        y = self.orbit_au * np.sin(angle)
        return x, y
class SolarSystem:
    def __init__(self, days_per_frame=10, num_frames=600, interval_ms=50):
        self.days_per_frame = days_per_frame
        self.num_frames = num_frames
        self.interval_ms = interval_ms
        names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
        diameters_km = [4880, 12140, 12756, 6796, 142984, 120536, 51118, 49576]
        periods = [88, 224, 365, 687, 4307, 10767, 30660, 60152]
        orbits = [0.387, 0.723, 1.000, 1.524, 5.203, 9.582, 19.201, 30.047]
        colors = ["darkgray", "goldenrod", "royalblue", "orangered",
                  "sandybrown", "khaki", "skyblue", "cornflowerblue"]
        self.planets = [Planet(n, d, p, o, c) for n, d, p, o, c in zip(names, diameters_km, periods, orbits, colors)]
        self.max_orbit = max(orbits)
        self.margin = 1.2
        self.fig, self.ax = plt.subplots(figsize=(8, 8))
        self.ax.set_facecolor("black")
        self.ax.set_aspect("equal", 'box')
        self.ax.set_xlim(-self.max_orbit * self.margin, self.max_orbit * self.margin)
        self.ax.set_ylim(-self.max_orbit * self.margin, self.max_orbit * self.margin)
        self.ax.set_xticks([]);
        self.ax.set_yticks([])
        self.sun = plt.Circle((0, 0), 0.3, color="yellow", zorder=3)
        self.ax.add_patch(self.sun)
        theta = np.linspace(0, 2 * np.pi, 400)
        for planet in self.planets:
            r = planet.orbit_au
            self.ax.plot(r * np.cos(theta), r * np.sin(theta),
                         linestyle='--', linewidth=0.6, color='white', alpha=0.3)
        xs = [p.orbit_au for p in self.planets]
        ys = [0 for _ in self.planets]
        sizes = [p.size for p in self.planets]
        colors = [p.color for p in self.planets]
        self.scat = self.ax.scatter(xs, ys, s=sizes, c=colors, edgecolors='k', zorder=4)
        self.texts = [self.ax.text(xs[i], ys[i], " " + self.planets[i].name, color='white', fontsize=8)
                      for i in range(len(self.planets))]

        # 显示时间
        self.time_display = self.ax.text(-self.max_orbit * self.margin * 0.95,
                                         self.max_orbit * self.margin * 0.95,
                                         "", color='white', fontsize=10)
    def update(self, frame):
        days = frame * self.days_per_frame
        xs, ys = [], []
        for i, planet in enumerate(self.planets):
            x, y = planet.position(days)
            xs.append(x);
            ys.append(y)
            self.texts[i].set_position((x + 0.06 * (1 if x >= 0 else -1), y + 0.06))
        self.scat.set_offsets(np.c_[xs, ys])
        # self.time_display.set_text(f"Simulated days: {int(days)}")
        return self.scat, *self.texts, self.time_display
    def animate(self):
        self.anim = FuncAnimation(self.fig, self.update, frames=self.num_frames,
                                  interval=self.interval_ms, blit=True)
        plt.title("Solar System Simulation (OOP version)", color='white')
        plt.show()
if __name__ == "__main__":
    system = SolarSystem()
    system.animate()
