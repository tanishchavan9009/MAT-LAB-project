# ∂ Partial Derivative Solver & Multivariable Calculus Suite

<div align="center">

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![SymPy](https://img.shields.io/badge/SymPy-Symbolic%20Math-3B5526?style=for-the-badge)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%203D-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

<p align="center">
  <b>A state-of-the-art computational calculus workbench and interactive 3D visualizer built with Streamlit, SymPy, Plotly, and Math.js.</b>
</p>

[✨ Live Demo](#-deployment-to-streamlit-community-cloud) • [⚡ Key Features](#-key-features) • [🚀 Quick Start](#-local-installation--quick-start) • [📖 Mathematics Guide](#-mathematical-capabilities) • [🌐 Deploy to Streamlit](#-deployment-to-streamlit-community-cloud)

---

</div>

## 🌟 Highlights

- 🧠 **Exact Symbolic Calculus Engine**: Computes exact symbolic partial derivatives of any order ($1^{\text{st}}, 2^{\text{nd}}, 3^{\text{rd}}, 4^{\text{th}}$) powered by SymPy and Math.js.
- 📜 **Step-by-Step Derivation Breakdown**: Clearly explains differentiation rules step-by-step (Power, Chain, Product, Quotient rules) with constant-variable isolation.
- 🌐 **Interactive 3D Response Surface Visualizer**: 360° rotatable 3D surface charts with customizable color themes, real-time tangent planes, and 2D contour slices.
- 🧭 **Gradient Flow Quiver Fields**: Visualizes $\nabla f$ vector arrows directly on 2D contour level sets to show steepest ascent paths.
- ⚡ **Multivariable Vector Calculus Suite**:
  - Gradient Vector $\nabla f$
  - Hessian Matrix $H(f)$ & Determinant $|H|$
  - Second Derivative Test Extrema Classification (Local Min / Max / Saddle Point)
  - Clairaut's / Schwarz's Mixed Partials Theorem Verification ($\frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}$)
  - Laplacian Operator $\nabla^2 f$ & Harmonic Function Detection ($\nabla^2 f = 0$)
  - Directional Derivatives $D_{\mathbf{u}} f = \nabla f \cdot \mathbf{u}$ along arbitrary vectors
  - Tangent Plane Equations & Linear Approximations
- 🔢 **Numeric Point Evaluator**: Evaluate $f$, slopes, gradient magnitudes, and directional rates of change at any custom coordinates.
- 📋 **Multi-Format Export**: One-click export for LaTeX math code, Python SymPy code, and plain string formulas.
- 🎨 **Cyberpunk Glassmorphism UI**: High-contrast, dark-mode design with glowing badges, smooth animations, and responsive layout.

---

## 🗂️ Project Structure

```
.
├── .streamlit/
│   └── config.toml          # Custom dark cyberpunk UI theme config for Streamlit
├── app.py                   # Production-grade Streamlit application
├── partial.html             # Standalone client-side HTML5/JS Calculus UI
├── requirements.txt         # Python dependencies for local run and Streamlit Cloud
└── README.md                # Comprehensive documentation & deployment guide
```

---

## 🚀 Local Installation & Quick Start

### 1. Prerequisites
Ensure you have Python 3.9+ installed on your system.

### 2. Clone or Navigate to the Workspace
```bash
cd "C:\Users\tanis\OneDrive\Desktop\Tanish codes\MATLAB"
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit Application
```bash
streamlit run app.py
```
Your default browser will automatically open:
```
Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

---

## ☁️ Deployment to Streamlit Community Cloud

Deploying this application online for free takes less than 2 minutes:

### Step 1: Push Code to GitHub
1. Initialize a git repository and push your project:
   ```bash
   git init
   git add .
   git commit -m "Initial commit of Partial Derivative Solver"
   git branch -M main
   git remote add origin https://github.com/<YOUR-USERNAME>/<YOUR-REPO-NAME>.git
   git push -u origin main
   ```

### Step 2: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io/) and sign in with your GitHub account.
2. Click **"New app"**.
3. Select your repository: `<YOUR-USERNAME>/<YOUR-REPO-NAME>`.
4. Set the **Main file path** to: `app.py`.
5. Click **"Deploy!"**.

Streamlit Cloud will read `requirements.txt` and `.streamlit/config.toml` automatically, launch your live web app, and provide a public URL (e.g. `https://your-app-name.streamlit.app/`) to share with anyone!

---

## 📖 Mathematical Capabilities

### 1. Partial Derivatives
For a multivariable function $f(x_1, x_2, \dots, x_n)$, the partial derivative with respect to $x_i$ holds all other variables constant:
$$\frac{\partial f}{\partial x_i} = \lim_{h \to 0} \frac{f(x_1, \dots, x_i + h, \dots, x_n) - f(x_1, \dots, x_i, \dots, x_n)}{h}$$

### 2. Gradient Vector
$$\nabla f(x, y, z) = \begin{bmatrix} \frac{\partial f}{\partial x} \\ \frac{\partial f}{\partial y} \\ \frac{\partial f}{\partial z} \end{bmatrix}$$
The gradient vector points in the direction of steepest ascent, with magnitude $\|\nabla f\|$ representing the maximum rate of change.

### 3. Hessian Matrix & Critical Point Classification
$$H(x, y) = \begin{bmatrix} \frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\ \frac{\partial^2 f}{\partial y \partial x} & \frac{\partial^2 f}{\partial y^2} \end{bmatrix}$$
- If $\det(H) > 0$ and $f_{xx} > 0$: **Local Minimum**
- If $\det(H) > 0$ and $f_{xx} < 0$: **Local Maximum**
- If $\det(H) < 0$: **Saddle Point**
- If $\det(H) = 0$: **Inconclusive Test**

### 4. Tangent Plane
The tangent plane to $z = f(x, y)$ at point $(x_0, y_0, z_0)$ is:
$$z - z_0 = f_x(x_0, y_0)(x - x_0) + f_y(x_0, y_0)(y - y_0)$$

---

## ⚡ Built-in Presets Included

| Preset Name | Function Formula | Mathematical Feature |
| :--- | :--- | :--- |
| **Sum of Squares** | $x^2 + y^2 + z^2$ | Paraboloid with global minimum at origin |
| **Trig Wave** | $\sin(x)\cos(y)$ | Periodic peaks, valleys, and saddle grids |
| **Exponential Mixture** | $x^2 y + e^{xy}$ | Coupled polynomial and exponential growth |
| **Hyperbolic Saddle** | $x^2 - y^2$ | Classic saddle surface with negative Hessian determinant |
| **Gaussian Bell** | $\exp(-(x^2 + y^2))$ | Radial distribution in physics and probability |
| **Rosenbrock Valley** | $(1-x)^2 + 100(y-x^2)^2$ | Classic non-convex optimization benchmark |
| **Monkey Saddle** | $x^3 - 3xy^2$ | Triple-fluted saddle surface |

---

## 🛡️ License

Distributed under the **MIT License**. Free for educational, commercial, and research use.
