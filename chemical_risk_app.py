import streamlit as st
import os
import csv
import base64


def run_chemical_risk_app():
 # Setting Up the local Path
    CSV_PATH = r"C:\Users\Uday\OneDrive - George Mason University - O365 Production\Desktop\CAPSTONE\data_files\WeightScoringData.csv"
    EVIDENCE_FOLDER = r"C:\Users\Uday\OneDrive - George Mason University - O365 Production\Desktop\CAPSTONE\Evidence"

    # st.set_page_config(page_title="Chemical Risk Assessment", layout="wide")
    st.title("Chemical Risk Assessment")

    main_option = st.radio("Choose a Section", ["Weighing", "Collected Sanctions"])

    if main_option == "Weighing":
        st.subheader("Weighing Model")
        action = st.radio("Select Action", ["Search Existing", "Add New"])

        # ADD NEW 
        if action == "Add New":
            st.markdown("### ➕ Add New Entry")
            entry_id = st.text_input("Enter ID")
            company_name = st.text_input("Enter Company Name")
            tag_type = st.selectbox("Select Tag Type", ["Company", "Substance", "Evidence", "Other"])

            st.markdown("#### ✅ Sanctions and Indictments (S)")
            s_1 = st.checkbox("S. Attempted Distribution of Synthetic Opioids (+10)")
            s_2 = st.checkbox("S. Precursor Chemical Distribution (+15)")
            s_3 = st.checkbox("S. Specific Opioid Importation Attempts (+12)")
            s_4 = st.checkbox("S. Bitcoin Wallet Associations (+8)")
            s_5 = st.checkbox("S. Money Laundering Involvement (+5)")

            st.markdown("#### ✅ Government Subsidies (G)")
            g_1 = st.checkbox("G. Existence of Subsidies Supporting Production (+10)")
            g_2 = st.checkbox("G. Promotion of Export Industries for Chemicals (+8)")
            g_3 = st.checkbox("G. Lack of Enforcement Support Funding (+5)")

            st.markdown("#### ✅ Complicity Indicators (C)")
            c_1 = st.checkbox("C. Weak Regulatory Framework (+15)")
            c_2 = st.checkbox("C. Minimal Enforcement Actions (+10)")
            c_3 = st.checkbox("C. Failure to Uphold International Agreements (+12)")
            c_4 = st.checkbox("C. Evidence of Cooperation with Traffickers (+20)")
            c_5 = st.checkbox("C. Favorable Market Access for Chemical Producers (+8)")

            # Score Calculations
            S = sum([10 if s_1 else 0, 15 if s_2 else 0, 12 if s_3 else 0, 8 if s_4 else 0, 5 if s_5 else 0])
            G = sum([10 if g_1 else 0, 8 if g_2 else 0, 5 if g_3 else 0])
            C = sum([15 if c_1 else 0, 10 if c_2 else 0, 12 if c_3 else 0, 20 if c_4 else 0, 8 if c_5 else 0])
            total_weight = round(S * 1.2 + G * 1.1 + C * 1.3, 2)

            st.markdown(f"### 🧮 Total Weighted Score: **{total_weight}**")

            if st.button("Save"):
                if not entry_id or not company_name:
                    st.warning("Please enter ID and Company Name.")
                else:
                    new_row = [
                        entry_id, tag_type, company_name,
                        int(s_1), int(s_2), int(s_3), int(s_4), int(s_5),
                        int(g_1), int(g_2), int(g_3),
                        int(c_1), int(c_2), int(c_3), int(c_4), int(c_5),
                        total_weight
                    ]

                    file_exists = os.path.exists(CSV_PATH)

                    with open(CSV_PATH, "a", newline="") as f:
                        writer = csv.writer(f)
                        if not file_exists:
                            writer.writerow([
                                "Id", "Tag", "Company Name",
                                "S.Attempted Distribution of Synthetic Opioids",
                                "S.PrecursorChemical Distribution",
                                "S.Specific Opioid Importation Attempts",
                                "S.Bitcoin Wallet Associations",
                                "S.Money Laundering Involvement",
                                "G.Existence of Subsidies Supporting Production",
                                "G.Promotion of Export Industries for Chemicals",
                                "G.Lack of Enforcement Support Funding",
                                "C.Weak Regulatory Framework",
                                "C.Minimal Enforcement Actions",
                                "C.Failure to Uphold International Agreements",
                                "C.Evidence of Cooperation with Traffickers",
                                "C.Favorable Market Access for Chemical Producers",
                                "Total Weight"
                            ])
                        writer.writerow(new_row)

                    st.success("✅ Record saved successfully!")

        # SEARCH EXISTING 
        elif action == "Search Existing":
            import csv

            st.markdown("### 🔍 Search and Filter Records")

            
            input_search = st.text_input("🔤 Search Company Name")
            input_tag = st.selectbox("🏷️ Filter by Tag Type", ["All", "Company", "Substance", "Evidence", "Other"])
            input_weight = st.selectbox("📊 Filter by Total Weight", ["All", "50+", "70+", "90+"])

            
            if st.button("Apply Filters"):
                st.session_state['filters_applied'] = True
                st.session_state['search_term'] = input_search
                st.session_state['filter_tag'] = input_tag
                st.session_state['weight_filter'] = input_weight
                st.session_state.pop('record_to_edit', None)  # reset edit on new filter

           
            if st.button("Reset Filters"):
                for key in ["filters_applied", "search_term", "filter_tag", "weight_filter", "record_to_edit"]:
                    st.session_state.pop(key, None)

           
            if st.session_state.get('filters_applied'):
                search_term = st.session_state.get('search_term', "")
                filter_tag = st.session_state.get('filter_tag', "All")
                weight_filter = st.session_state.get('weight_filter', "All")

                if not os.path.exists(CSV_PATH):
                    st.error("CSV file not found.")
                else:
                    with open(CSV_PATH, "r") as f:
                        reader = csv.reader(f)
                        rows = list(reader)

                    header = rows[0]
                    data = rows[1:]

                    # Filter data
                    filtered = []
                    for row in data:
                        company = row[2]
                        tag = row[1]
                        try:
                            weight = float(row[-1])
                        except:
                            weight = 0

                        matches = True
                        if search_term and search_term.lower() not in company.lower():
                            matches = False
                        if filter_tag != "All" and tag != filter_tag:
                            matches = False
                        if weight_filter == "50+" and weight < 50:
                            matches = False
                        if weight_filter == "70+" and weight < 70:
                            matches = False
                        if weight_filter == "90+" and weight < 90:
                            matches = False

                        if matches:
                            filtered.append(row)

                    if not filtered:
                        st.warning("No matching records found.")
                    else:
                        st.success(f"🔎 {len(filtered)} record(s) found")

                        
                        display_options = []
                        record_map = {}
                        for row in filtered:
                            label = f"[{row[0]}] - {row[2]} (Score: {row[-1]})"
                            display_options.append(label)
                            record_map[label] = row

                        selected_option = st.selectbox("✏️ Select a record to edit", display_options)

                        if selected_option:
                            st.session_state['record_to_edit'] = record_map[selected_option]

                       
                        if 'record_to_edit' in st.session_state:
                            st.markdown("### 📝 Edit Selected Record")

                            record = st.session_state['record_to_edit']

                            def safe_int(val):
                                return int(val) if str(val).isdigit() else 0

                            entry_id = st.text_input("Edit ID", value=record[0])
                            tag_options = ["Company", "Substance", "Evidence", "Other"]
                            default_index = tag_options.index(record[1]) if record[1] in tag_options else 0
                            tag_type = st.selectbox("Edit Tag Type", tag_options, index=default_index)
                            company_name = st.text_input("Edit Company Name", value=record[2])

                            st.markdown("#### ✅ Sanctions and Indictments (S)")
                            s_1 = st.checkbox("S. Attempted Distribution of Synthetic Opioids (+10)", value=bool(safe_int(record[3])))
                            s_2 = st.checkbox("S. Precursor Chemical Distribution (+15)", value=bool(safe_int(record[4])))
                            s_3 = st.checkbox("S. Specific Opioid Importation Attempts (+12)", value=bool(safe_int(record[5])))
                            s_4 = st.checkbox("S. Bitcoin Wallet Associations (+8)", value=bool(safe_int(record[6])))
                            s_5 = st.checkbox("S. Money Laundering Involvement (+5)", value=bool(safe_int(record[7])))

                            st.markdown("#### ✅ Government Subsidies (G)")
                            g_1 = st.checkbox("G. Existence of Subsidies Supporting Production (+10)", value=bool(safe_int(record[8])))
                            g_2 = st.checkbox("G. Promotion of Export Industries for Chemicals (+8)", value=bool(safe_int(record[9])))
                            g_3 = st.checkbox("G. Lack of Enforcement Support Funding (+5)", value=bool(safe_int(record[10])))

                            st.markdown("#### ✅ Complicity Indicators (C)")
                            c_1 = st.checkbox("C. Weak Regulatory Framework (+15)", value=bool(safe_int(record[11])))
                            c_2 = st.checkbox("C. Minimal Enforcement Actions (+10)", value=bool(safe_int(record[12])))
                            c_3 = st.checkbox("C. Failure to Uphold International Agreements (+12)", value=bool(safe_int(record[13])))
                            c_4 = st.checkbox("C. Evidence of Cooperation with Traffickers (+20)", value=bool(safe_int(record[14])))
                            c_5 = st.checkbox("C. Favorable Market Access for Chemical Producers (+8)", value=bool(safe_int(record[15])))

                            # Recalculate weight
                            S = sum([10 if s_1 else 0, 15 if s_2 else 0, 12 if s_3 else 0, 8 if s_4 else 0, 5 if s_5 else 0])
                            G = sum([10 if g_1 else 0, 8 if g_2 else 0, 5 if g_3 else 0])
                            C = sum([15 if c_1 else 0, 10 if c_2 else 0, 12 if c_3 else 0, 20 if c_4 else 0, 8 if c_5 else 0])
                            total_weight = round(S * 1.2 + G * 1.1 + C * 1.3, 2)

                            st.markdown(f"### 🧮 Updated Total Weighted Score: **{total_weight}**")

                            if st.button("Save Changes"):
                                with open(CSV_PATH, "r", newline="") as f:
                                    reader = list(csv.reader(f))
                                header = reader[0]
                                data = reader[1:]

                                updated_row = [
                                    entry_id, tag_type, company_name,
                                    int(s_1), int(s_2), int(s_3), int(s_4), int(s_5),
                                    int(g_1), int(g_2), int(g_3),
                                    int(c_1), int(c_2), int(c_3), int(c_4), int(c_5),
                                    total_weight
                                ]

                                target_id = record[0]
                                for i in range(len(data)):
                                    if data[i][0] == target_id:
                                        data[i] = updated_row
                                        break

                                with open(CSV_PATH, "w", newline="") as f:
                                    writer = csv.writer(f)
                                    writer.writerow(header)
                                    writer.writerows(data)

                                st.success("✅ Record updated successfully!")
                                del st.session_state['record_to_edit']
    # COLLECTED SANCTIONS 
    elif main_option == "Collected Sanctions":
        st.header("Collected Sanctions – Evidence PDFs")

        if not os.path.exists(EVIDENCE_FOLDER):
            st.error("Evidence folder not found.")
        else:
            action = st.radio("Select Action", ["Search Existing", "Upload New"])

            if action == "Search Existing":
                st.markdown("#### 🔍 Search Evidence Files")
                search_term = st.text_input("Enter keyword (e.g., company name)")
                all_pdfs = [f for f in os.listdir(EVIDENCE_FOLDER) if f.lower().endswith(".pdf")]
                matched_pdfs = [f for f in all_pdfs if search_term.lower() in f.lower()] if search_term else all_pdfs

                if not matched_pdfs:
                    st.warning("No matching PDF files found.")
                else:
                    selected_pdf = st.selectbox("Matching Files", sorted(matched_pdfs))
                    file_path = os.path.join(EVIDENCE_FOLDER, selected_pdf)
                    with open(file_path, "rb") as f:
                        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                    st.markdown(f"#### Preview: {selected_pdf}")
                    st.markdown(f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="800px"></iframe>', unsafe_allow_html=True)

            elif action == "Upload New":
                st.markdown("#### 📤 Upload a New Sanction Evidence PDF")
                uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
                if uploaded_file is not None:
                    save_path = os.path.join(EVIDENCE_FOLDER, uploaded_file.name)
                    with open(save_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())
                    st.success(f"File uploaded and saved as: {uploaded_file.name}")
                    st.balloons()
