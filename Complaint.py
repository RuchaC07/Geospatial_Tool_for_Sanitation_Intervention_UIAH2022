import pandas as  pd
import streamlit as st

from gsheetsdb import connect

# Create a connection object.
conn = connect()

SCOPE = "https://www.googleapis.com/auth/spreadsheets"
# SPREADSHEET_ID = "1QlPTiVvfRM82snGN6LELpNkOwVI1_Mp9J9xeJe-QoaA"
SHEET_NAME = "Database"
GSHEET_URL = f"https://docs.google.com/spreadsheets/d/1WDh2yXwmDWi_9cKgWRJF0o-cYI7dMPZNnfX8jGZSIgM/edit?usp=sharing"



def connect_to_gsheet():
    # Create a connection object.

    sheet_url = st.secrets["public_gsheets_url"]
    return sheet_url

def run_query(query):
    rows = conn.execute(query)

    rows = rows.fetchall()

    return rows




def get_data() -> pd.DataFrame:
    sheet_url = st.secrets["public_gsheets_url"]
    print(sheet_url)
    rows = run_query(f'SELECT * FROM "{sheet_url}"')
    print(rows)

    df = pd.DataFrame(data = rows)


    return df


def add_row_to_gsheet(gsheet_connector, row) -> None:
    print("j")
    print(gsheet_connector)
    gsheet_connector.values().append(

        body=dict(values=row),
        valueInputOption="USER_ENTERED",
    ).execute()


st.set_page_config(page_title="Complaints report", page_icon="🐞", layout="centered")

st.title("🐞 Complaint report!")

gsheet_connector = connect_to_gsheet()

st.sidebar.write(
    f"This app shows how a Streamlit app can interact easily with a [Google Sheet]({GSHEET_URL}) to read or store data."
)



form = st.form(key="annotation")

with form:
    cols = st.columns((1, 1))
    Reporter = cols[0].text_input("Report author:")
    complaint_type = cols[1].selectbox(
        "Complaint type:", ["Severage-Type", "Drinking-Water"], index=0
    )

    comment = st.text_area("Comment:")
    region_type = st.selectbox(
        "Region type:", ["Region"+str(i) for i in range(20)], index=0
    )
    cols = st.columns(2)
    date = cols[0].date_input("Complaint date :")
    complaint_severity = cols[1].slider("Complaint severity:", 1, 5, 2)
    submitted = st.form_submit_button(label="Submit")


if submitted:
    add_row_to_gsheet(
        gsheet_connector,
        [[Reporter, complaint_type, comment,region_type, str(date), complaint_severity]],
    )
    st.success("Thanks! Your bug was recorded.")
    st.balloons()

expander = st.expander("See all records!s")
with expander:
    st.write(f"Open original [Google Sheet]({GSHEET_URL})")
    st.dataframe(get_data())# import google_auth_httplib2