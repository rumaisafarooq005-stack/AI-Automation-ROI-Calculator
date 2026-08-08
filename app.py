import streamlit as st

# ============================================================
# SafeX Solutions | AI & ML Department
# AI Automation ROI Calculator — Client-Ready Version
# ============================================================

st.set_page_config(
    page_title="SafeX | AI Automation ROI Calculator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Styling
# -----------------------------
st.markdown("""
<style>
    .block-container {max-width: 1180px; padding-top: 2rem; padding-bottom: 2rem;}
    .hero {
        padding: 1.8rem 2rem;
        border-radius: 18px;
        background: linear-gradient(135deg, #111827 0%, #1f2937 55%, #111827 100%);
        border: 1px solid rgba(255,255,255,.10);
        margin-bottom: 1.4rem;
    }
    .hero h1 {font-size: 2.35rem; margin: 0 0 .35rem 0;}
    .hero p {font-size: 1.05rem; color: #cbd5e1; margin: 0;}
    .eyebrow {font-size: .82rem; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: #93c5fd; margin-bottom: .5rem;}
    .section {font-size: 1.35rem; font-weight: 700; margin: 1.2rem 0 .7rem 0;}
    .info-card {
        padding: 1rem 1.1rem;
        border-radius: 12px;
        background: rgba(127,127,127,.08);
        border: 1px solid rgba(127,127,127,.18);
        margin: .4rem 0 1rem 0;
    }
    .small {color: #94a3b8; font-size: .88rem;}
    .result-card {
        padding: 1rem;
        border-radius: 14px;
        border: 1px solid rgba(127,127,127,.18);
        background: rgba(127,127,127,.06);
        min-height: 115px;
    }
    .result-label {font-size: .82rem; color: #94a3b8; margin-bottom: .35rem;}
    .result-value {font-size: 1.65rem; font-weight: 750;}
    .positive {font-weight: 700;}
    .footer {text-align:center; color:#94a3b8; font-size:.82rem; padding:1.2rem 0 .2rem 0;}
    div[data-testid="stMetric"] {border-radius: 12px;}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# Scenario presets
# -----------------------------
SCENARIOS = {
    "Custom Business": {
        "tasks": 1000, "minutes": 5.0, "hourly": 10.0, "automation": 70, "setup": 500.0,
        "description": "Enter your own business assumptions and estimate the potential value of automation."
    },
    "E-commerce Customer Support": {
        "tasks": 1000, "minutes": 5.0, "hourly": 10.0, "automation": 70, "setup": 500.0,
        "description": "Automate repetitive questions about orders, products, returns, shipping, and FAQs."
    },
    "Email Management": {
        "tasks": 600, "minutes": 8.0, "hourly": 15.0, "automation": 60, "setup": 750.0,
        "description": "Use AI to draft routine replies, follow-ups, confirmations, and repetitive business emails."
    },
    "Customer Service / FAQ": {
        "tasks": 1500, "minutes": 4.0, "hourly": 12.0, "automation": 75, "setup": 600.0,
        "description": "Automate common customer questions using an AI assistant or FAQ chatbot."
    },
}

# -----------------------------
# Session state
# -----------------------------
if "scenario" not in st.session_state:
    st.session_state.scenario = "E-commerce Customer Support"
preset = SCENARIOS[st.session_state.scenario]

for key, value in {
    "tasks": preset["tasks"],
    "minutes": preset["minutes"],
    "hourly": preset["hourly"],
    "automation": preset["automation"],
    "setup": preset["setup"],
}.items():
    if key not in st.session_state:
        st.session_state[key] = value

def apply_scenario():
    p = SCENARIOS[st.session_state.scenario]
    st.session_state.tasks = p["tasks"]
    st.session_state.minutes = p["minutes"]
    st.session_state.hourly = p["hourly"]
    st.session_state.automation = p["automation"]
    st.session_state.setup = p["setup"]

# -----------------------------
# Header
# -----------------------------
st.markdown("""
<div class="hero">
    <div class="eyebrow">SafeX Solutions • AI & ML Department</div>
    <h1>🤖 AI Automation ROI Calculator</h1>
    <p>Quantify the potential time savings, cost savings, and business value of automating repetitive work.</p>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# Scenario
# -----------------------------
st.markdown('<div class="section">1. Choose a business scenario</div>', unsafe_allow_html=True)

scenario = st.selectbox(
    "Business scenario",
    list(SCENARIOS.keys()),
    key="scenario",
    on_change=apply_scenario,
    label_visibility="collapsed",
)

st.markdown(
    f'<div class="info-card"><strong>What can be automated?</strong><br>'
    f'{SCENARIOS[scenario]["description"]}<br><span class="small">'
    f'Preset values are illustrative and can be adjusted below.</span></div>',
    unsafe_allow_html=True
)

# -----------------------------
# Inputs
# -----------------------------
st.markdown('<div class="section">2. Business assumptions</div>', unsafe_allow_html=True)

left, right = st.columns(2)

with left:
    st.number_input(
        "Monthly repetitive tasks / queries",
        min_value=1,
        step=100,
        key="tasks",
        help="Approximate number of repetitive tasks handled each month."
    )
    st.number_input(
        "Average staff time per task (minutes)",
        min_value=0.5,
        step=0.5,
        key="minutes",
        help="Average staff time required to complete one task."
    )
    st.number_input(
        "Staff hourly cost (USD)",
        min_value=1.0,
        step=1.0,
        key="hourly",
        help="Approximate fully loaded hourly cost of the staff member doing the work."
    )

with right:
    st.slider(
        "Expected automation rate",
        min_value=10,
        max_value=100,
        step=5,
        key="automation",
        format="%d%%",
        help="Estimated percentage of repetitive work that the automation can handle."
    )
    st.number_input(
        "Estimated one-time setup cost (USD)",
        min_value=0.0,
        step=50.0,
        key="setup",
        help="Illustrative implementation/setup cost."
    )

# -----------------------------
# Calculations
# -----------------------------
tasks = float(st.session_state.tasks)
minutes = float(st.session_state.minutes)
hourly = float(st.session_state.hourly)
automation_rate = float(st.session_state.automation) / 100
setup = float(st.session_state.setup)

current_hours = tasks * minutes / 60
hours_saved = current_hours * automation_rate
remaining_hours = current_hours - hours_saved
current_monthly_cost = current_hours * hourly
monthly_savings = hours_saved * hourly
annual_savings = monthly_savings * 12
first_year_net = annual_savings - setup
payback_months = setup / monthly_savings if monthly_savings > 0 else 0
roi = ((annual_savings - setup) / setup * 100) if setup > 0 else 0
workload_reduction = (hours_saved / current_hours * 100) if current_hours > 0 else 0

# -----------------------------
# Impact metrics
# -----------------------------
st.divider()
st.markdown('<div class="section">3. Estimated business impact</div>', unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
m1.metric("Hours saved / month", f"{hours_saved:,.1f}")
m2.metric("Monthly cost saved", f"${monthly_savings:,.2f}")
m3.metric("Annual savings", f"${annual_savings:,.2f}")
m4.metric("Payback period", f"{payback_months:.1f} mo")

# -----------------------------
# Before / after
# -----------------------------
st.markdown('<div class="section">4. Before vs. after automation</div>', unsafe_allow_html=True)
b1, b2 = st.columns(2)

with b1:
    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">BEFORE AUTOMATION</div>
        <div class="result-value">{current_hours:,.1f} hrs/month</div>
        <div class="small">Estimated manual staff workload</div>
        <br>
        <div><strong>${current_monthly_cost:,.2f}</strong> estimated monthly labor cost</div>
    </div>
    """, unsafe_allow_html=True)

with b2:
    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">AFTER AUTOMATION</div>
        <div class="result-value">{remaining_hours:,.1f} hrs/month</div>
        <div class="small">Estimated remaining human workload</div>
        <br>
        <div><strong>{hours_saved:,.1f} hrs</strong> potentially freed each month</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# Charts
# -----------------------------
st.markdown('<div class="section">5. Workload and financial comparison</div>', unsafe_allow_html=True)

chart_left, chart_right = st.columns(2)

with chart_left:
    st.caption("Monthly workload (hours)")
    st.bar_chart({
        "Manual workload": [current_hours],
        "Remaining after automation": [remaining_hours],
        "Potential hours saved": [hours_saved],
    }, height=280)

with chart_right:
    st.caption("Estimated savings")
    st.bar_chart({
        "Monthly savings": [monthly_savings],
        "Annual savings": [annual_savings],
    }, height=280)

# -----------------------------
# Financial value
# -----------------------------
st.markdown('<div class="section">6. Financial value</div>', unsafe_allow_html=True)
f1, f2, f3 = st.columns(3)
f1.metric("Annual gross savings", f"${annual_savings:,.2f}")
f2.metric("Setup cost", f"${setup:,.2f}")
f3.metric("First-year net benefit", f"${first_year_net:,.2f}")

# -----------------------------
# ROI and assessment
# -----------------------------
st.markdown('<div class="section">7. ROI assessment</div>', unsafe_allow_html=True)
r1, r2 = st.columns(2)
r1.metric("Estimated annual ROI", f"{roi:,.1f}%")
r2.metric("Workload reduction", f"{workload_reduction:,.1f}%")

if first_year_net > 0:
    st.success(
        f"🟢 **Positive business case:** Under these assumptions, the automation "
        f"could generate approximately **${annual_savings:,.2f}** in gross annual "
        f"savings and **${first_year_net:,.2f}** in first-year net benefit."
    )
else:
    st.warning(
        "🟠 **Review the business case:** The estimated first-year savings do not "
        "currently cover the setup cost. Consider validating the assumptions or "
        "targeting a higher-value workflow."
    )

# -----------------------------
# Recommendation
# -----------------------------
st.markdown('<div class="section">8. Automation recommendation</div>', unsafe_allow_html=True)

if automation_rate >= 0.70:
    level = "High"
    recommendation = (
        "This workflow appears well suited to automation. A chatbot, AI assistant, "
        "or workflow automation could handle a large share of repetitive work, "
        "with human review retained for exceptions."
    )
elif automation_rate >= 0.40:
    level = "Moderate"
    recommendation = (
        "A hybrid human + AI workflow is likely the safest starting point. "
        "Automate repetitive steps while keeping human oversight for complex cases."
    )
else:
    level = "Low"
    recommendation = (
        "Start with a smaller automation scope. Identify the most repetitive "
        "subtasks first and validate accuracy before expanding."
    )

st.info(f"**{level} automation potential** — {recommendation}")

# -----------------------------
# Client-ready summary
# -----------------------------
st.markdown('<div class="section">9. Client-ready summary</div>', unsafe_allow_html=True)

summary = f"""
AI AUTOMATION ROI ASSESSMENT

Scenario: {scenario}

Current monthly workload: {current_hours:,.1f} staff hours
Potential monthly hours saved: {hours_saved:,.1f}
Potential monthly cost savings: ${monthly_savings:,.2f}
Potential annual savings: ${annual_savings:,.2f}
Estimated setup cost: ${setup:,.2f}
Estimated first-year net benefit: ${first_year_net:,.2f}
Estimated annual ROI: {roi:,.1f}%
Estimated payback period: {payback_months:.1f} months

Recommendation:
{recommendation}

Note: These figures are estimates based on user-provided assumptions and should
be validated against actual workflows, costs, volumes, and automation performance.
"""

with st.expander("View the client summary"):
    st.text(summary)

st.download_button(
    "📄 Download assessment summary",
    data=summary,
    file_name="AI_Automation_ROI_Assessment.txt",
    mime="text/plain",
)

# -----------------------------
# Footer
# -----------------------------
st.divider()
st.markdown(
    """
    <div class="footer">
        <strong>SafeX Solutions</strong> • AI Automation ROI Assessment<br>
        Estimates are illustrative and should be validated against actual business data.
    </div>
    """,
    unsafe_allow_html=True
)
