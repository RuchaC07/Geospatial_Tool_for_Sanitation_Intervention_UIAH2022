import streamlit as st
from PIL import Image

st.title("What's this about?")
st.markdown("---")

# Problem Statement
st.subheader("Problem Statement")
st.markdown("Geo-spatial tool to support decision making for sanitation interventions in urban areas.\
            Spatially demarcate settlement areas and recommend suitable sanitation options to decision makers.")

# Image representing the flow
image_flow = Image.open('geoflow.jpg')
st.image(image_flow, caption='Flow Diagram')

st.markdown("---")

# Sanitation Techniques
st.subheader("Sanitation Techniques")

# FSM
st.subheader("FSM")
st.markdown('''
Involves the storage, collection, transport, treatment, and safe disposal of fecal sludge accumulated in onsite sanitation systems''')
st.subheader("Benefits of FSM")

st.markdown('''
1)Reduces potential human contact with fecal-borne pathogens.
2)Minimizes odors and nuisances from overflowing tanks or pits.
3)Enables the production and sale of end-products like recycled water, soil conditioners, and energy products.

''')

image_fsm = Image.open('FSM-CARTOON.jpg')
st.image(image_fsm, caption='FMS')

st.markdown("---")

# Sewerage
st.subheader("SEWERAGE")
st.markdown('''
The system by which waste matter is carried away in sewers and made harmless
''')
st.subheader("Benefits of SEWERAGE")

st.markdown('''
1)Provides efficient removal of wastewater and refuse through sewers.
2)Helps in maintaining cleanliness and hygiene in urban areas.
3)Enables centralized treatment of sewage for safe disposal or reuse.

''')

image_sewerage = Image.open('SEWEAGE-CARTOON.jpg')
st.image(image_sewerage, caption='SEWERAGE...')

# DEWATS
st.subheader("DEWATS")
st.markdown('''
Refers to wastewater treatment systems that operate at or near the point of waste generation.
''')
st.subheader("Benefits of DEWATS")

st.markdown('''
1)Reduces groundwater vulnerability by recharging aquifers with treated wastewater.
2)Provides localized treatment and reuse of wastewater.
3)Helps in preserving water quality.

''')

image_sewerage = Image.open('DEWATS-CATOON.png')
st.image(image_sewerage, caption='SEWERAGE...')
