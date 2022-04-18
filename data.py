import pandas as pd
import json
import requests
import math

class CovidData:
    def __init__(self):
        self.df1 = "https://api.covid19india.org/state_district_wise.json"
        self.df2 = "https://api.covid19india.org/data.json"
    
    def getting_data(self,url):
        response = requests.get(url)
        data = response.content.decode('utf-8')
        return data
    
    def district_wise_data(self):
        df_state = json.loads(self.getting_data(self.df1))
        lis = []
        state_names = df_state.keys()
        for state in state_names:
            district_names = df_state[state]['districtData'].keys() 
            for district in district_names:
                temp = df_state[state]['districtData'][district]
                var_lis = [state,district,temp.get('confirmed'),temp.get('recovered'),
                        temp.get('active'),temp.get('deceased')]
                lis.append(var_lis)
                
        return pd.DataFrame(lis,columns=['State/UT','District','Confirmed',
                                              'Recovered','Active','Death'])

    def statewise_total_data(self):
        df = json.loads(self.getting_data(self.df2))
        temp = [[i['state'],i['confirmed'],i['recovered'],i['active'],i['deaths'],i['lastupdatedtime']]
                    for i in df['statewise']]
        statewise_total = pd.DataFrame(temp,columns=['State/UT','Confirmed','Recovered','Active','Death','LastUpdateTime'])

        statewise_total['Confirmed']=statewise_total['Confirmed'].astype('int')
        statewise_total['Recovered']=statewise_total['Recovered'].astype('int')
        statewise_total['Active']=statewise_total['Active'].astype('int')
        statewise_total['Death']=statewise_total['Death'].astype('int')
        statewise_total['RecoveryRate%'] = round(statewise_total['Recovered']/statewise_total['Confirmed']*100,2)
        statewise_total['MortalityRate%'] = round(statewise_total['Death']/statewise_total['Confirmed']*100,2)
        statewise_total['Active/100 Confirmed'] = round(statewise_total['Active']/statewise_total['Confirmed']*100,2)
        statewise_total['LastUpdateTime'] = pd.to_datetime(statewise_total.LastUpdateTime.str.split(expand=True)[0])
        statewise_total.sort_values(by='Confirmed',ascending=False,inplace=True)
        return statewise_total

    def timeseries_data(self):
        df = json.loads(self.getting_data(self.df2))
        timeseries = [list(i.values()) for i in df['cases_time_series']]
        timeseries = pd.DataFrame(timeseries,columns=df['cases_time_series'][0].keys())
        timeseries['dailyconfirmed'] = timeseries['dailyconfirmed'].astype('int')
        timeseries['dailydeceased'] = timeseries['dailydeceased'].astype('int')
        timeseries['dailyrecovered'] = timeseries['dailyrecovered'].astype('int')
        timeseries['totalconfirmed'] = timeseries['totalconfirmed'].astype('int')
        timeseries['totaldeceased'] = timeseries['totaldeceased'].astype('int')
        timeseries['totalrecovered'] = timeseries['totalrecovered'].astype('int')
        timeseries['7dyMnConfirmed'] = timeseries.totalconfirmed.rolling(7).mean().fillna(0).astype(int)
        timeseries['7dyMnRecovered'] = timeseries.totalrecovered.rolling(7).mean().fillna(0).astype(int)
        timeseries['7dyMnDeceased'] = timeseries.totaldeceased.rolling(7).mean().fillna(0).astype(int)
        return timeseries

    def test_data(self):
        df = json.loads(self.getting_data(self.df2))
        values = [list(i.values()) for i in df["tested"]]
        tests = pd.DataFrame(values, columns=list(df["tested"][0].keys()))
        for i,value in enumerate(tests['totalsamplestested']):
            if value=='':
                avg = math.ceil((int(tests['totalsamplestested'].iloc[i-1])+int(tests['totalsamplestested'].iloc[i+1]))/2)
                tests['totalsamplestested'].iloc[i] = avg 
        tests['totalsamplestested'] = tests['totalsamplestested'].astype('int')
        return tests

    def time_series_state(self):
        time_series_state = pd.read_csv('https://api.covid19india.org/csv/latest'
                                        '/state_wise_daily.csv')
        del time_series_state['TT']
        time_series_state = time_series_state.melt(id_vars=['Status','Date'], 
                            value_vars=time_series_state.columns[2:],
                            value_name='Census',var_name='State')
        time_series_state = time_series_state.pivot_table(index=['Date', 'State'], 
                                                        columns=['Status'], 
                                                        values='Census')
        time_series_state = time_series_state.reset_index()

        given_data = json.loads(self.getting_data(self.df1))
        state_names = given_data.keys()
        given_dic = {}
        for state in state_names:
            given_dic[given_data[state]['statecode']] =state
        
        given_dic['DD'] = 'Daman and Diu'
        time_series_state['State-Name'] = time_series_state['State'].map(given_dic)
        time_series_state['Date'] = pd.to_datetime(time_series_state['Date'])
        time_series_state.set_index('Date',inplace=True)
        return time_series_state    