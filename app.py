import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BarycentricInterpolator

class InteractivePolynomial:
    def __init__(self, points):
        self.points = np.array(points, dtype=float)
        self.validate_unique_x()
        
        self.fig, self.ax = plt.subplots(figsize=(9, 6))
        self.ax.set_title("Interactive Polynomial Interpolation\n(Click & drag points to edit)")
        
        self.curve, = self.ax.plot([], [], 'b-', lw=2, label="f(x)")
        self.point_plot, = self.ax.plot(self.points[:, 0], self.points[:, 1], 'ro', ms=8, label="Control Points")
        
        self.selected_idx = None
        self.annotations = []
        
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)
        
        self.ax.grid(True)
        self.ax.legend()
        self.update_plot()
        
    def validate_unique_x(self):
        x_vals = self.points[:, 0]
        if len(np.unique(x_vals)) < len(x_vals):
            for i in range(1, len(x_vals)):
                while np.any(np.isclose(self.points[i, 0], self.points[:i, 0], atol=1e-2)):
                    self.points[i, 0] += 0.05

    def on_press(self, event):
        if event.inaxes != self.ax:
            return
        dists = np.hypot(self.points[:, 0] - event.xdata, self.points[:, 1] - event.ydata)
        min_idx = np.argmin(dists)
        if dists[min_idx] < 0.4:
            self.selected_idx = min_idx

    def on_motion(self, event):
        if self.selected_idx is None or event.inaxes != self.ax:
            return
        
        new_x, new_y = event.xdata, event.ydata
        other_x = np.delete(self.points[:, 0], self.selected_idx)
        if np.any(np.abs(other_x - new_x) < 0.05):
            return  
            
        self.points[self.selected_idx] = [new_x, new_y]
        self.update_plot()

    def on_release(self, event):
        self.selected_idx = None

    def update_plot(self):
        x_vals = self.points[:, 0]
        y_vals = self.points[:, 1]
        
        poly = BarycentricInterpolator(x_vals, y_vals)
        x_grid = np.linspace(min(x_vals) - 1.5, max(x_vals) + 1.5, 500)
        y_grid = poly(x_grid)
        
        self.curve.set_data(x_grid, y_grid)
        self.point_plot.set_data(x_vals, y_vals)
        
        for txt in self.annotations:
            txt.remove()
        self.annotations.clear()
        
        for (x, y) in zip(x_vals, y_vals):
            txt = self.ax.annotate(f"({x:.2f}, {y:.2f})", (x, y), 
                                   textcoords="offset points", xytext=(0,10), ha='center')
            self.annotations.append(txt)
            
        self.ax.relim()
        self.ax.autoscale_view()
        self.fig.canvas.draw_idle()

# النقاط الأولية من المسألة
initial_points = [
    [0.0, 1.080],
    [1.0, 1.693],
    [2.0, 0.715],
    [3.0, -0.505],
    [4.0, 0.109]
]

plotter = InteractivePolynomial(initial_points)
plt.show()