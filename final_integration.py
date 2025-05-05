import streamlit as st
from Key_value_sheet import run_key_value_log_app
from data_log import run_data_log_viewer_and_entry
from attribute_log import run_attribute_log_app
from chemical_risk_app import run_chemical_risk_app


st.set_page_config(page_title="Illicit Synthetic Opioid (ISO) Determination Engine", layout="wide")

#CSS Styling 
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 3rem;
        color: #f63366;
        padding-top: 1rem;
        padding-bottom: 0.5rem;
        font-weight: bold;
    }
    .sub-title {
        text-align: center;
        font-size: 1.2rem;
        color: #CCCCCC;
        margin-bottom: 2rem;
    }
    .stRadio > div {
        flex-direction: row !important;
        justify-content: center;
        gap: 2rem;
    }
    .icon-box {
        background-color: #262730;
        border: 1px solid #444;
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.3);
        transition: transform 0.2s ease;
        color: white;
    }
    .icon-box:hover {
        transform: scale(1.03);
        background-color: #333641;
    }
    .icon-box h4 {
        font-size: 1.3rem;
        color: #f6c90e;
        margin-bottom: 0.5rem;
    }
    .icon-box p {
        font-size: 0.95rem;
        color: #CCCCCC;
    }
    </style>
""", unsafe_allow_html=True)

#Sidebar Navigation
with st.sidebar:
    st.title("📁 Navigation")
    nav_choice = st.radio("Go to", [
        "Home",
        "Key-Value Object Log",
        "Data Log",
        "Attribute Log Manager",
        "Risk Assessment"
    ])

# Home Page Layout
def render_home():
    st.markdown("<div class='main-title'>Illicit Synthetic Opioid (ISO) Determination Engine</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-title'>🚨 A Streamlined Platform to Assess, Trace, and Manage Chemical Risk Intelligence Efficiently</div>", unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/2913/2913461.png", width=100)

    st.markdown("---")
    st.markdown("## 🧭 Select a Module Below")

    selected = st.radio(
        "",
        [
            "Key-Value Object Log",
            "Data Log",
            "Attribute Log Manager",
            "Risk Assessment"
        ],
        horizontal=True,
        index=None
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="icon-box">
            <h4>📚 Key-Value : Object Log</h4>
            <p>Trace object logs and custom entries through a flexible data model.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="icon-box">
            <h4>📄 Data Log</h4>
            <p>Manage data logs and entries linked to attributes and sources.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="icon-box">
            <h4>🧾 Attribute Log</h4>
            <p>Manage structured attributes tied to substances and sanctions.</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="icon-box">
            <h4>📊 Risk Assessment</h4>
            <p>Score and analyze chemical sources and evidence to determine risk.</p>
        </div>
        """, unsafe_allow_html=True)

    return selected

# Main Routing
if nav_choice == "Home":
    selected_page = render_home()
    if selected_page == "Key-Value Object Log":
        run_key_value_log_app()
    elif selected_page == "Data Log":
        run_data_log_viewer_and_entry()
    elif selected_page == "Attribute Log Manager":
        run_attribute_log_app()
    elif selected_page == "Risk Assessment":
        run_chemical_risk_app()
else:
    if nav_choice == "Key-Value Object Log":
        run_key_value_log_app()
    elif nav_choice == "Data Log":
        run_data_log_viewer_and_entry()
    elif nav_choice == "Attribute Log Manager":
        run_attribute_log_app()
    elif nav_choice == "Risk Assessment":
        run_chemical_risk_app()
