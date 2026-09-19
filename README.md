# Interactive Polynomial Interpolation Tool

An interactive Python GUI application built with **Matplotlib**, **NumPy**, and **SciPy** to visualize polynomial curve fitting through control points in real time.

## Key Features
* **Interactive Drag & Drop:** Click and drag control points directly on the plot to dynamically recompute and redraw the polynomial curve.
* **Manual Point Coordinates:** Manually set exact $(X, Y)$ values for any control point via the control panel.
* **Duplicate $X$ Protection:** Built-in error handling that prevents duplicate $X$-coordinates to avoid division-by-zero errors in polynomial interpolation.
* **Live Equation Display:** Real-time formatting and rendering of the resulting interpolating polynomial equation $f(x)$.
* **Custom Point Estimation:** Input any $X$ value to instantly calculate and highlight $f(X)$ on the curve.
* **One-Click View Reset:** Easily restore the initial control points and axis limits.

## Installation & Setup

1. Clone or download this repository.
2. Install the required dependencies:
   ```bash
   pip install matplotlib numpy scipy
