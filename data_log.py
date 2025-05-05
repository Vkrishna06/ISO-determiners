import streamlit as st
import pandas as pd
from openpyxl import load_workbook

EXCEL_PATH = r"C:\Users\Uday\Downloads\Key_Value Data Collector and Tracer v2.xlsx"
SHEET_LOG = "Demo_Data_Log"  
SHEET_OBJECT = "Demo_Object_Log"
SHEET_ATTRIBUTE = "Attribute_Log"
SHEET_SOURCE = "Data _Source_Log"  
SHEET_LIBRARY = "Library_Log"


@st.cache_data(show_spinner=False)  
def load_excel_with_values(excel_path, sheet_name):
    wb = load_workbook(excel_path, data_only=True)  
    sheet = wb[sheet_name]
    data = sheet.values
    columns = next(data)  
    df = pd.DataFrame(data, columns=columns)
    return df


def run_data_log_viewer_and_entry():
    
    df_log = load_excel_with_values(EXCEL_PATH, SHEET_LOG)
    df_obj = load_excel_with_values(EXCEL_PATH, SHEET_OBJECT)
    df_attr = load_excel_with_values(EXCEL_PATH, SHEET_ATTRIBUTE)
    df_source = load_excel_with_values(EXCEL_PATH, SHEET_SOURCE)  
    df_library = load_excel_with_values(EXCEL_PATH, SHEET_LIBRARY)

    
    df_log.columns = df_log.columns.str.strip()
    df_obj.columns = df_obj.columns.str.strip()
    df_attr.columns = df_attr.columns.str.strip()
    df_source.columns = df_source.columns.str.strip()
    df_library.columns = df_library.columns.str.strip()

    
    st.sidebar.title("Navigation")
    section = st.sidebar.radio("Select Section", ["View All", "Search Data", "Add New Data Log Entry"])

    
    st.title("🧾 Data Log Viewer and Entry")

    
    if section == "View All":
        st.header("View All Data")
        st.dataframe(df_log)

    
    elif section == "Search Data":
        st.header("Search Entries")

        
        search_term = st.text_input("Search by Anchor Object Title or Attribute Value", "", key="search", max_chars=100)

        if search_term:
            
            df_filtered = df_log[df_log["Anchor_Object Title"].str.contains(search_term, case=False, na=False) |
                                 df_log["Attribute_Value"].str.contains(search_term, case=False, na=False)]
        else:
            df_filtered = df_log

        st.dataframe(df_filtered)

    
    elif section == "Add New Data Log Entry":
        st.header("Add New Data Log Entry")

       
        next_id = int(df_log["Data_Log_ID"].max()) + 1 if not df_log.empty else 1
        st.markdown(f"**Next `Data_Log_ID`:** `{next_id}`")

        
        anchor_id = st.selectbox("Anchor Object ID", df_obj["Object_ID"].dropna().unique())

        
        anchor_row = df_obj[df_obj["Object_ID"] == anchor_id].iloc[0]
        anchor_name = anchor_row.get("Anchor_Object_Name", "")  
        anchor_type = anchor_row.get("Object_Type_SubType", "")

        st.text_input("Anchor Object Title", value=anchor_name, disabled=True)  
        st.text_input("Anchor Object Type-SubType", value=anchor_type, disabled=True)

        
        ordering_override = st.text_input("Ordering Override (optional)")

        
        attr_id = st.selectbox("Attribute ID", df_attr["Attribute_ID"].dropna().unique())
        attr_name = df_attr[df_attr["Attribute_ID"] == attr_id].iloc[0].get("Attribute_Name", "")
        st.text_input("Registered Attribute", value=attr_name, disabled=True)

        new_attr = st.text_input("New Attribute (optional)")
        attr_value = st.text_area("Attribute Value (required)", height=80)

        
        process_statuses = [
            "", "Unprocessed", "Processed Fully", "Processed Partially (NLP/NER)",
            "Processed Partially (OCR)", "Processed Partially (Object Recognition)",
            "Processed Partially (Substance Reference Matched)", "Archived"
        ]
        process_status = st.selectbox("Process Status", process_statuses)

        process_result = st.text_area("Process Results (optional)", height=80)  
        evidence_match = st.selectbox("Evidence ID Matches", process_statuses)

        # Source inputs
        src_record_id = st.text_input("Source Record ID (optional)")
        src_location = st.text_area("Source Location Description (optional)", height=80)  
        src_value = st.text_area("Source Value (optional)", height=80)  

        # Data Source ID and Name
        source_id = st.selectbox("Data Source ID", df_source["Data_Source_ID"].dropna().unique())
        source_name = df_source[df_source["Data_Source_ID"] == source_id].iloc[0].get("Data_Source_Name", "")
        st.text_input("Data Source Name", value=source_name, disabled=True)

        # Library ID and Name
        library_id = st.selectbox("Library ID", df_library["Library_ID"].dropna().unique())
        library_name = df_library[df_library["Library_ID"] == library_id].iloc[0].get("Library_Name", "")
        st.text_input("Library Name", value=library_name, disabled=True)

        # Save new entry
        if st.button("✅ Add Data Log Entry"):
            new_row = {
                "Data_Log_ID": next_id,
                "Anchor_Object_ID": anchor_id,
                "Anchor_Object Title": anchor_name,
                "Anchor_Object Type-SubType": anchor_type,
                "Ordering Override": ordering_override,
                "Attribute_ID": attr_id,
                "Registered Attribute": attr_name,
                "New Attribute (to be registered)": new_attr,
                "Attribute_Value": attr_value,
                "Process Status": process_status,
                "Process Results": process_result,
                "Evidence ID Matches": evidence_match,
                "Source_Record_ID": src_record_id,
                "Source Location Description": src_location,
                "Source_Value": src_value,
                "Data_Source_ID": source_id,
                "Data Source Name": source_name,
                "Library_ID": library_id,
                "Library Name": library_name
            }

           
            df_log = pd.concat([df_log, pd.DataFrame([new_row])], ignore_index=True)

            
            with pd.ExcelWriter(EXCEL_PATH, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
                df_log.to_excel(writer, sheet_name=SHEET_LOG, index=False)

            st.success("✅ Entry saved to Demo_Data_Log successfully!")
            st.rerun()  
