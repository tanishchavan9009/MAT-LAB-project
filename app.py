"""
∂ Partial Derivative & Multivariable Calculus Suite
A production-grade Streamlit web application for symbolic differentiation,
vector calculus, 3D surface visualization, and step-by-step calculus exploration.
"""

import streamlit as st
import sympy as sp
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import re

# Set page configuration
st.set_page_config(
    page_title="∂ Partial Derivative Solver & 3D Visualizer",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-End Cyberpunk / Modern Dark UI Theme CSS
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Space+Mono:ital,wght@0,400;0,700;1,400&family=Syne:wght@400;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

    :root {
        --bg: #07070d;
        --card: #11111a;
        --card2: #181826;
        --border: rgba(138, 108, 255, 0.22);
        --primary: #8a6cff;
        --primary-glow: rgba(138, 108, 255, 0.4);
        --secondary: #ff6ca8;
        --green: #65ffd0;
        --text: #f3f1ff;
        --muted: #9490b8;
    }

    /* Base Styling */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: var(--text);
    }
    
    .stApp {
        background-color: #07070d;
        background-image: 
            radial-gradient(at 0% 0%, rgba(138, 108, 255, 0.12) 0px, transparent 50%),
            radial-gradient(at 100% 100%, rgba(255, 108, 168, 0.08) 0px, transparent 50%),
            linear-gradient(rgba(125, 108, 255, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(125, 108, 255, 0.03) 1px, transparent 1px);
        background-size: 100% 100%, 100% 100%, 40px 40px, 40px 40px;
    }

    /* Hero Header Styling */
    .hero-container {
        text-align: center;
        padding: 30px 10px 20px;
        position: relative;
    }
    
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        background: rgba(138, 108, 255, 0.1);
        border: 1px solid rgba(138, 108, 255, 0.35);
        color: #a78bfa;
        padding: 6px 16px;
        border-radius: 9999px;
        font-family: 'Space Mono', monospace;
        font-size: 0.78rem;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 15px;
        box-shadow: 0 0 15px rgba(138, 108, 255, 0.15);
    }

    .badge-dot {
        width: 8px;
        height: 8px;
        background-color: #65ffd0;
        border-radius: 50%;
        box-shadow: 0 0 8px #65ffd0;
        animation: pulse 2s infinite;
    }

    @keyframes pulse {
        0%, 100% { transform: scale(1); opacity: 1; }
        50% { transform: scale(0.7); opacity: 0.5; }
    }

    .hero-title {
        font-family: 'Syne', sans-serif;
        font-size: 2.8rem;
        font-weight: 800;
        line-height: 1.1;
        letter-spacing: -1.5px;
        margin-bottom: 10px;
        background: linear-gradient(135deg, #ffffff 30%, #c4b5fd 70%, #ff6ca8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        color: var(--muted);
        font-size: 1.05rem;
        max-width: 700px;
        margin: 0 auto 20px;
        line-height: 1.6;
    }

    /* Glass Cards */
    .glass-card {
        background: rgba(17, 17, 26, 0.75);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(138, 108, 255, 0.2);
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
        transition: transform 0.2s ease, border-color 0.2s ease;
    }

    .glass-card:hover {
        border-color: rgba(138, 108, 255, 0.4);
    }

    .card-title {
        font-family: 'Space Mono', monospace;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #65ffd0;
        margin-bottom: 15px;
        display: flex;
        align-items: center;
        gap: 8px;
    }

    .result-display {
        background: #181826;
        border: 1px solid rgba(101, 255, 208, 0.25);
        border-radius: 14px;
        padding: 20px;
        margin: 15px 0;
        box-shadow: inset 0 0 20px rgba(0,0,0,0.4);
    }

    /* Custom Step Container */
    .step-box {
        display: flex;
        align-items: flex-start;
        gap: 15px;
        padding: 12px 16px;
        margin-bottom: 10px;
        background: rgba(24, 24, 38, 0.6);
        border: 1px solid rgba(138, 108, 255, 0.15);
        border-radius: 12px;
        font-family: 'Space Mono', monospace;
        font-size: 0.9rem;
    }

    .step-num {
        background: rgba(138, 108, 255, 0.2);
        color: #a78bfa;
        border: 1px solid rgba(138, 108, 255, 0.4);
        border-radius: 8px;
        padding: 3px 8px;
        font-size: 0.75rem;
        font-weight: 700;
        min-width: 32px;
        text-align: center;
    }

    /* Metric pill */
    .stat-pill {
        display: inline-block;
        background: rgba(255, 108, 168, 0.1);
        border: 1px solid rgba(255, 108, 168, 0.3);
        color: #ff8ebb;
        padding: 4px 12px;
        border-radius: 8px;
        font-family: 'Space Mono', monospace;
        font-size: 0.82rem;
        margin-right: 8px;
        margin-bottom: 8px;
    }

    /* Custom button overrides */
    div.stButton > button {
        background: linear-gradient(135deg, #8a6cff, #a87dff);
        color: #ffffff;
        font-weight: 600;
        border: none;
        border-radius: 12px;
        padding: 10px 24px;
        transition: all 0.25s ease;
        box-shadow: 0 4px 20px rgba(138, 108, 255, 0.3);
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 30px rgba(138, 108, 255, 0.5);
        color: #ffffff;
    }

    /* Inputs */
    div[data-baseweb="input"] {
        background-color: #181826 !0mportant;
        border-radius: 12px;
        border-color: rgba(138, 108, 255, 0.25);
    }

    /* Streamlit tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: #11111a;
        padding: 6px;
        border-radius: 14px;
        border: 1px solid rgba(138, 108, 255, 0.15);
    }

    .stTabs [data-baseweb="tab"] {
        border-radius: 10px;
        color: #9490b8;
        padding: 8px 18px;
        font-family: 'Space Mono', monospace;
        font-size: 0.85rem;
    }

    .stTabs [aria-selected="true"] {
        background: rgba(138, 108, 255, 0.18) !important;
        color: #c4b5fd !important;
        border: 1px solid rgba(138, 108, 255, 0.35) !important;
    }
</style>
""", unsafe_allow_html=True)


# Helper: Parse user math string safely into SymPy
def sanitize_expression(expr_str: str) -> str:
    """Preprocess common human mathematical notations into standard SymPy syntax."""
    s = expr_str.strip()
    if not s:
        return ""
    # Replace Greek theta with theta
    s = s.replace("θ", "theta").replace("π", "pi")
    # Replace ^ with **
    s = s.replace("^", "**")
    # Replace ln with log
    s = re.sub(r'\bln\b', 'log', s)
    # Replace e^(...) or e^x with exp(...)
    s = re.sub(r'\be\^\((.*?)\)', r'exp(\1)', s)
    s = re.sub(r'\be\*\*([a-zA-Z0-9]+)', r'exp(\1)', s)
    s = re.sub(r'\be\^([a-zA-Z0-9]+)', r'exp(\1)', s)
    # Handle implicit multiplication like 2x -> 2*x, 3y -> 3*y, x y -> x*y (carefully)
    s = re.sub(r'(\d)([a-zA-Z\(])', r'\1*\2', s)
    s = re.sub(r'(\))([a-zA-Z0-9\(])', r'\1*\2', s)
    return s


def parse_to_sympy(expr_str: str):
    """Parse math string to sympy expression with predefined symbols."""
    x, y, z, t, r, theta, u, v, w = sp.symbols('x y z t r theta u v w', real=True)
    local_dict = {
        'x': x, 'y': y, 'z': z, 't': t, 'r': r, 'theta': theta,
        'u': u, 'v': v, 'w': w, 'e': sp.E, 'pi': sp.pi, 'E': sp.E,
        'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan, 'cot': sp.cot,
        'sec': sp.sec, 'csc': sp.csc, 'asin': sp.asin, 'acos': sp.acos,
        'atan': sp.atan, 'sinh': sp.sinh, 'cosh': sp.cosh, 'tanh': sp.tanh,
        'exp': sp.exp, 'log': sp.log, 'ln': sp.log, 'sqrt': sp.sqrt,
        'abs': sp.Abs
    }
    cleaned = sanitize_expression(expr_str)
    return sp.parse_expr(cleaned, local_dict=local_dict, evaluate=False)


# Render Header
st.markdown("""
<div class="hero-container">
    <div class="badge">
        <span class="badge-dot"></span>
        Multivariable Calculus & Vector Analysis Suite
    </div>
    <div class="hero-title">∂ Partial Derivative Solver</div>
    <p class="hero-subtitle">
        Compute symbolic partial derivatives of any order, examine step-by-step calculus derivations,
        analyze Hessian matrices & gradients, and explore interactive 3D response surfaces.
    </p>
</div>
""", unsafe_allow_html=True)


# Sidebar Configuration & Preset Selection
with st.sidebar:
    st.markdown("### 🎛️ Control Panel")
    
    preset = st.selectbox(
        "⚡ Quick Presets & Engineering Models",
        [
            "Custom Expression",
            "Sum of Squares: x^2 + y^2 + z^2",
            "Trig Product: sin(x) * cos(y)",
            "Exponential Mixture: x^2*y + e^(x*y)",
            "Hyperbolic Saddle: x^2 - y^2",
            "Gaussian Bell Surface: exp(-(x^2 + y^2))",
            "Rosenbrock Valley: (1 - x)^2 + 100*(y - x^2)^2",
            "Logarithmic Potential: ln(x^2 + y^2)",
            "3D Spatial Wave: exp(-t)*sin(x)*cos(y)",
            "Monkey Saddle: x^3 - 3*x*y^2"
        ]
    )

    preset_map = {
        "Sum of Squares: x^2 + y^2 + z^2": "x^2 + y^2 + z^2",
        "Trig Product: sin(x) * cos(y)": "sin(x)*cos(y)",
        "Exponential Mixture: x^2*y + e^(x*y)": "x^2*y + exp(x*y)",
        "Hyperbolic Saddle: x^2 - y^2": "x^2 - y^2",
        "Gaussian Bell Surface: exp(-(x^2 + y^2))": "exp(-(x^2 + y^2))",
        "Rosenbrock Valley: (1 - x)^2 + 100*(y - x^2)^2": "(1 - x)^2 + 100*(y - x^2)^2",
        "Logarithmic Potential: ln(x^2 + y^2)": "ln(x^2 + y^2)",
        "3D Spatial Wave: exp(-t)*sin(x)*cos(y)": "exp(-t)*sin(x)*cos(y)",
        "Monkey Saddle: x^3 - 3*x*y^2": "x^3 - 3*x*y^2"
    }

    default_expr = "x^2*y + exp(x*y)"
    if preset != "Custom Expression":
        default_expr = preset_map.get(preset, default_expr)

    st.markdown("---")
    st.markdown("### 🛠️ Function Variables")
    active_var = st.selectbox("Differentiate with respect to (w.r.t):", ["x", "y", "z", "t", "r", "theta"], index=0)
    deriv_order = st.slider("Derivative Order ($n$):", min_value=1, max_value=4, value=1, step=1)
    
    st.markdown("---")
    st.markdown("### 🎨 3D Visualization Settings")
    color_scale = st.selectbox(
        "Plot Color Theme:",
        ["Viridis", "Plasma", "Electric", "Purples", "Turbo", "RdBu_r", "Hot", "Cividis"],
        index=0
    )
    grid_resolution = st.slider("3D Grid Resolution:", min_value=30, max_value=100, value=60, step=10)
    show_tangent = st.checkbox("Show Tangent Plane", value=True)
    show_contours = st.checkbox("Show Bottom Contours", value=True)

    st.markdown("---")
    st.markdown("""
    <div style="font-size:0.75rem; color:#9490b8; text-align:center;">
        Engineered with 💜 using <b>Streamlit</b>, <b>SymPy</b>, & <b>Plotly</b>.<br>
        Ready for instant deployment on Streamlit Community Cloud.
    </div>
    """, unsafe_allow_html=True)


# Main Content Area
col_input, col_tools = st.columns([3, 1])

with col_input:
    func_str = st.text_input(
        "Function Expression f(x, y, z, ...):",
        value=default_expr,
        placeholder="e.g., x^3*y^2 - 3*x*y + sin(x*z)",
        help="Use standard notation: ^ for power, * for multiplication, sin, cos, exp, ln, sqrt."
    )

with col_tools:
    st.markdown("<div style='height: 28px;'></div>", unsafe_allow_html=True)
    simplify_result = st.checkbox("Fully Simplify Result", value=True)


# Parse and Compute
if not func_str.strip():
    st.warning("⚠️ Please enter a mathematical expression above.")
    st.stop()

try:
    expr = parse_to_sympy(func_str)
    all_symbols = sorted(list(expr.free_symbols), key=lambda s: s.name)
    var_sym = sp.Symbol(active_var)
except Exception as e:
    st.error(f"❌ Syntax Error in Mathematical Expression: `{str(e)}`")
    st.info("💡 Tip: Ensure correct operators such as `x^2`, `2*x*y`, `sin(x)`, `exp(x*y)`, or `ln(x^2 + y^2)`.")
    st.stop()


# Symbolic Derivative Computation
with st.spinner("Computing symbolic partial derivatives..."):
    # Target derivative
    raw_deriv = expr
    deriv_steps = []
    
    deriv_steps.append((f"Start with function", expr))
    
    current_diff = expr
    for step_i in range(1, deriv_order + 1):
        prev_diff = current_diff
        current_diff = sp.diff(current_diff, var_sym)
        if simplify_result:
            current_simplified = sp.simplify(current_diff)
        else:
            current_simplified = current_diff
        
        ord_symbol = f"\\frac{{\\partial^{{{step_i}}} f}}{{\\partial {active_var}^{{{step_i}}}}}" if step_i > 1 else f"\\frac{{\\partial f}}{{\\partial {active_var}}}"
        deriv_steps.append((f"Order {step_i} derivative w.r.t ${active_var}$", current_simplified))

    final_derivative = deriv_steps[-1][1]
    if simplify_result:
        final_derivative = sp.simplify(final_derivative)


# Tabs for rich modular view
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📐 Symbolic Result & Steps",
    "🌐 3D Surface & Contour Visualizer",
    "⚡ Multivariable & Vector Analysis",
    "🔢 Numeric Point Evaluator",
    "📖 Calculus Reference Manual"
])


# ==========================================
# TAB 1: SYMBOLIC RESULT & STEP-BY-STEP
# ==========================================
with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">✦ Partial Derivative Result</div>', unsafe_allow_html=True)
    
    # Notation header
    order_latex = f"\\frac{{\\partial^{{{deriv_order}}} f}}{{\\partial {active_var}^{{{deriv_order}}}}}" if deriv_order > 1 else f"\\frac{{\\partial f}}{{\\partial {active_var}}}"
    
    res_col1, res_col2 = st.columns([3, 1])
    with res_col1:
        st.markdown(f"### $${order_latex} = {sp.latex(final_derivative)}$$")
        st.caption(f"Evaluated with respect to variable **{active_var}** (order **{deriv_order}**). All other variables are treated as constants.")
    
    with res_col2:
        st.markdown("**Identified Variables:**")
        symbols_html = "".join([f"<span class='stat-pill'>{s.name}</span>" for s in all_symbols]) or "<span class='stat-pill'>constant</span>"
        st.markdown(symbols_html, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

    # Step-by-Step Breakdown
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">✦ Step-by-Step Derivation Breakdown</div>', unsafe_allow_html=True)
    
    st.markdown(f"""
    <div class="step-box">
        <div class="step-num">01</div>
        <div>
            <strong>Identify Target Variable:</strong> Treat <code>{active_var}</code> as the sole independent variable. 
            All other symbols ({', '.join([s.name for s in all_symbols if s.name != active_var]) if len(all_symbols) > 1 else 'none'}) act as invariant constants.
        </div>
    </div>
    """, unsafe_allow_html=True)

    for idx, (label, step_expr) in enumerate(deriv_steps[1:], start=2):
        st.markdown(f"""
        <div class="step-box">
            <div class="step-num">{idx:02d}</div>
            <div>
                <strong>{label}:</strong><br>
                <div style="margin-top: 6px; font-size: 1.05rem;">$${sp.latex(step_expr)}$$</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Code exports
    st.markdown("---")
    st.markdown("#### 💻 Export Mathematical Notation & Code")
    exp_c1, exp_c2, exp_c3 = st.columns(3)
    with exp_c1:
        st.text_input("LaTeX Code:", value=f"{order_latex} = {sp.latex(final_derivative)}", key="latex_copy")
    with exp_c2:
        st.text_input("Python / SymPy Code:", value=f"sp.diff({sp.srepr(expr)}, {active_var}, {deriv_order})", key="python_copy")
    with exp_c3:
        st.text_input("Plain Math String:", value=str(final_derivative), key="plain_copy")
        
    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# TAB 2: INTERACTIVE 3D & CONTOUR VISUALIZER
# ==========================================
with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">✦ 3D Interactive Surface & Contour Dynamics</div>', unsafe_allow_html=True)
    
    # Check if function has at least x and y or single variable
    plot_vars = [s for s in all_symbols if s.name in ['x', 'y']]
    if not plot_vars and len(all_symbols) >= 2:
        plot_vars = all_symbols[:2]
    elif len(all_symbols) == 1:
        plot_vars = [all_symbols[0], sp.Symbol('y')]
    elif len(all_symbols) == 0:
        plot_vars = [sp.Symbol('x'), sp.Symbol('y')]

    var1, var2 = plot_vars[0], plot_vars[1] if len(plot_vars) > 1 else sp.Symbol('y')

    ctrl1, ctrl2, ctrl3, ctrl4 = st.columns(4)
    with ctrl1:
        x_min = st.number_input(f"{var1.name} Min:", value=-3.0, step=0.5)
    with ctrl2:
        x_max = st.number_input(f"{var1.name} Max:", value=3.0, step=0.5)
    with ctrl3:
        y_min = st.number_input(f"{var2.name} Min:", value=-3.0, step=0.5)
    with ctrl4:
        y_max = st.number_input(f"{var2.name} Max:", value=3.0, step=0.5)

    # Point for tangent plane
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        x0 = st.slider(f"Evaluation Point ${var1.name}_0$:", float(x_min), float(x_max), float((x_min + x_max) / 4), step=0.1)
    with p_col2:
        y0 = st.slider(f"Evaluation Point ${var2.name}_0$:", float(y_min), float(y_max), float((y_min + y_max) / 4), step=0.1)

    try:
        # Create numerical evaluation lambda
        # Substitute any other variable with 1.0 for plotting
        other_symbols = {s: 1.0 for s in all_symbols if s not in [var1, var2]}
        subbed_expr = expr.subs(other_symbols)
        f_lambdified = sp.lambdify((var1, var2), subbed_expr, modules=['numpy'])

        X = np.linspace(x_min, x_max, grid_resolution)
        Y = np.linspace(y_min, y_max, grid_resolution)
        X_grid, Y_grid = np.meshgrid(X, Y)
        
        Z_grid = f_lambdified(X_grid, Y_grid)
        # Clean infinities or nans
        if np.isscalar(Z_grid):
            Z_grid = np.full_like(X_grid, float(Z_grid))
        else:
            Z_grid = np.nan_to_num(Z_grid, nan=0.0, posinf=1e4, neginf=-1e4)

        fig = go.Figure()

        # Add Main 3D Surface
        surface_kwargs = {
            "x": X_grid,
            "y": Y_grid,
            "z": Z_grid,
            "colorscale": color_scale,
            "opacity": 0.92,
            "name": f"f({var1.name},{var2.name})",
            "colorbar": dict(title="f(x,y)", thickness=15, len=0.7)
        }
        if show_contours:
            surface_kwargs["contours_z"] = dict(
                show=True, usecolormap=True, highlightcolor="limegreen", project_z=True
            )

        fig.add_trace(go.Surface(**surface_kwargs))

        # Add Tangent Plane at (x0, y0) if requested
        if show_tangent:
            try:
                df_dx = sp.diff(subbed_expr, var1)
                df_dy = sp.diff(subbed_expr, var2)
                z0_val = float(subbed_expr.subs({var1: x0, var2: y0}).evalf())
                fx_val = float(df_dx.subs({var1: x0, var2: y0}).evalf())
                fy_val = float(df_dy.subs({var1: x0, var2: y0}).evalf())

                # Tangent plane: Z_tan = z0 + fx*(X - x0) + fy*(Y - y0)
                Z_tan = z0_val + fx_val * (X_grid - x0) + fy_val * (Y_grid - y0)

                fig.add_trace(go.Surface(
                    x=X_grid,
                    y=Y_grid,
                    z=Z_tan,
                    colorscale=[[0, 'rgba(255, 108, 168, 0.4)'], [1, 'rgba(255, 108, 168, 0.4)']],
                    showscale=False,
                    name=f"Tangent Plane at ({x0:.1f}, {y0:.1f})",
                    opacity=0.55
                ))

                # Point Marker
                fig.add_trace(go.Scatter3d(
                    x=[x0], y=[y0], z=[z0_val],
                    mode='markers',
                    marker=dict(size=8, color='#65ffd0', symbol='diamond'),
                    name=f"Point P({x0:.1f}, {y0:.1f}, {z0_val:.2f})"
                ))
            except Exception as tan_err:
                pass

        # Configure layout for sleek cyberpunk/dark appearance
        fig.update_layout(
            title=f"3D Response Surface: f({var1.name}, {var2.name})",
            template="plotly_dark",
            paper_bgcolor='rgba(7, 7, 13, 0)',
            plot_bgcolor='rgba(7, 7, 13, 0)',
            scene=dict(
                xaxis=dict(title=var1.name, backgroundcolor="#11111a", gridcolor="rgba(138,108,255,0.15)"),
                yaxis=dict(title=var2.name, backgroundcolor="#11111a", gridcolor="rgba(138,108,255,0.15)"),
                zaxis=dict(title="f", backgroundcolor="#11111a", gridcolor="rgba(138,108,255,0.15)"),
                camera=dict(eye=dict(x=1.6, y=1.6, z=1.2))
            ),
            margin=dict(l=0, r=0, b=0, t=40),
            height=620
        )

        st.plotly_chart(fig, use_container_width=True)

        # 2D Contour Plot with Gradient Vector Field
        st.markdown("#### 🧭 2D Contour Slice & Gradient Vector Field")
        
        # Compute gradient vectors on a coarser grid for arrows
        sample_pts = 16
        X_sub = np.linspace(x_min, x_max, sample_pts)
        Y_sub = np.linspace(y_min, y_max, sample_pts)
        X_sub_g, Y_sub_g = np.meshgrid(X_sub, Y_sub)
        
        df_dx_lamb = sp.lambdify((var1, var2), sp.diff(subbed_expr, var1), modules=['numpy'])
        df_dy_lamb = sp.lambdify((var1, var2), sp.diff(subbed_expr, var2), modules=['numpy'])
        
        U = df_dx_lamb(X_sub_g, Y_sub_g)
        V = df_dy_lamb(X_sub_g, Y_sub_g)
        if np.isscalar(U): U = np.full_like(X_sub_g, float(U))
        if np.isscalar(V): V = np.full_like(Y_sub_g, float(V))
        
        # Normalize vectors for clear quiver display
        mag = np.sqrt(U**2 + V**2) + 1e-9
        U_norm = (U / mag) * ((x_max - x_min) / (sample_pts * 2.2))
        V_norm = (V / mag) * ((y_max - y_min) / (sample_pts * 2.2))

        fig2 = go.Figure()
        # Add Contour
        fig2.add_trace(go.Contour(
            x=X, y=Y, z=Z_grid,
            colorscale=color_scale,
            contours=dict(showlabels=True, labelfont=dict(size=10, color="white")),
            colorbar=dict(title="Value")
        ))
        
        # Add Quiver Arrows
        for i in range(sample_pts):
            for j in range(sample_pts):
                fig2.add_annotation(
                    x=X_sub_g[i, j] + U_norm[i, j],
                    y=Y_sub_g[i, j] + V_norm[i, j],
                    ax=X_sub_g[i, j],
                    ay=Y_sub_g[i, j],
                    xref="x", yref="y", axref="x", ayref="y",
                    showarrow=True,
                    arrowhead=2,
                    arrowsize=1,
                    arrowwidth=1.5,
                    arrowcolor="#65ffd0",
                    opacity=0.75
                )

        fig2.update_layout(
            title=f"Gradient Flow Field ∇f({var1.name}, {var2.name}) over Level Curves",
            template="plotly_dark",
            paper_bgcolor='rgba(7, 7, 13, 0)',
            plot_bgcolor='rgba(17, 17, 26, 0.8)',
            xaxis=dict(title=var1.name),
            yaxis=dict(title=var2.name),
            height=450,
            margin=dict(l=20, r=20, b=20, t=40)
        )
        st.plotly_chart(fig2, use_container_width=True)

    except Exception as plot_err:
        st.info(f"💡 3D plot is optimized for functions of 2 variables. (Detail: {str(plot_err)})")

    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# TAB 3: MULTIVARIABLE & VECTOR ANALYSIS
# ==========================================
with tab3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">✦ Comprehensive Vector Calculus & Matrix Operators</div>', unsafe_allow_html=True)
    
    calc_vars = [s for s in all_symbols if s.name in ['x', 'y', 'z']]
    if not calc_vars:
        calc_vars = all_symbols if all_symbols else [sp.Symbol('x'), sp.Symbol('y')]
    
    # 1. Gradient Vector
    st.markdown("#### 1. Gradient Vector $\\nabla f$")
    grad_vector = [sp.diff(expr, v) for v in calc_vars]
    grad_latex = "\\nabla f = \\begin{bmatrix}" + " \\\\ ".join([f"\\frac{{\\partial f}}{{\\partial {v.name}}} = {sp.latex(sp.simplify(g))}" for v, g in zip(calc_vars, grad_vector)]) + "\\end{bmatrix}"
    st.markdown(f"$${grad_latex}$$")
    
    # 2. Laplacian
    st.markdown("#### 2. Laplacian Operator $\\nabla^2 f = \\Delta f$")
    laplacian_expr = sum([sp.diff(expr, v, 2) for v in calc_vars])
    laplacian_simplified = sp.simplify(laplacian_expr)
    is_harmonic = laplacian_simplified == 0
    
    st.markdown(f"$$\\nabla^2 f = \\sum_{{i}} \\frac{{\\partial^2 f}}{{\\partial x_i^2}} = {sp.latex(laplacian_simplified)}$$")
    if is_harmonic:
        st.success("✨ **Harmonic Function Alert:** $\\nabla^2 f = 0$ everywhere! This function satisfies Laplace's Equation.")
    else:
        st.info(f"Function is non-harmonic (Laplacian is nonzero).")

    # 3. Hessian Matrix & Critical Point Test (for 2 variables)
    if len(calc_vars) >= 2:
        v1, v2 = calc_vars[0], calc_vars[1]
        st.markdown(f"#### 3. Hessian Matrix $H$ w.r.t $({v1.name}, {v2.name})$")
        f_xx = sp.simplify(sp.diff(expr, v1, 2))
        f_yy = sp.simplify(sp.diff(expr, v2, 2))
        f_xy = sp.simplify(sp.diff(expr, v1, v2))
        f_yx = sp.simplify(sp.diff(expr, v2, v1))
        
        # Clairaut's theorem check
        clairaut_match = (f_xy == f_yx)
        
        hessian_mat = sp.Matrix([[f_xx, f_xy], [f_yx, f_yy]])
        det_H = sp.simplify(hessian_mat.det())
        
        h_col1, h_col2 = st.columns([2, 1])
        with h_col1:
            st.markdown(f"$$H = \\begin{{bmatrix}} \\frac{{\\partial^2 f}}{{\\partial {v1.name}^2}} & \\frac{{\\partial^2 f}}{{\\partial {v1.name} \\partial {v2.name}}} \\\\ \\frac{{\\partial^2 f}}{{\\partial {v2.name} \\partial {v1.name}}} & \\frac{{\\partial^2 f}}{{\\partial {v2.name}^2}} \\end{{bmatrix}} = \\begin{{bmatrix}} {sp.latex(f_xx)} & {sp.latex(f_xy)} \\\\ {sp.latex(f_yx)} & {sp.latex(f_yy)} \\end{{bmatrix}}$$")
            st.markdown(f"**Hessian Determinant $|H| = f_{{{v1.name}{v1.name}}} f_{{{v2.name}{v2.name}}} - (f_{{{v1.name}{v2.name}}})^2$:**")
            st.markdown(f"$$|H| = {sp.latex(det_H)}$$")
        
        with h_col2:
            st.markdown("**Clairaut's / Schwarz's Theorem:**")
            if clairaut_match:
                st.success(f"Verified: $\\frac{{\\partial^2 f}}{{\\partial {v1.name} \\partial {v2.name}}} = \\frac{{\\partial^2 f}}{{\\partial {v2.name} \\partial {v1.name}}}$")
            else:
                st.warning("Mixed partials differ due to discontinuity in 2nd derivatives.")
            
            st.markdown("""
            **Second Derivative Test Rules:**
            - If $|H| > 0$ and $f_{xx} > 0$: **Local Minimum**
            - If $|H| > 0$ and $f_{xx} < 0$: **Local Maximum**
            - If $|H| < 0$: **Saddle Point**
            - If $|H| = 0$: **Inconclusive**
            """)

    # 4. Tangent Plane & Linearization Equation
    st.markdown("#### 4. Tangent Plane & Linear Approximation Formula")
    if len(calc_vars) >= 2:
        v1, v2 = calc_vars[0], calc_vars[1]
        st.markdown(f"At any point $({v1.name}_0, {v2.name}_0)$:")
        st.markdown(f"$$L({v1.name}, {v2.name}) = f({v1.name}_0, {v2.name}_0) + \\frac{{\\partial f}}{{\\partial {v1.name}}}({v1.name}_0, {v2.name}_0) \\cdot ({v1.name} - {v1.name}_0) + \\frac{{\\partial f}}{{\\partial {v2.name}}}({v1.name}_0, {v2.name}_0) \\cdot ({v2.name} - {v2.name}_0)$$")

    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# TAB 4: NUMERIC POINT EVALUATOR
# ==========================================
with tab4:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">✦ Point Evaluation & Directional Derivative</div>', unsafe_allow_html=True)
    
    st.markdown("Enter numerical coordinates to evaluate $f$ and its partial derivatives at a specific point:")
    
    eval_cols = st.columns(len(all_symbols) if all_symbols else 1)
    eval_vals = {}
    
    for i, s in enumerate(all_symbols):
        with eval_cols[i]:
            eval_vals[s] = st.number_input(f"Value for ${s.name}$:", value=1.0, step=0.5, key=f"eval_val_{s.name}")

    try:
        f_at_pt = expr.subs(eval_vals).evalf()
        deriv_at_pt = final_derivative.subs(eval_vals).evalf()
        
        e_col1, e_col2, e_col3 = st.columns(3)
        with e_col1:
            st.metric(label="f(Point)", value=f"{float(f_at_pt):.4f}")
        with e_col2:
            st.metric(label=f"∂^{deriv_order}f / ∂{active_var}^{deriv_order} at Point", value=f"{float(deriv_at_pt):.4f}")
        with e_col3:
            # Gradient Magnitude at Point
            grad_vals = [float(g.subs(eval_vals).evalf()) for g in grad_vector]
            grad_mag = np.linalg.norm(grad_vals)
            st.metric(label="||∇f|| (Steepest Slope)", value=f"{grad_mag:.4f}")

        # Directional Derivative Calculator
        st.markdown("---")
        st.markdown("#### 🎯 Directional Derivative $D_{\\mathbf{u}} f = \\nabla f \\cdot \\mathbf{u}$")
        st.markdown("Specify a directional vector $\\mathbf{v}$ (it will be automatically normalized to unit vector $\\mathbf{u} = \\mathbf{v}/\\|\\mathbf{v}\\|$):")
        
        dir_cols = st.columns(len(calc_vars))
        dir_v = []
        for i, v in enumerate(calc_vars):
            with dir_cols[i]:
                dir_v.append(st.number_input(f"Vector component $v_{{{v.name}}}$:", value=1.0 if i == 0 else 0.0, step=0.5, key=f"dir_comp_{v.name}"))
        
        dir_v = np.array(dir_v, dtype=float)
        v_norm = np.linalg.norm(dir_v)
        if v_norm > 0:
            u_unit = dir_v / v_norm
            d_u_f = np.dot(grad_vals[:len(u_unit)], u_unit)
            st.markdown(f"""
            - **Unit Direction Vector $\\mathbf{{u}}$:** `[{', '.join([f'{comp:.3f}' for comp in u_unit])}]`
            - **Directional Derivative $D_{{\\mathbf{{u}}}} f$:** ` {d_u_f:.4f} `
            """)
        else:
            st.warning("Direction vector cannot be the zero vector.")

    except Exception as num_err:
        st.error(f"Error evaluating at point: {str(num_err)}")

    st.markdown('</div>', unsafe_allow_html=True)


# ==========================================
# TAB 5: CALCULUS THEORY & REFERENCE
# ==========================================
with tab5:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown('<div class="card-title">✦ Multivariable Calculus Reference Manual & Differentiation Rules</div>', unsafe_allow_html=True)
    
    r1, r2 = st.columns(2)
    with r1:
        st.markdown("""
        #### 📜 Fundamental Differentiation Rules
        
        **1. Power Rule:**
        $$\\frac{\\partial}{\\partial x}[x^n] = n x^{n-1}$$
        
        **2. Product Rule:**
        $$\\frac{\\partial}{\\partial x}[u \\cdot v] = u \\frac{\\partial v}{\\partial x} + v \\frac{\\partial u}{\\partial x}$$
        
        **3. Quotient Rule:**
        $$\\frac{\\partial}{\\partial x}\\left[\\frac{u}{v}\\right] = \\frac{v \\frac{\\partial u}{\\partial x} - u \\frac{\\partial v}{\\partial x}}{v^2}$$
        
        **4. Multivariable Chain Rule:**
        $$\\frac{df}{dt} = \\frac{\\partial f}{\\partial x}\\frac{dx}{dt} + \\frac{\\partial f}{\\partial y}\\frac{dy}{dt} + \\frac{\\partial f}{\\partial z}\\frac{dz}{dt}$$
        """)
        
    with r2:
        st.markdown("""
        #### 🌌 Physics & Engineering Applications
        
        **1. Wave Equation:**
        $$\\frac{\\partial^2 u}{\\partial t^2} = c^2 \\nabla^2 u$$
        
        **2. Heat Diffusion Equation:**
        $$\\frac{\\partial u}{\\partial t} = \\alpha \\nabla^2 u$$
        
        **3. Navier-Stokes Incompressible Continuity:**
        $$\\nabla \\cdot \\mathbf{u} = \\frac{\\partial u}{\\partial x} + \\frac{\\partial v}{\\partial y} + \\frac{\\partial w}{\\partial z} = 0$$
        
        **4. Gradient Descent Optimization:**
        $$\\mathbf{w}_{k+1} = \\mathbf{w}_k - \\eta \\nabla f(\\mathbf{w}_k)$$
        """)

    st.markdown('</div>', unsafe_allow_html=True)
