import streamlit as st
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# st.set_page_config(page_title='Live DASHBOARD',  layout='wide', page_icon=':ambulance:')

#this is the header


t1, t2 = st.columns((0.07,1))

# t1.image('images/index.png', width = 120)
t2.title("LIVE DASHBOARD FOR COMPLAINT TRACKING")
t2.markdown(" **tel:** 01392 451192 **| website:** https://www.aqua_nets.nhs.in **| email:** mailto:data.science@aqua_nets.nhs.in")



## Data

with st.spinner('Updating Report...'):

    #Metrics setting and rendering

    hosp_df = pd.read_excel('DataforMock.xlsx',sheet_name = 'Hospitals')
    hosp = st.selectbox('Choose Regions', hosp_df, help = 'Filter report to show only one Region')

    m1, m2, m3, m4 = st.columns((1,1,1,1))

    todf = pd.read_excel('DataforMock.xlsx',sheet_name = 'metrics')
    to = todf[(todf['Hospital Attended']==hosp) & (todf['Metric']== 'Total Complaints Remaning')]
    ch = todf[(todf['Hospital Attended']==hosp) & (todf['Metric']== ' Avg time to resolve the complaints')]
    print(to)
    print(ch)
    m1.write('')
    m2.metric(label ='Total Complaints Remaining',value = int(to['Value']), delta = str(int(to['Previous']))+' Compared to 1 hour ago', delta_color = 'inverse')
    m3.metric(label ='Total Resolving time for complaints',value = str(int(ch['Value']))+" Mins", delta = str(int(ch['Previous']))+' Compared to 1 hour ago', delta_color = 'inverse')
    m1.write('')

    # Number of Completed Handovers by Hour

    g1, g2 = st.columns((1,1))
    
    fgdf = pd.read_excel('DataforMock.xlsx',sheet_name = 'Graph')

    fgdf = fgdf[fgdf['Hospital Attended']==hosp]

    fig = px.bar(fgdf, x = 'Arrived Destination Resolved', y='Number of Handovers', template = 'seaborn')

    fig.update_traces(marker_color='#264653')

    fig.update_layout(title_text="Number of Complaints Resolved",title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None)

    g1.plotly_chart(fig, use_container_width=True)

    # Predicted Number of Arrivals

    fcst = pd.read_excel('DataforMock.xlsx',sheet_name = 'Forecast')

    fcst = fcst[fcst['Hospital Attended']==hosp]

    fig = px.bar(fcst, x = 'Arrived Destination Resolved', y='y', template = 'seaborn')

    fig.update_traces(marker_color='#7A9E9F')

    fig.update_layout(title_text="Number of new Complaints ",title_x=0,margin= dict(l=0,r=10,b=10,t=30), yaxis_title=None, xaxis_title=None)

    g2.plotly_chart(fig, use_container_width=True)

    # Average Completed Handover Duration by hour

    # Waiting Handovers table

with st.spinner('Report updated!'):
    time.sleep(1)

# Performance Section

with st.expander("Previous Analysis"):

    hhc24 = pd.read_excel('DataforMock.xlsx',sheet_name = 'HospitalHandoversCompleted')

    colourcode = []

    for i in range(0,13):
        colourcode.append(hhc24['c'+str(i)].tolist())

    hhc24 = hhc24[['RegionWise','Total complaints','In Progress','Average time to resolve','0 to 15 days','15 to 30 days','30 to 60 days','60 to 90 days','90 to 120 days','120 days','% 15 days','% 30 days']]

    fig = go.Figure(
            data = [go.Table (columnorder = [0,1,2,3,4,5,6,7,8,9,10,11,12], columnwidth = [18,12],
                header = dict(
                 values = list(hhc24.columns),
                 font=dict(size=11, color = 'white'),
                 fill_color = '#264653',
                 line_color = 'rgba(255,255,255,0.2)',
                 align = ['left','center'],
                 #text wrapping
                 height=20
                 )
              , cells = dict(
                  values = [hhc24[K].tolist() for K in hhc24.columns],
                  font=dict(size=10),
                  align = ['left','center'],
                  fill_color = colourcode,
                  line_color = 'rgba(255,255,255,0.2)',
                  height=20))])

    fig.update_layout(title_text="Total Complaints Completed in the Past 120 days",title_font_color = '#264653',title_x=0,margin= dict(l=0,r=10,b=10,t=30), height=400)

    st.plotly_chart(fig, use_container_width=True)


# Contact Form

with st.expander("Contact us"):
    with st.form(key='contact', clear_on_submit=True):

        email = st.text_input('Contact Email')
        st.text_area("Query","Please fill in all the information or we may not be able to process your request")

        submit_button = st.form_submit_button(label='Send Information')
