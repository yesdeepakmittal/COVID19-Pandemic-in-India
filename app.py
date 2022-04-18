import streamlit as st

st.set_page_config(
     page_title="Impact of Covid19 in India",
     page_icon="./img/favicon.ico",
     layout="wide",
    #  initial_sidebar_state="expanded",
     menu_items={
         'Get Help': 'https://github.com/yesdeepakmittal/COVID19-Pandemic-in-India/issues/new',
         'Report a bug': "https://github.com/yesdeepakmittal/COVID19-Pandemic-in-India/issues/new",
         'About': '''
                  # Impact of Covid19
                  This data analysis is an attempt find which location of India has most cases 
                  and how Covid19 cases increased overtime. The result might not be accurate. 

                  - Check the shared code on [Github](https://github.com/yesdeepakmittal/COVID19-Pandemic-in-India/) and do not forget to hit the star⭐ button.
                  ---
                  '''
     }
 )

with open('report.pdf','rb') as file:
    st.download_button(
        label = 'Download Complete Report',
        data = file,
        file_name='report.pdf',
        mime='pdf'
    )

st.title('Impact of Covid19')
st.subheader('*Analysing the impact of Covid19 on different part of India*')
st.write('''*👉This data analysis is for educational purpose only and may not 
    indicate accurate information. Please use other sources for accurate data.*''')


from analysis import Visualize
obj = Visualize()

fig = obj.save_funnel()
col1, col2 = st.columns(2)
col1.plotly_chart(fig, width=400,height=500)
col2.markdown('''
        - ## Around 32.25 Million Confirmed Cases in India as of record date
        - ## Around 31.44 Million recovered from Covid19 as of record date
        - ## Around 431.55 Thousand people dead due to Covid19 as of record date
''')

fig = obj.state_wise_total()
st.plotly_chart(fig, use_container_width=True)

fig = obj.state_wise_cases()
st.plotly_chart(fig, use_container_width=True)

fig = obj.state_wise_per_100()
st.plotly_chart(fig, use_container_width=True)

fig = obj.hist_confirmed()
st.plotly_chart(fig, use_container_width=True)

fig = obj.hist_recovered()
st.plotly_chart(fig, use_container_width=True)

fig = obj.hist_death()
st.plotly_chart(fig, use_container_width=True)

fig = obj.daywise_analysis()
st.plotly_chart(fig, use_container_width=True)

fig = obj.total_cases()
st.plotly_chart(fig, use_container_width=True)

fig = obj.top21_city()
st.plotly_chart(fig, use_container_width=True)

df = obj.district_gradient()
st.write('30 most affected Cities Data')
st.table(df)

fig = obj.daywise_some_states()
st.plotly_chart(fig, use_container_width=True)

st.markdown('''
        ***This webpage is designed by [Deepak Mittal](https://github.com/yesdeepakmittal) 
            and the code is shared on [Github](https://github.com/yesdeepakmittal/COVID19-Pandemic-in-India)***
''',)