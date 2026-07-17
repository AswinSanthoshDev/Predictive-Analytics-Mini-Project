import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.markdown("""
<style>
#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Customer Lifetime Value Intelligence",
    page_icon="💎",
    layout="wide"
)

# -------------------------------------------------------
# Load Saved Files
# -------------------------------------------------------

model = joblib.load("models/xgboost_model.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")

# -------------------------------------------------------
# Fonts, Icons & Premium Theme
# -------------------------------------------------------

st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

<style>

:root{
    --bg-deep:#080D18;
    --bg-panel: rgba(255,255,255,0.035);
    --bg-panel-solid:#111a2e;
    --border-soft: rgba(201,162,39,0.18);
    --gold:#D4AF37;
    --gold-bright:#F2D879;
    --gold-dim:#8A7326;
    --text-primary:#EDEFF5;
    --text-secondary:#8B93A7;
    --emerald:#22C55E;
    --amber:#F5A524;
    --rose:#F0475C;
    --radius:16px;
}

/* ---------- Global canvas ---------- */
.stApp{
    background:
        radial-gradient(circle at 12% -10%, rgba(212,175,55,0.10), transparent 40%),
        radial-gradient(circle at 90% 0%, rgba(59,130,246,0.08), transparent 45%),
        linear-gradient(180deg, #080D18 0%, #0B1220 40%, #0A0F1C 100%);
    color: var(--text-primary);
    font-family:'Inter', sans-serif;
}

html, body, [class*="css"]{
    font-family:'Inter', sans-serif;
}

@keyframes fadeInUp{
    from{ opacity:0; transform: translateY(16px); }
    to{ opacity:1; transform: translateY(0); }
}
@keyframes shimmer{
    0%{ background-position: -400px 0; }
    100%{ background-position: 400px 0; }
}
@keyframes floatY{
    0%, 100%{ transform: translateY(0px); }
    50%{ transform: translateY(-6px); }
}
@keyframes glowPulse{
    0%, 100%{ box-shadow: 0 0 18px rgba(212,175,55,0.25); }
    50%{ box-shadow: 0 0 34px rgba(212,175,55,0.5); }
}
@keyframes gradientMove{
    0%{ background-position: 0% 50%; }
    50%{ background-position: 100% 50%; }
    100%{ background-position: 0% 50%; }
}

.block-container{
    padding-top: 1.6rem;
    animation: fadeInUp 0.6s ease-out;
}

/* ---------- Hero ---------- */
.hero-card{
    position:relative;
    overflow:hidden;
    border-radius:22px;
    padding:46px 52px;
    margin: 8px 0 4px 0;
    background:
        radial-gradient(circle at 10% 12%, rgba(64, 64, 64, 0.18), transparent 50%),
        radial-gradient(circle at 25% 10%, rgba(59,130,246,0.18), transparent 50%),
        radial-gradient(circle at 92% 88%, rgba(59,130,246,0.18), transparent 55%),
        linear-gradient(145deg, #10131F 0%, #15130E 45%, #0A0D16 100%);
    border:1px solid rgba(212,175,55,0.15);
    box-shadow: 0 30px 60px -25px rgba(4,8,20,0.65);
    animation: fadeInUp 0.7s ease-out;
}
.hero-icon{
    position:absolute;
    right:70px;
    top:20%;
    transform: translateY(-50%);
    font-size:260px;
    color:#F5F5F5;
    opacity:0.065;
    pointer-events:none;
    animation: floatY 6s ease-in-out infinite;
}
.hero-content{
    position:relative;
    z-index:1;
    max-width:640px;
}
.hero-eyebrow{
    display:flex;
    align-items:center;
    gap:10px;
    color: var(--gold);
    font-size:12.5px;
    font-weight:700;
    letter-spacing:0.14em;
    text-transform:uppercase;
    margin-bottom:18px;
}
.hero-eyebrow .dash{
    width:22px;
    height:2px;
    background: var(--gold);
    display:inline-block;
    border-radius:2px;
}
.main-title{
    font-family:'Playfair Display', serif;
    font-weight:800;
    font-size:44px;
    line-height:1.15;
    letter-spacing:0.005em;
    margin:0;
    color: var(--text-primary);
}
.main-title .accent{
    background: linear-gradient(100deg, #F2D879 0%, #D4AF37 40%, #F2D879 100%);
    background-size: 300% auto;
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
    background-clip:text;
    animation: gradientMove 8s ease infinite;
}
.sub-title{
    font-size:15.5px;
    color: var(--text-secondary);
    font-weight:500;
    line-height:1.65;
    margin-top:16px;
    max-width:520px;
}
.hero-pills{
    display:flex;
    flex-wrap:wrap;
    gap:10px;
    margin-top:26px;
}
.hero-pill{
    display:inline-flex;
    align-items:center;
    gap:6px;
    padding:7px 16px;
    border-radius:999px;
    font-size:12.5px;
    font-weight:700;
    border:1px solid;
    background: rgba(255,255,255,0.02);
    letter-spacing:0.01em;
}
.hero-pill.gold{ color: var(--gold-bright); border-color: rgba(212,175,55,0.4); }
.hero-pill.green{ color: var(--emerald); border-color: rgba(34,197,94,0.35); }
.hero-pill.neutral{ color: var(--text-primary); border-color: rgba(255,255,255,0.14); }

@media (max-width: 900px){
    .hero-icon{ font-size:170px; opacity:0.06; right:6px; }
    .hero-card{ padding:36px 28px; }
    .main-title{ font-size:32px; }
}

/* ---------- Section headers ---------- */
.section-header{
    display:flex;
    align-items:center;
    gap:12px;
    font-family:'Playfair Display', serif;
    font-size:23px;
    font-weight:700;
    color: var(--text-primary);
    margin: 6px 0 2px 0;
}
.section-header .icon-chip{
    display:inline-flex;
    align-items:center;
    justify-content:center;
    width:38px;
    height:38px;
    border-radius:11px;
    background: linear-gradient(135deg, rgba(212,175,55,0.22), rgba(212,175,55,0.04));
    border:1px solid var(--border-soft);
    color: var(--gold-bright);
    font-size:16px;
}
.section-caption{
    color: var(--text-secondary);
    font-size:13.5px;
    margin: 2px 0 14px 50px;
}
.gold-divider{
    height:1px;
    border:none;
    margin: 26px 0 22px 0;
    background: linear-gradient(90deg, transparent, var(--border-soft) 20%, var(--border-soft) 80%, transparent);
}

/* ---------- Inputs ---------- */
div[data-testid="stNumberInput"] input,
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div{
    background-color: var(--bg-panel-solid) !important;
    border:1px solid rgba(255,255,255,0.08) !important;
    color: var(--text-primary) !important;
    border-radius:10px !important;
    transition: all 0.25s ease;
}
div[data-testid="stNumberInput"] input:focus,
div[data-baseweb="select"] > div:focus-within{
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 3px rgba(212,175,55,0.15) !important;
}
label, .stSelectbox label, .stNumberInput label, .stSlider label{
    color: var(--text-secondary) !important;
    font-weight:600 !important;
    font-size:13.5px !important;
    letter-spacing:0.01em;
}

/* Slider */
div[data-testid="stSlider"] [role="slider"]{
    background-color: var(--gold) !important;
    box-shadow: 0 0 0 6px rgba(212,175,55,0.15) !important;
}
div[data-testid="stSlider"] .st-emotion-cache-1dj0hjr,
div[data-testid="stTickBar"]{
    color: var(--text-secondary) !important;
}
div[data-testid="stSlider"] div[data-baseweb="slider"] > div > div{
    background: linear-gradient(90deg, var(--gold-dim), var(--gold)) !important;
}

/* ---------- Buttons ---------- */
.stButton > button{
    position:relative;
    overflow:hidden;
    width:100%;
    background: linear-gradient(135deg, #D4AF37 0%, #F2D879 45%, #D4AF37 100%);
    background-size: 220% auto;
    color:#0B0E14 !important;
    font-weight:700 !important;
    font-size:16.5px !important;
    letter-spacing:0.02em;
    padding:0.85em 1.2em;
    border:none !important;
    border-radius:12px !important;
    box-shadow: 0 8px 24px rgba(212,175,55,0.28);
    transition: all 0.35s cubic-bezier(.2,.8,.2,1);
}
.stButton > button:hover{
    background-position: right center;
    transform: translateY(-2px) scale(1.01);
    box-shadow: 0 14px 34px rgba(212,175,55,0.42);
}
.stButton > button:active{
    transform: translateY(0px) scale(0.99);
}
.stButton > button p{
    color:#0B0E14 !important;
    font-weight:700 !important;
}

/* ---------- Glass panels / result cards ---------- */
.glass-card{
    background: var(--bg-panel);
    border:1px solid var(--border-soft);
    border-radius: var(--radius);
    padding:26px 28px;
    backdrop-filter: blur(6px);
    animation: fadeInUp 0.6s ease-out;
}
.result-box{
    background: linear-gradient(155deg, rgba(212,175,55,0.10), rgba(212,175,55,0.02));
    border:1px solid var(--border-soft);
    border-radius: var(--radius);
    padding:30px 32px;
    animation: fadeInUp 0.55s ease-out, glowPulse 3.5s ease-in-out infinite;
}
.result-label{
    color: var(--text-secondary);
    font-size:14px;
    font-weight:600;
    letter-spacing:0.04em;
    text-transform:uppercase;
    margin-bottom:6px;
}
.result-value{
    font-family:'JetBrains Mono', monospace;
    font-size:52px;
    font-weight:700;
    color: var(--gold-bright);
    letter-spacing:-0.01em;
    text-shadow: 0 0 24px rgba(212,175,55,0.25);
}
.segment-card{
    text-align:center;
    padding:26px 18px;
    border-radius: var(--radius);
    background: var(--bg-panel);
    border:1px solid var(--border-soft);
    animation: fadeInUp 0.6s ease-out;
}
.segment-icon{
    font-size:30px;
    margin-bottom:10px;
}
.segment-title{
    font-family:'Playfair Display', serif;
    font-size:20px;
    font-weight:700;
    margin-top:4px;
}
.gauge-track{
    position:relative;
    height:10px;
    border-radius:999px;
    background: linear-gradient(90deg, var(--rose) 0%, var(--amber) 50%, var(--emerald) 100%);
    margin: 18px 4px 6px 4px;
    overflow:visible;
}
.gauge-marker{
    position:absolute;
    top:-7px;
    width:24px;
    height:24px;
    border-radius:50%;
    background: var(--bg-deep);
    border:3px solid #fff;
    box-shadow: 0 0 12px rgba(255,255,255,0.5);
    transform: translateX(-50%);
    transition: left 0.8s cubic-bezier(.2,.8,.2,1);
}
.gauge-labels{
    display:flex;
    justify-content:space-between;
    font-size:11.5px;
    color: var(--text-secondary);
    margin: 4px 4px 0 4px;
    font-weight:600;
    letter-spacing:0.03em;
}

/* metric mini-cards */
.metric-grid{
    display:grid;
    grid-template-columns: repeat(auto-fit, minmax(190px, 1fr));
    gap:14px;
    margin-top:6px;
}
.metric-card{
    background: var(--bg-panel);
    border:1px solid rgba(255,255,255,0.07);
    border-radius:14px;
    padding:16px 18px;
    transition: all 0.25s ease;
    animation: fadeInUp 0.6s ease-out;
}
.metric-card:hover{
    border-color: var(--border-soft);
    transform: translateY(-3px);
}
.metric-card .m-icon{
    color: var(--gold-bright);
    font-size:15px;
    margin-bottom:8px;
}
.metric-card .m-label{
    color: var(--text-secondary);
    font-size:12px;
    font-weight:600;
    text-transform:uppercase;
    letter-spacing:0.04em;
}
.metric-card .m-value{
    font-family:'JetBrains Mono', monospace;
    color: var(--text-primary);
    font-size:19px;
    font-weight:600;
    margin-top:4px;
}

/* recommendation card */
.reco-card{
    border-radius: var(--radius);
    padding:22px 26px;
    border:1px solid var(--border-soft);
    animation: fadeInUp 0.6s ease-out;
}
.reco-card ul{
    margin:10px 0 0 0;
    padding-left:20px;
}
.reco-card li{
    margin-bottom:6px;
    color: var(--text-primary);
    font-size:14.5px;
}

/* ---------- Top info toggle (replaces sidebar) ---------- */
div[data-testid="stExpander"]{
    border:1px solid var(--border-soft) !important;
    border-radius:12px !important;
    background: var(--bg-panel) !important;
    max-width:520px;
    margin: 6px auto 4px auto;
    overflow:hidden;
}
div[data-testid="stExpander"] summary{
    padding:8px 14px !important;
}
div[data-testid="stExpander"] summary p{
    color: var(--gold-bright) !important;
    font-size:13px !important;
    font-weight:700 !important;
    letter-spacing:0.02em;
}
div[data-testid="stExpander"] summary:hover{
    background: rgba(212,175,55,0.05) !important;
}
div[data-testid="stExpander"] svg{
    fill: var(--gold-bright) !important;
}
div[data-testid="stExpanderDetails"]{
    padding: 4px 16px 14px 16px !important;
}
.tech-pill{
    display:inline-flex;
    align-items:center;
    gap:6px;
    background: rgba(212,175,55,0.08);
    border:1px solid var(--border-soft);
    color: var(--gold-bright);
    padding:4px 10px;
    border-radius:999px;
    font-size:11.5px;
    font-weight:600;
    margin:3px 4px 3px 0;
}
.info-row{
    display:flex;
    align-items:center;
    justify-content:space-between;
    gap:10px;
    padding: 6px 2px;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    font-size:13px;
}
.info-row:last-child{ border-bottom:none; }
.info-row .i-label{
    color: var(--text-secondary);
    display:flex;
    align-items:center;
    gap:8px;
    font-weight:500;
}
.info-row .i-value{
    color: var(--text-primary);
    font-weight:700;
    font-family:'JetBrains Mono', monospace;
    font-size:12.5px;
}

/* dataframe polish */
[data-testid="stDataFrame"]{
    border-radius:12px;
    overflow:hidden;
    border:1px solid rgba(255,255,255,0.07);
}

/* footer */
.footer{
    text-align:center;
    color: var(--text-secondary);
    margin-top:30px;
    font-size:13px;
    letter-spacing:0.03em;
}
.footer i{
    color: var(--gold-bright);
}

::-webkit-scrollbar{ width:10px; }
::-webkit-scrollbar-track{ background: var(--bg-deep); }
::-webkit-scrollbar-thumb{ background: var(--gold-dim); border-radius:10px; }

</style>
""", unsafe_allow_html=True)


def section_header(icon, title, caption=None):
    st.markdown(f"""
    <div class="section-header">
        <span class="icon-chip"><i class="{icon}"></i></span>
        <span>{title}</span>
    </div>
    {f'<div class="section-caption">{caption}</div>' if caption else ''}
    """, unsafe_allow_html=True)


# -------------------------------------------------------
# City <-> State mapping (for responsive location fields)
# -------------------------------------------------------

CITY_STATE_MAP = {
    'Ahmedabad': 'Gujarat',
    'Bengaluru': 'Karnataka',
    'Bhopal': 'Madhya Pradesh',
    'Chandigarh': 'Punjab',
    'Chennai': 'Tamil Nadu',
    'Coimbatore': 'Tamil Nadu',
    'Delhi': 'Delhi',
    'Guwahati': 'Assam',
    'Howrah': 'West Bengal',
    'Hubballi': 'Karnataka',
    'Hyderabad': 'Telangana',
    'Indore': 'Madhya Pradesh',
    'Jaipur': 'Rajasthan',
    'Jodhpur': 'Rajasthan',
    'Kanpur': 'Uttar Pradesh',
    'Kochi': 'Kerala',
    'Kolkata': 'West Bengal',
    'Kozhikode': 'Kerala',
    'Lucknow': 'Uttar Pradesh',
    'Ludhiana': 'Punjab',
    'Madurai': 'Tamil Nadu',
    'Mumbai': 'Maharashtra',
    'Mysuru': 'Karnataka',
    'Nagpur': 'Maharashtra',
    'Noida': 'Uttar Pradesh',
    'Patna': 'Bihar',
    'Pune': 'Maharashtra',
    'Surat': 'Gujarat',
    'Thiruvananthapuram': 'Kerala',
    'Udaipur': 'Rajasthan',
    'Vadodara': 'Gujarat',
    'Warangal': 'Telangana',
}

STATE_CITIES_MAP = {}
for _city, _state in CITY_STATE_MAP.items():
    STATE_CITIES_MAP.setdefault(_state, []).append(_city)

CITY_OPTIONS = sorted(CITY_STATE_MAP.keys())
STATE_OPTIONS = sorted(STATE_CITIES_MAP.keys())

if "city_select" not in st.session_state:
    st.session_state.city_select = "Mumbai"
if "state_select" not in st.session_state:
    st.session_state.state_select = CITY_STATE_MAP[st.session_state.city_select]


def _sync_state_from_city():
    st.session_state.state_select = CITY_STATE_MAP[st.session_state.city_select]


def _sync_city_from_state():
    current_city = st.session_state.city_select
    if CITY_STATE_MAP.get(current_city) != st.session_state.state_select:
        st.session_state.city_select = STATE_CITIES_MAP[st.session_state.state_select][0]


# -------------------------------------------------------
# Hero
# -------------------------------------------------------

st.markdown("""
<div class="hero-card">
    <i class="fa-solid fa-user-tie hero-icon"></i>
    <div class="hero-content">
        <div class="hero-eyebrow"><span class="dash"></span> AI-Powered Value Intelligence</div>
        <p class="main-title">Customer Lifetime <span class="accent">Value Prediction</span></p>
        <p class="sub-title">Machine learning model trained on real e-commerce customer data across India. Enter a customer's profile and get a precise future value estimate instantly &mdash; no technical inputs required.</p>
        <div class="hero-pills">
            <span class="hero-pill gold"><i class="fa-solid fa-bullseye"></i>&nbsp; R&sup2; 0.8556</span>
            <span class="hero-pill green"><i class="fa-solid fa-layer-group"></i>&nbsp; XGBoost Regressor</span>
            <span class="hero-pill neutral"><i class="fa-solid fa-city"></i>&nbsp; 32 Indian Cities</span>
            <span class="hero-pill neutral"><i class="fa-solid fa-sliders"></i>&nbsp; 22 Inputs Only</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

with st.expander("About this model", expanded=False):
    st.markdown(
        """
        <div class="info-row"><span class="i-label"><i class="fa-solid fa-robot" style="color:#D4AF37;"></i> Model</span><span class="i-value">XGBoost Regressor</span></div>
        <div class="info-row"><span class="i-label"><i class="fa-solid fa-bullseye" style="color:#D4AF37;"></i> R² Score</span><span class="i-value">0.8556</span></div>
        <div class="info-row"><span class="i-label"><i class="fa-solid fa-layer-group" style="color:#D4AF37;"></i> Feature Groups</span><span class="i-value">5</span></div>
        <div style="margin-top:10px;">
            <span class="tech-pill"><i class="fa-brands fa-python"></i> Python</span>
            <span class="tech-pill">Pandas</span>
            <span class="tech-pill">XGBoost</span>
            <span class="tech-pill">Scikit-learn</span>
            <span class="tech-pill">Streamlit</span>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)


# =======================================================
# Customer Information
# =======================================================

section_header("fa-solid fa-user-tie", "Customer Information", "Core demographic profile of the customer")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=30
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Female", "Male", "Other"]
    )

with col3:
    membership = st.selectbox(
        "Membership Level",
        ["Gold", "Platinum", "Silver"]
    )

st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)

# =======================================================
# Location Information
# =======================================================

section_header("fa-solid fa-map-location-dot", "Location", "Where the customer is based")

col1, col2, col3 = st.columns(3)

with col1:
    city = st.selectbox(
        "City",
        CITY_OPTIONS,
        key="city_select",
        on_change=_sync_state_from_city
    )

with col2:
    state = st.selectbox(
        "State",
        STATE_OPTIONS,
        key="state_select",
        on_change=_sync_city_from_state
    )

with col3:
    acquisition = st.selectbox(
        "Acquisition Channel",
        [
            'Affiliate',
            'Email Marketing',
            'Organic Search',
            'Paid Ads',
            'Referral',
            'Social Media'
        ]
    )

st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)

# =======================================================
# Purchase Behaviour
# =======================================================

section_header("fa-solid fa-bag-shopping", "Purchase Behaviour", "How the customer shops and spends")

col1, col2 = st.columns(2)

with col1:

    tenure = st.number_input(
        "Customer Tenure (Days)",
        min_value=1,
        value=365
    )

    total_orders = st.number_input(
        "Total Orders",
        min_value=1,
        value=10
    )

    total_items = st.number_input(
        "Total Items Purchased",
        min_value=1,
        value=25
    )

with col2:

    avg_order_value = st.number_input(
        "Average Order Value",
        min_value=0.0,
        value=500.0
    )

    total_spend = st.number_input(
            "Total Spend",
            min_value=0.0,
            value=5000.0
        )

    preferred_category = st.selectbox(
        "Preferred Category",
        [
            'Beauty & Personal Care',
            'Books',
            'Electronics',
            'Fashion',
            'Grocery',
            'Home & Kitchen',
            'Mobile & Accessories',
            'Sports & Fitness'
        ]
    )

st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)

# =======================================================
# Customer Activity
# =======================================================

section_header("fa-solid fa-chart-line", "Customer Activity", "Engagement across web and app touchpoints")

col1, col2 = st.columns(2)

with col1:

    website_visits = st.number_input(
        "Website Visits",
        min_value=0,
        value=100
    )

    app_sessions = st.number_input(
        "App Sessions",
        min_value=0,
        value=80
    )

    days_since_purchase = st.number_input(
        "Days Since Last Purchase",
        min_value=0,
        value=15
    )

with col2:

    purchase_frequency = st.number_input(
        "Purchase Frequency Per Month",
        min_value=0.0,
        value=2.5
    )

    avg_days_between = st.number_input(
        "Average Days Between Orders",
        min_value=0,
        value=30
    )

st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)

# =======================================================
# Customer Service
# =======================================================

section_header("fa-solid fa-star", "Customer Service", "Satisfaction, support and payment preferences")

col1, col2 = st.columns(2)

with col1:

    coupon_usage = st.slider(
        "Coupon Usage Rate",
        0.0,
        1.0,
        0.30
    )

    return_rate = st.slider(
        "Return Rate",
        0.0,
        1.0,
        0.05
    )

with col2:

    support_tickets = st.number_input(
        "Support Tickets",
        min_value=0,
        value=2
    )

    satisfaction = st.slider(
        "Customer Satisfaction",
        1.0,
        5.0,
        4.0
    )

payment_method = st.selectbox(
    "Preferred Payment Method",
    [
        'Cash On Delivery',
        'Credit Card',
        'Debit Card',
        'EMI',
        'Net Banking',
        'UPI'
    ]
)

st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)

predict_button = st.button(
    "✦  Predict Future CLV",
    use_container_width=True
)


# =======================================================
# Prediction Pipeline
# =======================================================

if predict_button:

    with st.spinner("Analyzing customer profile..."):

        # -----------------------------
        # Create Input DataFrame
        # -----------------------------

        input_df = pd.DataFrame({

            "Age": [age],
            "Gender": [gender],
            "City": [city],
            "State": [state],
            "Membership_Level": [membership],
            "Acquisition_Channel": [acquisition],
            "Customer_Tenure_Days": [tenure],
            "Total_Orders": [total_orders],
            "Total_Items_Purchased": [total_items],
            "Total_Spend": [total_spend],
            "Average_Order_Value": [avg_order_value],
            "Preferred_Category": [preferred_category],
            "Website_Visits": [website_visits],
            "App_Sessions": [app_sessions],
            "Days_Since_Last_Purchase": [days_since_purchase],
            "Purchase_Frequency_Per_Month": [purchase_frequency],
            "Average_Days_Between_Orders": [avg_days_between],
            "Coupon_Usage_Rate": [coupon_usage],
            "Return_Rate": [return_rate],
            "Support_Tickets": [support_tickets],
            "Customer_Satisfaction": [satisfaction],
            "Preferred_Payment_Method": [payment_method]

        })

        # ===================================================
        # Feature Engineering
        # ===================================================

        # Purchase Intensity
        input_df["Purchase_Intensity"] = (
            input_df["Total_Orders"] /
            input_df["Customer_Tenure_Days"]
        )

        # Engagement Score
        input_df["Engagement_Score"] = (
            input_df["Website_Visits"] +
            input_df["App_Sessions"]
        )

        # Spend Per Day
        input_df["Spend_Per_Day"] = (
            input_df["Total_Spend"] /
            input_df["Customer_Tenure_Days"]
        )

        # ===================================================
        # One-Hot Encoding
        # ===================================================

        input_df = pd.get_dummies(
            input_df,
            drop_first=True
        )

        # ===================================================
        # Match Training Columns
        # ===================================================

        input_df = input_df.reindex(
            columns=feature_columns,
            fill_value=0
        )

        # ===================================================
        # Make Prediction
        # ===================================================

        prediction = model.predict(input_df)[0]

        # Prevent negative predictions
        prediction = max(0, prediction)

    # ===================================================
    # Customer Value Category
    # ===================================================

    if prediction < 2000:
        segment = "Low Value Customer"
        segment_icon = "fa-solid fa-arrow-trend-down"
        segment_color = "#F0475C"
        gauge_pos = min(max((prediction / 2000) * 33, 3), 33)

    elif prediction < 5000:
        segment = "Medium Value Customer"
        segment_icon = "fa-solid fa-scale-balanced"
        segment_color = "#F5A524"
        gauge_pos = 33 + min(max(((prediction - 2000) / 3000) * 33, 0), 33)

    else:
        segment = "High Value Customer"
        segment_icon = "fa-solid fa-crown"
        segment_color = "#22C55E"
        gauge_pos = 66 + min(max(((prediction - 5000) / 5000) * 34, 0), 34)

    # ===================================================
    # Prediction Result
    # ===================================================

    st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)
    section_header("fa-solid fa-bullseye", "Prediction Result", "Model output for this customer profile")

    col1, col2 = st.columns([2, 1])

    with col1:

        st.markdown(
            f"""
            <div class="result-box">
                <div class="result-label"><i class="fa-solid fa-coins"></i>&nbsp; Predicted Future Customer Lifetime Value</div>
                <div class="result-value">₹ {prediction:,.2f}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            f"""
            <div class="segment-card" style="border-color:{segment_color}55;">
                <div class="segment-icon" style="color:{segment_color};"><i class="{segment_icon}"></i></div>
                <div class="result-label">Customer Segment</div>
                <div class="segment-title" style="color:{segment_color};">{segment}</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        f"""
        <div class="glass-card" style="margin-top:16px; padding:20px 26px;">
            <div class="gauge-track">
                <div class="gauge-marker" style="left:{gauge_pos}%;"></div>
            </div>
            <div class="gauge-labels">
                <span>🔻 Low</span>
                <span>Medium</span>
                <span>High 🔺</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ===================================================
    # Prediction Summary
    # ===================================================

    st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)
    section_header("fa-solid fa-clipboard-list", "Prediction Summary", "Key inputs behind this forecast")

    st.markdown(
        f"""
        <div class="metric-grid">
            <div class="metric-card"><div class="m-icon"><i class="fa-solid fa-cake-candles"></i></div><div class="m-label">Age</div><div class="m-value">{age}</div></div>
            <div class="metric-card"><div class="m-icon"><i class="fa-solid fa-medal"></i></div><div class="m-label">Membership</div><div class="m-value">{membership}</div></div>
            <div class="metric-card"><div class="m-icon"><i class="fa-solid fa-city"></i></div><div class="m-label">City</div><div class="m-value">{city}</div></div>
            <div class="metric-card"><div class="m-icon"><i class="fa-solid fa-map"></i></div><div class="m-label">State</div><div class="m-value">{state}</div></div>
            <div class="metric-card"><div class="m-icon"><i class="fa-solid fa-boxes-stacked"></i></div><div class="m-label">Total Orders</div><div class="m-value">{total_orders}</div></div>
            <div class="metric-card"><div class="m-icon"><i class="fa-solid fa-sack-dollar"></i></div><div class="m-label">Total Spend</div><div class="m-value">₹ {total_spend:,.2f}</div></div>
            <div class="metric-card"><div class="m-icon"><i class="fa-solid fa-receipt"></i></div><div class="m-label">Avg Order Value</div><div class="m-value">₹ {avg_order_value:,.2f}</div></div>
            <div class="metric-card"><div class="m-icon"><i class="fa-solid fa-globe"></i></div><div class="m-label">Website Visits</div><div class="m-value">{website_visits:,.0f}</div></div>
            <div class="metric-card"><div class="m-icon"><i class="fa-solid fa-heart"></i></div><div class="m-label">Satisfaction</div><div class="m-value">{satisfaction} / 5</div></div>
            <div class="metric-card" style="border-color:{segment_color}55;"><div class="m-icon" style="color:{segment_color};"><i class="fa-solid fa-gem"></i></div><div class="m-label">Predicted Future CLV</div><div class="m-value" style="color:{segment_color};">₹ {prediction:,.2f}</div></div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # ===================================================
    # Business Recommendation
    # ===================================================

    st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)
    section_header("fa-solid fa-lightbulb", "Business Recommendation", "Suggested next steps for this customer")

    if prediction < 2000:

        st.markdown(
            """
            <div class="reco-card" style="background:rgba(240,71,92,0.08); border-color:rgba(240,71,92,0.3);">
                <div style="font-weight:700; font-size:15.5px; color:#F0475C;"><i class="fa-solid fa-triangle-exclamation"></i>&nbsp; Low predicted lifetime value</div>
                <ul>
                    <li>Offer personalized discounts to boost engagement.</li>
                    <li>Increase touchpoints through targeted campaigns.</li>
                    <li>Recommend popular, high-conversion products.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif prediction < 5000:

        st.markdown(
            """
            <div class="reco-card" style="background:rgba(245,165,36,0.08); border-color:rgba(245,165,36,0.3);">
                <div style="font-weight:700; font-size:15.5px; color:#F5A524;"><i class="fa-solid fa-circle-info"></i>&nbsp; Moderate future value</div>
                <ul>
                    <li>Upsell premium products aligned to purchase history.</li>
                    <li>Encourage repeat purchases with timely nudges.</li>
                    <li>Provide loyalty rewards to deepen engagement.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            """
            <div class="reco-card" style="background:rgba(34,197,94,0.08); border-color:rgba(34,197,94,0.3);">
                <div style="font-weight:700; font-size:15.5px; color:#22C55E;"><i class="fa-solid fa-crown"></i>&nbsp; Predicted to be highly valuable</div>
                <ul>
                    <li>Retain through VIP programs and priority service.</li>
                    <li>Cross-sell premium products and bundles.</li>
                    <li>Offer exclusive benefits and early access.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

# =======================================================
# Footer
# =======================================================

st.markdown('<hr class="gold-divider">', unsafe_allow_html=True)

st.markdown(
"""
<div class="footer">
    <i class="fa-solid fa-gem"></i>&nbsp; Customer Lifetime Value Prediction System
<br><br>
<div>Made by <strong style="color: #F2D879">Aswin Santhosh</strong> &nbsp;·&nbsp; Machine Learning Project &nbsp;·&nbsp; <a href="https://github.com/AswinSanthoshDev" target="_blank" style="color:#F2D879;text-decoration:none;font-weight:600;">GitHub</a> &nbsp;·&nbsp; <a href="https://www.linkedin.com/in/aswin-santhosh-114b87364/" target="_blank" style="color:#F2D879;text-decoration:none;font-weight:600;">LinkedIn</a></div>

</div>
""",
unsafe_allow_html=True
)