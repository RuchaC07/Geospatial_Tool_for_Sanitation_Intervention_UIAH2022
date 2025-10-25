import streamlit as st
from model import model
st.title("Parameters")

# col1, col2 = st.beta_columns(2)

# with col1:
#     with st.form('Form1'):
#         st.selectbox('Select flavor', ['Vanilla', 'Chocolate'], key=1)
#         st.slider(label='Select intensity', min_value=0, max_value=100, key=4)
#         submitted1 = st.form_submit_button('Submit 1')

# with col2:
#     with st.form('Form2'):
#         st.selectbox('Select Topping', ['Almonds', 'Sprinkles'], key=2)
#         st.slider(label='Select Intensity', min_value=0, max_value=100, key=3)
#         submitted2 = st.form_submit_button('Submit 2')

with st.form('sanitize_method'):
    pop = st.number_input('Population', 0,1000000)
    area = st.number_input('Area in KM')
    build = st.number_input('Buildings Number')
    pop_den = st.number_input("Population Density")
    # st.date_input('Date')

    option = st.selectbox(
        'Building Type',
        ('Residential', 'Education Center', 'Office'))

    submitted = st.form_submit_button("Submit")

   
# with st.form("my_form"):
#    st.write("Inside the form")
#    slider_val = st.slider("Form slider")
#    checkbox_val = st.checkbox("Form checkbox")

#    # Every form must have a submit button.
#    submitted = st.form_submit_button("Submit")
#    if submitted:
#        st.write("slider", slider_val, "checkbox", checkbox_val)

# st.write("Outside the form")
if submitted:
    st.header(model(pop_den)+" Technique is usefull for that area.")


