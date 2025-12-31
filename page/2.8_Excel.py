import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.markdown('---')
st.title('Mock Survey Results filtered by Ages and Departments')

excel_file = 'downloads/Survey_Results.xlsx'
sheet_name = 'DATA'

df = pd.read_excel(excel_file,
                   sheet_name=sheet_name,
                   usecols='B:D',
                   header=3)

df_participants = pd.read_excel(excel_file,
                                sheet_name= sheet_name,
                                usecols='F:G',
                                header=3)

df_participants.dropna(inplace=True) #drops NA values

#Age slider and department multiselect
department = df['Department'].unique().tolist()
ages = df['Age'].unique().tolist()

age_selection = st.slider('Age:',
                          min_value=min(ages),
                          max_value=max(ages),
                          value=(min(ages), max(ages)))

# Initialize session state to store defaults
if "reset" not in st.session_state:
    st.session_state.reset = False

# Example list of departments
departments = department

# Reset defaults after refresh (buggy)
if "age_selection" not in st.session_state:
    st.session_state.age_selection = (23, 65)
if st.session_state.reset:
    st.session_state.reset = False  # Reset the flag
    department_selection = departments
else:
    department_selection = st.multiselect(
        'Select Departments:',
        departments,
        default=departments
    )

# Refresh the app if all options are deselected
if not department_selection:
    st.session_state.reset = False
    st.rerun()

# Update session state with user selections
st.session_state.department_selection = department_selection

#Filter data based on selections
mask = (df['Age'].between(*age_selection)) & df['Department'].isin(department_selection)
number_of_result = df[mask].shape[0]
st.subheader(f'Number of results: {number_of_result}')

#Group data after selections 
df_grouped = df[mask].groupby(by=['Rating']).count()[['Age']]
df_grouped = df_grouped.rename(columns={'Age': 'Votes'})
df_grouped = df_grouped.reset_index()

bar_chart = px.bar(df_grouped,
                          x='Rating',
                          y='Votes',
                          text='Votes',
                          color_discrete_sequence= ['#F63366']*len(df_grouped),
                          template= 'plotly_white')

st.plotly_chart(bar_chart)

st.title('Mock Survey Table with Sorting')
st.dataframe(df, hide_index=True, use_container_width=True)

st.title('Total number of Participants in each Department')
pie_chart = px.pie(df_participants,
                   values='Participants',
                   names='Departments')

st.plotly_chart(pie_chart)
