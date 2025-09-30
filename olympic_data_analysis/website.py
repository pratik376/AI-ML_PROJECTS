import streamlit as st
import  pandas as pd

import preprocessing,hepler
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.figure_factory as ff

df=pd.read_csv("athlete_events.csv")
region_df=pd.read_csv("noc_regions.csv")

df=preprocessing.preprocessing(df,region_df)


st.sidebar.title("Olympics Analysis")

user_menu=st.sidebar.radio(
    'select an option',
    ('medal tally','overall analysis','Country-wise Analysis', 'Athlete wise Analysis')
)


if  user_menu=='medal tally':

    st.header("Medal Tally")
    years,country=hepler.country_year_list(df)

    selected_year=st.sidebar.selectbox("Select Year",years)
    selected_country=st.sidebar.selectbox("Select Country",country)
    

    medal_tally=hepler.medal_tally(df,years,country)

    if selected_year == 'Overall' and selected_country == 'Overall':
        st.title("Overall Tally")
    
    if selected_year!='Overall' and selected_country=='Overall':
        st.title("Medal Telly in "+ str(selected_year)+ " Olympics")

    if selected_year=='Overall' and selected_country!='Overall':
        st.title(selected_country+" Overall Performance") 

    if selected_year!= 'Overall' and selected_country!='Overall':
        st.write(selected_country+" Performance in "+str(selected_year)+ " Olympics")      
    st.table(medal_tally)


  
if user_menu=='overall analysis':

    editions=df['Year'].unique().shape[0] -1
    cities=df['City'].unique().shape[0] 
    sports=df['Sport'].unique().shape[0] 
    events=df['Event'].unique().shape[0]
    athletes=df['Name'].unique().shape[0] 
    nations=df['region'].unique().shape[0]

    st.title("TOP STATISTICS")
    col1,col2,col3=st.columns(3)  

    with col1:
        st.header("Editions")
        st.title(editions)
        
    with col2:
        st.header("Hosts")
        st.title(cities)
    with col3:
        st.header("Sports")
        st.title(sports)

    col1,col2,col3 = st.columns(3)

    with col1:
        st.header("Events")
        st.title(events)   
    with col2:
        st.header("Nations")
        st.title(nations)    
    with col3:
        st.header("Athelets")
        st.title(athletes)            

    nations_over_time=hepler.data_over_time(df,'region') 
    st.title("Participating Nation Over The Times")      
    fig=px.line(nations_over_time, x='Year',y='count')
    st.plotly_chart(fig) 

    nations_over_time=hepler.data_over_time(df,'Event') 
    st.title("Events Over The Times")      
    fig=px.line(nations_over_time, x='Year',y='count')
    st.plotly_chart(fig) 

    nations_over_time=hepler.data_over_time(df,'Name') 
    st.title("Athelets Over The Times")      
    fig=px.line(nations_over_time, x='Year',y='count')
    st.plotly_chart(fig) 

    st.title("No of Events over time (Every Sport)")
    fig, ax = plt.subplots(figsize=(20, 20))
    X=df.drop_duplicates(['Year','Sport','Event'])
    ax=sns.heatmap(X.pivot_table(index='Sport', columns='Year',values='Event',aggfunc='count').fillna(0).astype(int),annot=True)
    st.pyplot(fig)


    st.title("Most sucessful Athletes")
    sports_list=df['Sport'].unique().tolist()
    sports_list.sort()
    sports_list.insert(0,'overall')

    selected_sports=st.selectbox("Select a Sport",sports_list)
    x=hepler.most_successful(df,'Overall')
    st.table(x)

if user_menu=='Country-wise Analysis':

    st.sidebar.title('Country-wise Analysis')
    country_list=df['region'].dropna().unique().tolist()
    country_list.sort()

    selected_country=st.sidebar.selectbox('Select a country', country_list)

    country_df=hepler.year_wise_medal_tally(df,selected_country)
    fig=px.line(country_df,x='Year',y='Medal')
    st.title(selected_country+ " Medal Tally over the years")
    st.plotly_chart(fig) 

    st.title(selected_country + " excels in the following sport")

    pt = hepler.country_event_heatmap(df, selected_country)

    if not pt.empty:
      

      fig, ax = plt.subplots()
      sns.heatmap(pt, annot=True, ax=ax)
      st.pyplot(fig)
    else:
      st.warning("No data available to plot the heatmap.")


    st.title("Top 10 Athelets of "+ selected_country)
    top10_Df=hepler.most_successful_countrywise(df,selected_country)
    st.table(top10_Df)





if user_menu=='Athlete wise Analysis':
    athelets_df=df.drop_duplicates(subset=['Name','region'])
    x1=athelets_df['Age'].dropna()
    x2=athelets_df[athelets_df['Medal']=='Gold']['Age'].dropna()
    x3=athelets_df[athelets_df['Medal']=='Silver']['Age'].dropna() 
    x4=athelets_df[athelets_df['Medal']=='Bronze']['Age'].dropna()  

    fig = ff.create_distplot([x1, x2, x3, x4], ['Overall Age', 'Gold Medalist', 'Silver Medalist', 'Bronze Medalist'],show_hist=False, show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = ['Basketball', 'Judo', 'Football', 'Tug-Of-War', 'Athletics',
                     'Swimming', 'Badminton', 'Sailing', 'Gymnastics',
                     'Art Competitions', 'Handball', 'Weightlifting', 'Wrestling',
                     'Water Polo', 'Hockey', 'Rowing', 'Fencing',
                     'Shooting', 'Boxing', 'Taekwondo', 'Cycling', 'Diving', 'Canoeing',
                     'Tennis', 'Golf', 'Softball', 'Archery',
                     'Volleyball', 'Synchronized Swimming', 'Table Tennis', 'Baseball',
                     'Rhythmic Gymnastics', 'Rugby Sevens',
                     'Beach Volleyball', 'Triathlon', 'Rugby', 'Polo', 'Ice Hockey']
   
    for sport in famous_sports:
        temp_df = athelets_df[athelets_df['Sport'] == sport]
        x.append(temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna())
        name.append(sport)

    fig = ff.create_distplot(x, name, show_hist=False, show_rug=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    st.title("Distribution of Age wrt Sports(Gold Medalist)")
    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0, 'Overall')

    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport', sport_list)
    temp_df = hepler.weight_v_height(df,selected_sport)
    fig,ax = plt.subplots()
    ax = sns.scatterplot(x=temp_df['Weight'], y=temp_df['Height'], hue=temp_df['Medal'], style=temp_df['Sex'], s=60)

    st.pyplot(fig)

    st.title("Men Vs Women Participation Over the Years")
    final = hepler.men_vs_women(df)
    fig = px.line(final, x="Year", y=["Male", "Female"])
    fig.update_layout(autosize=False, width=1000, height=600)
    st.plotly_chart(fig)



      


    

    
    
 
