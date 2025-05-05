import streamlit as st
import pandas as pd


def run_attribute_log_app():

    # st.set_page_config(page_title="Attribute Log Manager", layout="wide")

    EXCEL_PATH = r"C:\Users\Uday\Downloads\Key_Value Data Collector and Tracer v2.xlsx"
    SHEET_NAME = "Attribute_Log"
    source_column_key = "Source?"  

    # Source dropdown values
    source_options = [
        "Spring 2025 Key-Value Methodology",
        "2019 TraCCC Data",
        "2025 Re-conxsituted Data",
        "Other (Type Manually)"
    ]

    # Load and clean data
    def load_attribute_data():
        df = pd.read_excel(EXCEL_PATH, sheet_name=SHEET_NAME)
        df.columns = df.columns.str.strip()

        df = df.dropna(subset=["Attribute_ID"])  # Remove blank rows

        df['Attribute_ID'] = pd.to_numeric(df['Attribute_ID'], errors='coerce').astype('Int64')
        df['Attribute_Name'] = df['Attribute_Name'].fillna("None")
        df[source_column_key] = df[source_column_key].fillna("None")
        df['Comments'] = df['Comments'].fillna("None")
        df['Old_TraCCC_Attribute_ID'] = df['Old_TraCCC_Attribute_ID'].fillna("None")

        return df

    # Save to Excel using reliable method
    def save_attribute_data(df):
        try:
            df = df.copy()
            with pd.ExcelWriter(EXCEL_PATH, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                df.to_excel(writer, sheet_name=SHEET_NAME, index=False)
            return True
        except Exception as e:
            st.error(f"❌ Error saving data: {e}")
            return False

    df = load_attribute_data()

    st.title("🧾 Attribute Log Management")
    option = st.radio("Select an action:", ["View All", "Search/Edit", "Add New Attribute"])

    # VIEW ALL
    if option == "View All":
        st.subheader("📋 All Attributes")
        st.markdown(f"### Total records loaded: **{len(df)}**")
        st.dataframe(df)

    #SEARCH / EDIT 
    elif option == "Search/Edit":
        st.subheader("🔍 Search & Edit Attribute")
        search = st.text_input("Search by Attribute Name")
        filtered_df = df[df['Attribute_Name'].str.contains(search, case=False, na=False)] if search else df

        if not filtered_df.empty:
            st.write(f"### Found {len(filtered_df)} record(s):")
            st.dataframe(filtered_df)

            selection_options = [
                f"{i} - {row['Attribute_Name']}" for i, row in df.loc[filtered_df.index].iterrows()
            ]
            selection_map = dict(zip(selection_options, filtered_df.index.tolist()))
            selected_label = st.selectbox("Select a record to edit/delete:", options=selection_options)
            true_index = selection_map[selected_label]
            selected_row = df.loc[true_index]

            with st.form("edit_form"):
                attr_name = st.text_input("Attribute Name", value=selected_row['Attribute_Name'])

                default_source = selected_row[source_column_key]
                selected_source = st.selectbox(
                    "Select Source",
                    options=source_options,
                    index=source_options.index(default_source) if default_source in source_options else len(source_options) - 1
                )

                if selected_source == "Other (Type Manually)":
                    source = st.text_input("Enter Custom Source", value=default_source if default_source not in source_options else "")
                else:
                    source = selected_source

                comments = st.text_input("Comments", value=selected_row['Comments'])
                old_id = st.text_input("Old TraCCC Attribute ID", value=str(selected_row['Old_TraCCC_Attribute_ID']))

                submitted_edit = st.form_submit_button("✅ Save Changes")
                submitted_delete = st.form_submit_button("🗑️ Delete Record")

            if submitted_edit:
                df.at[true_index, 'Attribute_Name'] = attr_name
                df.at[true_index, source_column_key] = source
                df.at[true_index, 'Comments'] = comments
                df.at[true_index, 'Old_TraCCC_Attribute_ID'] = old_id if old_id else "None"

                if save_attribute_data(df):
                    st.success("✅ Changes saved!")
                    st.rerun()

            elif submitted_delete:
                try:
                    st.info(f"Attempting to delete index: {true_index}")
                    df = df.drop(index=true_index)
                    df.reset_index(drop=True, inplace=True)

                    if save_attribute_data(df):
                        st.success("🗑️ Record deleted successfully!")
                        st.rerun()
                    else:
                        st.error("⚠️ Failed to save after deletion.")
                except Exception as e:
                    st.error(f"❌ Exception during delete: {e}")
        else:
            st.warning("No matching records found.")

    # ADD NEW 
    elif option == "Add New Attribute":
        st.subheader("➕ Register New Attribute")

        if st.session_state.get("entry_added"):
            st.success(f"✅ Attribute added successfully!")
            if st.button("➕ Add Another Attribute"):
                st.session_state["entry_added"] = False
                st.rerun()
            st.stop()

        next_id = df['Attribute_ID'].max() + 1 if not df.empty else 0

        st.markdown("### 📌 Select Source")
        selected_source = st.selectbox("Select Source", options=source_options, key="source_selector")

        if selected_source == "Other (Type Manually)":
            manual_source = st.text_input("Enter Custom Source", key="manual_source_input")
            final_source = manual_source
        else:
            final_source = selected_source

        with st.form("add_form"):
            attr_name = st.text_input("Attribute Name")
            comments = st.text_input("Comments")
            old_id = st.text_input("Old TraCCC Attribute ID (optional)")

            submitted = st.form_submit_button("✅ Add Attribute")

        if submitted:
            new_row = {
                "Attribute_ID": next_id,
                "Attribute_Name": attr_name,
                source_column_key: final_source,
                "Comments": comments,
                "Old_TraCCC_Attribute_ID": old_id if old_id else "None"
            }

            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

            if save_attribute_data(df):
                st.session_state["entry_added"] = True
                st.rerun()
