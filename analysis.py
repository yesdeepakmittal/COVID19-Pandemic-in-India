import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

from data import CovidData
data_obj = CovidData()

class Color:
    def __init__(self):
        self.confirmed_color = 'navy'
        self.recovered_color = 'green'
        self.death_color = 'indianred'
        self.active_color = 'purple'

class Visualize(Color):
    def __init__(self):
        super().__init__()

    def save_funnel(self):
        timeseries = data_obj.timeseries_data()

        fig = go.Figure(go.Funnel(
            x = [timeseries['totalconfirmed'].iloc[-1],timeseries['totalrecovered'].iloc[-1],
                timeseries['totaldeceased'].iloc[-1]],
            y = ["Total Cases", "Total Recovered",  "Deaths"],
            textposition = "inside",
            textinfo = "value",
            opacity = 0.8, 
            marker = {"color": [self.confirmed_color,self.recovered_color,self.death_color],
                    "line": {"width": 2.5, "color": 'Black'}},
            connector = {"line": {"color": "navy", "dash": "dot", "width": 2.5}}))
        fig.update_layout(
            template="simple_white",
            title={'text': "COVID19: Pandemic in India",'x':0.5,'y':0.9,       
                'xanchor': 'center','yanchor': 'top'})
        fig.update_layout(height=700, template='simple_white',width=600)
        return fig

    def state_wise_total(self):
        statewise_total = data_obj.statewise_total_data()
        temp = statewise_total[statewise_total['State/UT']!='Total']
        temp = temp[temp['State/UT']!='State Unassigned']
        fig = go.Figure(data=[
            go.Bar(name='Death', y=temp['State/UT'], x=temp['Death'],orientation='h',marker_color=self.death_color),
            go.Bar(name='Recovered', y=temp['State/UT'], x=temp['Recovered'],orientation='h',marker_color=self.recovered_color),
            go.Bar(name='Confirmed', y=temp['State/UT'], x=temp['Confirmed'],orientation='h',marker_color=self.confirmed_color)
        ])
        fig.update_layout(barmode='stack',title='Stacked barplot for Statewise Confirmed, Recovered & Death cases', xaxis_title="Cases", yaxis_title="State/UT", 
                            yaxis_categoryorder = 'total ascending', height = 1000,
                            template='simple_white')
        return fig 

    def state_wise_cases(self):
        statewise_total = data_obj.statewise_total_data()
        temp = statewise_total[statewise_total['State/UT']!='Total']
        temp = temp[temp['State/UT']!='State Unassigned']
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=temp['Death'], x=temp['State/UT'],
                            mode='lines+markers',
                            name='Death',marker_color=self.death_color))
        fig.add_trace(go.Scatter(y=temp['Recovered'], x=temp['State/UT'],
                            mode='lines+markers',
                            name='Recovered',marker_color=self.recovered_color))
        fig.add_trace(go.Scatter(y=temp['Active'], x=temp['State/UT'],
                            mode='lines+markers', name='Active',marker_color=self.active_color))
        fig.add_trace(go.Scatter(y=temp['Confirmed'], x=temp['State/UT'],
                            mode='lines+markers', name='Confirmed',marker_color=self.confirmed_color))
        fig.update_layout(height=900,width= 1200, title_text="Statewise Total Covid19 Cases",template='simple_white')
        return fig 

    def state_wise_per_100(self):
        statewise_total = data_obj.statewise_total_data()
        temp = statewise_total[statewise_total['State/UT']!='Total']
        temp = temp[temp['State/UT']!='State Unassigned']
        fig = go.Figure()
        fig.add_trace(go.Scatter(y=temp['MortalityRate%'], x=temp['State/UT'],
                            mode='lines+markers',
                            name='Mortality Rate',marker_color=self.death_color))
        fig.add_trace(go.Scatter(y=temp['RecoveryRate%'], x=temp['State/UT'],
                            mode='lines+markers',
                            name='Recovery Rate',marker_color=self.recovered_color))
        fig.add_trace(go.Scatter(y=temp['Active/100 Confirmed'], x=temp['State/UT'],
                            mode='lines+markers', name='Active/100 Confirmed',marker_color=self.active_color))
        fig.update_layout(height=700,width= 1200, title_text="Statewise Cases per 100 Confirmed",template='simple_white')
        return fig

    def hist_confirmed(self):
        timeseries = data_obj.timeseries_data()
        fig = px.bar(timeseries, x='date', y='totalconfirmed', color_discrete_sequence=[self.confirmed_color],template='simple_white')
        fig.update_layout(title='Cumulative Confirmed Cases', xaxis_title="Date", yaxis_title="No. of Confirmed Cases")
        fig.add_scatter(x=timeseries['date'],y=timeseries['7dyMnConfirmed'],name='7 day mean Confirmed',
                        marker={'color': 'red','opacity': 0.6,'colorscale': 'Viridis'},)
        return fig
    
    def hist_recovered(self):
        timeseries = data_obj.timeseries_data()
        fig = px.bar(timeseries, x='date', y='totalrecovered', 
             color_discrete_sequence=[self.recovered_color],template='simple_white')
        fig.update_layout(title='Cumulative Recovered Cases', xaxis_title="Date", yaxis_title="No. of Recovered Cases")
        fig.add_scatter(x=timeseries['date'],y=timeseries['7dyMnRecovered'],name='7 day mean Recovered',
                        marker={'color': 'red','opacity': 0.6,'colorscale': 'Viridis'},)
        return fig

    def hist_death(self):
        timeseries = data_obj.timeseries_data()
        fig = px.bar(timeseries, x='date', y='totaldeceased', 
                    color_discrete_sequence=[self.death_color],template='simple_white')
        fig.update_layout(title='Cumulative Death Cases', xaxis_title="Date", yaxis_title="No. of Deceased Cases")
        fig.add_scatter(x=timeseries['date'],y=timeseries['7dyMnDeceased'],name='7 day mean Deceased',
                        marker={'color': 'black','opacity': 0.6,'colorscale': 'Viridis'},)
        return fig

    def daywise_analysis(self):
        timeseries = data_obj.timeseries_data()
        fig = px.line(color_discrete_sequence=[self.confirmed_color],template='simple_white')
        fig.add_scatter(x=timeseries['date'],y=timeseries['dailyconfirmed'],name='Daily Confirmed',marker={'color': self.confirmed_color,'opacity': 0.6,'colorscale': 'Viridis'},)
        fig.add_scatter(x=timeseries['date'],y=timeseries['dailyrecovered'],name='Daily Recovered',marker={'color': self.recovered_color,'opacity': 0.6,'colorscale': 'Viridis'},)
        fig.add_scatter(x=timeseries['date'],y=timeseries['dailydeceased'],name='Daily Death',marker={'color': self.death_color,'opacity': 0.6,'colorscale': 'Viridis'})
        fig.update_layout(title='Day Wise Analysis', xaxis_title="Date", yaxis_title="No. of Cases")
        return fig

    def total_cases(self):
        timeseries = data_obj.timeseries_data()
        timeseries['totalactive'] = timeseries.totalconfirmed-timeseries.totalrecovered-timeseries.totaldeceased
        fig = px.line(color_discrete_sequence=[self.confirmed_color],template='simple_white')
        fig.add_scatter(x=timeseries['date'],y=timeseries['totalconfirmed'],name='Total Confirmed',marker={'color': self.confirmed_color,'opacity': 0.6,'colorscale': 'Viridis'},)
        fig.add_scatter(x=timeseries['date'],y=timeseries['totalrecovered'],name='Total Recovered',marker={'color': self.recovered_color,'opacity': 0.6,'colorscale': 'Viridis'},)
        fig.add_scatter(x=timeseries['date'],y=timeseries['totaldeceased'],name='Total Death',marker={'color': self.death_color,'opacity': 0.6,'colorscale': 'Viridis'})
        fig.add_scatter(x=timeseries['date'],y=timeseries['totalactive'],name='Total Active',marker={'color': self.active_color,'opacity': 0.6,'colorscale': 'Viridis'})
        fig.update_layout(title='Total Cases', xaxis_title="Date", yaxis_title="No. of Cases")
        return fig 

    def top21_city(self):
        district_wise = data_obj.district_wise_data()
        temp = district_wise.sort_values('Confirmed').tail(21)
        fig = go.Figure(data=[
            go.Bar(name='Death', y=temp['District'], x=temp['Death'].head(21),orientation='h',marker_color=self.death_color),
            go.Bar(name='Recovered', y=temp['District'], x=temp['Recovered'].head(21),orientation='h',marker_color=self.recovered_color),
            go.Bar(name='Confirmed', y=temp['District'], x=temp['Confirmed'].head(21),orientation='h',marker_color=self.confirmed_color)
        ])
        fig.update_layout(barmode='stack',title='Top21 Cities Confirmed, Recovered & Death Cases(Unknown is Delhi)', xaxis_title="Cases", yaxis_title="District", 
                            yaxis_categoryorder = 'total ascending',
                            template='simple_white')
        return fig
    
    def district_gradient(self):
        district_wise = data_obj.district_wise_data()
        district_wise = district_wise[district_wise['State/UT']!='State Unassigned']
        return district_wise.sort_values('Confirmed', ascending= False).head(30).fillna(0).style\
                                .background_gradient(cmap='Blues',subset=["Confirmed"])\
                                .background_gradient(cmap='Greens',subset=["Recovered"])\
                                .background_gradient(cmap='Reds',subset=["Death"])\
                                .background_gradient(cmap='pink',subset=["Active"])

    def daywise_some_states(self):
        temp = pd.read_csv('https://api.covid19india.org/csv/latest'
                                '/state_wise_daily.csv')
        temp = temp[temp['Status']=='Confirmed']
        fig = go.Figure()
        # fig.add_trace(go.Scatter(y=temp['TT'], x=temp['Date'],
        #                     mode='lines+markers',name='Total'))
        fig.add_trace(go.Scatter(y=temp['UP'], x=temp['Date'],
                            mode='lines+markers',name='Uttar Pradesh'))
        fig.add_trace(go.Scatter(y=temp['MH'], x=temp['Date'],
                            mode='lines+markers',name='Maharashtra'))
        fig.add_trace(go.Scatter(y=temp['DL'], x=temp['Date'],
                            mode='lines+markers',name='Delhi'))
        fig.add_trace(go.Scatter(y=temp['PB'], x=temp['Date'],
                            mode='lines+markers',name='Punjab'))
        fig.add_trace(go.Scatter(y=temp['RJ'], x=temp['Date'],
                            mode='lines+markers',name='Rajasthan'))
        fig.update_layout(title_text="Daywise Confirmed Cases of States",
                        template='simple_white',height=700)
        return fig