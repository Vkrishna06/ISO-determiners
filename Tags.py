import streamlit as st
import pandas as pd
from openpyxl import load_workbook

#Configuration
EXCEL_PATH = r"C:\\Users\\Uday\\Downloads\\Ds_Empsising_example w Profs Approach v2.xlsx"

# Sheets to manage
sheet_mapping = {
    "lkp_Weighting_Tag_Type": ("Weighting Tag Types", "Manage different types for weighting tags."),
    "lkp_Weighting_Tag_Category": ("Weighting Tag Categories", "Manage categories under each weighting tag type."),
    "Weighting_Tag": ("Weighting Tags", "View and manage all defined weighting tags."),
    "Organization_Weighting_Tag": ("Organization Weighting Tags", "Map organizations to corresponding weighting tags."),
    "Substance_Weighting_Tag": ("Substance Weighting Tags", "Map substances to corresponding weighting tags."),
    "Evidence_Weighting_Tag": ("Evidence Weighting Tags", "Link evidence to weighting tags and manage scores.")
}

# Utility Functions
def load_sheet(sheet_name):
    try:
        df = pd.read_excel(EXCEL_PATH, sheet_name=sheet_name)
        df.columns = df.columns.str.strip()
        return df
    except Exception as e:
        st.error(f"Failed to load {sheet_name}: {e}")
        return pd.DataFrame()

def save_sheet(df, sheet_name):
    try:
        with pd.ExcelWriter(EXCEL_PATH, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False)
        st.success("✅ Changes saved successfully!")
    except Exception as e:
        st.error(f"❌ Error saving changes: {e}")

def search_dataframe(df, search_term):
    if search_term:
        mask = df.apply(lambda row: row.astype(str).str.contains(search_term, case=False, na=False).any(), axis=1)
        return df[mask]
    return df

# Streamlit App 
st.set_page_config(page_title="Weighting Tag Management", layout="wide")

st.markdown("""
    <style>
    .big-title {text-align: center; font-size: 3rem; color: #f63366; margin-top: 2rem; margin-bottom: 0.5rem; font-weight: bold;}
    .sub-header {text-align: center; font-size: 1.2rem; color: #CCCCCC; margin-bottom: 2rem;}
    .section-header {text-align: center; font-size: 1.5rem; color: #f6c90e; margin-bottom: 2rem; margin-top: 2rem; font-weight: bold;}
    .icon-box {background-color: #262730; border: 1px solid #444; border-radius: 15px; padding: 1.5rem; text-align: center; transition: transform 0.2s ease; color: white; box-shadow: 0 4px 8px rgba(0,0,0,0.3);}
    .icon-box:hover {transform: scale(1.03); background-color: #333641;}
    .icon-box h4 {font-size: 1.3rem; color: #f6c90e; margin-bottom: 0.5rem;}
    .icon-box p {font-size: 0.95rem; color: #CCCCCC;}
    .sidebar-title {font-size: 1.5rem; color: #f63366; font-weight: bold; padding-bottom: 10px;}
    section[data-testid="stSidebar"] {background-color: #1f2023;}
    .stRadio > div {flex-direction: column; gap: 1rem;}
    .stRadio div label {font-size: 1.1rem; color: #dddddd;}
    .stRadio div input:checked + label {color: #f6c90e; font-weight: bold;}
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("📚 Navigation")
nav_options = ["Home"] + [v[0] for v in sheet_mapping.values()]
if "navigation_choice" not in st.session_state:
    st.session_state.navigation_choice = "Home"
choice = st.sidebar.radio("Select Sheet", nav_options, index=nav_options.index(st.session_state.navigation_choice))

if choice == "Home":
    st.markdown("<div class='big-title'>Weighting Tag Management System</div>", unsafe_allow_html=True)
    st.markdown("<div class='sub-header'>⚡ A Streamlined Platform to Manage Tag Types, Categories, and Mappings Efficiently</div>", unsafe_allow_html=True)
    st.markdown("<div class='section-header'>✨ Explore the Sections Below</div>", unsafe_allow_html=True)

    cols = st.columns(3)
    for idx, (sheet_key, (sheet_name, sheet_desc)) in enumerate(sheet_mapping.items()):
        with cols[idx % 3]:
            if st.button(f"📄 {sheet_name}"):
                st.session_state.navigation_choice = sheet_name
                st.experimental_rerun()
            st.markdown(f"""
            <div class='icon-box'>
                <h4>{sheet_name}</h4>
                <p>{sheet_desc}</p>
            </div>
            """, unsafe_allow_html=True)

if choice != "Home":
    sheet_key = [k for k, v in sheet_mapping.items() if v[0] == choice][0]
    st.title(f"📄 {choice}")

    df = load_sheet(sheet_key)

    if not df.empty:
        search_key = f"search_term_{choice}"
        search_term = st.text_input("Enter keyword to search across all columns:", key=search_key)

        if search_term:
            filtered_df = search_dataframe(df, search_term)
        else:
            filtered_df = df.copy()

        st.write(f"### Found {len(filtered_df)} matching record(s):")

        if not filtered_df.empty:
            st.data_editor(filtered_df.reset_index(drop=True), use_container_width=True, disabled=True)
        else:
            st.warning("No matching records found.")

        st.markdown("---")
        st.subheader("➕ Add New Record")
        with st.form("add_form"):
            new_data = {}
            for col in df.columns:
                new_data[col] = st.text_input(f"{col}")
            add_submit = st.form_submit_button("✅ Add Record")

        if add_submit:
            df = pd.concat([df, pd.DataFrame([new_data])], ignore_index=True)
            save_sheet(df, sheet_key)
            st.success("Record added successfully!")
            st.experimental_rerun()

        st.markdown("---")
        st.subheader("✏️ Edit Existing Record")
        edit_index = st.number_input("Enter index to edit (0-based index):", min_value=0, max_value=len(df)-1, step=1)
        selected_row = df.iloc[edit_index]

        with st.form("edit_form"):
            updated_data = {}
            for col in df.columns:
                updated_data[col] = st.text_input(f"{col}", value=str(selected_row[col]))
            edit_submit = st.form_submit_button("✅ Save Changes")

        if edit_submit:
            for col in df.columns:
                df.at[edit_index, col] = updated_data[col]
            save_sheet(df, sheet_key)
            st.success("Record updated successfully!")
            st.experimental_rerun()
    else:
        st.warning("No data found or error loading the sheet.")
