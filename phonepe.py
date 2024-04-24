#                                                  Importing Libraries

import streamlit as st
import os
import json
import pandas as pd
import pyodbc
import mysql.connector
import requests
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image 

# -----------------------------------------------------------------------------------------------------------------------------------------

#                                                 1) Aggregate Transactions

path_1="D:/PhonePe_Project/pulse/data/aggregated/transaction/country/india/state/" #the path from the pulse data aggregate transactions
aggre_trans_list = os.listdir(path_1)

column_1={"States":[], "Years":[], "Quarter":[], "Transaction_type":[], "Transaction_count":[], "Transaction_amount":[]}

for state in aggre_trans_list:
    present_states=path_1+state+"/"
    aggre_year_list=os.listdir(present_states)
    
    for year in aggre_year_list:
        present_year=present_states+year+"/"
        aggre_file_list=os.listdir(present_year)
        
        for file in aggre_file_list:
            present_file=present_year+file
            data=open(present_file, "r")
            S=json.load(data)

            for i in S["data"]["transactionData"]:
                name=i["name"]
                count=i["paymentInstruments"][0]["count"]
                amount=i["paymentInstruments"][0]["amount"]
                column_1["Transaction_type"].append(name)
                column_1["Transaction_count"].append(count)
                column_1["Transaction_amount"].append(amount)
                column_1["States"].append(state)
                column_1["Years"].append(year)
                column_1["Quarter"].append(int(file.strip(".json")))

aggre_transaction=pd.DataFrame(column_1)

aggre_transaction["States"] = aggre_transaction["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
aggre_transaction["States"] = aggre_transaction["States"].str.replace("-"," ")
aggre_transaction["States"] = aggre_transaction["States"].str.title()
aggre_transaction["States"] = aggre_transaction["States"].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli and Daman Diu")

# -----------------------------------------------------------------------------------------------------------------------------------------

#                                                      2) Aggregate Users

path_2="D:/PhonePe_Project/pulse/data/aggregated/user/country/india/state/"  #aggregate users path
aggre_user_list = os.listdir(path_2)

column_2 = {"States":[], "Years":[], "Quarter":[], "Brands":[], "Transaction_count":[], "Percentage":[]}

for state in aggre_user_list:
    present_states = path_2+state+"/"
    aggre_year_list = os.listdir(present_states)
    
    for year in aggre_year_list:
        present_year = present_states+year+"/"
        aggre_file_list = os.listdir(present_year)
        
        for file in aggre_file_list:
            present_file = present_year+file
            data = open(present_file, "r")
            U = json.load(data)
            
            try:

                for i in U["data"]["usersByDevice"]:
                    brand = i["brand"]
                    count =i["count"]
                    percentage = i["percentage"]
                    column_2["Brands"].append(brand)
                    column_2["Transaction_count"].append(count)
                    column_2["Percentage"].append(percentage)
                    column_2["States"].append(state)
                    column_2["Years"].append(year)
                    column_2["Quarter"].append(int(file.strip(".json")))
            except:
                pass

aggre_user=pd.DataFrame(column_2)

aggre_user["States"] = aggre_user["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
aggre_user["States"] = aggre_user["States"].str.replace("-"," ")
aggre_user["States"] = aggre_user["States"].str.title()
aggre_user["States"] = aggre_user["States"].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli and Daman Diu")

# -----------------------------------------------------------------------------------------------------------------------------------------

#                                                   3) Map Transaction

path_3="D:/PhonePe_Project/pulse/data/map/transaction/hover/country/india/state/"  #map transactions path
map_trans_list = os.listdir(path_3)

column_3 = {"States":[], "Years":[], "Quarter":[], "District":[], "Transaction_count":[], "Transaction_amount":[]}

for state in map_trans_list:
    present_states = path_3+state+"/"
    map_year_list = os.listdir(present_states)
    
    for year in map_year_list:
        present_year = present_states+year+"/"
        map_file_list = os.listdir(present_year)
        
        for file in map_file_list:
            present_file = present_year+file
            data = open(present_file, "r")
            D = json.load(data)
            
            for i in D["data"]["hoverDataList"]:
                name = i["name"]
                count = i["metric"][0]["count"]
                amount = i["metric"][0]["amount"]
                column_3["District"].append(name)
                column_3["Transaction_count"].append(count)
                column_3["Transaction_amount"].append(amount)
                column_3["States"].append(state)
                column_3["Years"].append(year)
                column_3["Quarter"].append(int(file.strip(".json")))

map_transaction=pd.DataFrame(column_3)

map_transaction["States"] = map_transaction["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
map_transaction["States"] = map_transaction["States"].str.replace("-"," ")
map_transaction["States"] = map_transaction["States"].str.title()
map_transaction["States"] = map_transaction["States"].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli and Daman Diu")

# -----------------------------------------------------------------------------------------------------------------------------------------


#                                                           4) Map User

path_4="D:/PhonePe_Project/pulse/data/map/user/hover/country/india/state/" #map users path
map_user_list = os.listdir(path_4)

column_4 = {"States":[], "Years":[], "Quarter":[], "Districts":[], "RegisteredUser":[], "AppOpens":[]}

for state in map_user_list:
    present_states = path_4+state+"/"
    map_year_list = os.listdir(present_states)
    
    for year in map_year_list:
        present_year = present_states+year+"/"
        map_file_list = os.listdir(present_year)
        
        for file in map_file_list:
            present_file=present_year+file
            data=open(present_file, "r")
            H = json.load(data)
            
            for i in H["data"]["hoverData"].items():
                district = i[0]
                registereduser = i[1]["registeredUsers"]
                appopens = i[1]["appOpens"]
                column_4["Districts"].append(district)
                column_4["RegisteredUser"].append(registereduser)
                column_4["AppOpens"].append(appopens)
                column_4["States"].append(state)
                column_4["Years"].append(year)
                column_4["Quarter"].append(int(file.strip(".json")))

map_user = pd.DataFrame(column_4)

map_user["States"] = map_user["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
map_user["States"] = map_user["States"].str.replace("-"," ")
map_user["States"] = map_user["States"].str.title()
map_user["States"] = map_user["States"].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli and Daman Diu")

# -----------------------------------------------------------------------------------------------------------------------------------------


#                                                        5) Top Transactions

path_5="D:/PhonePe_Project/pulse/data/top/transaction/country/india/state/" #top transactions path
top_trans_list = os.listdir(path_5)

column_5 = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "Transaction_count":[], "Transaction_amount":[]}

for state in top_trans_list:
    present_states = path_5+state+"/"
    top_trans_list = os.listdir(present_states)
       
    for year in top_trans_list:
        present_year = present_states+year+"/"
        top_file_list = os.listdir(present_year)
                
        for file in top_file_list:
            present_file = present_year+file
            data = open(present_file, "r")
            A = json.load(data)
            
            for i in A["data"]["pincodes"]:
                entityName = i["entityName"]
                count = i["metric"]["count"]
                amount = i["metric"]["amount"]
                column_5["Pincodes"].append(entityName)
                column_5["Transaction_count"].append(count)
                column_5["Transaction_amount"].append(amount)
                column_5["States"].append(state)
                column_5["Years"].append(year)
                column_5["Quarter"].append(int(file.strip(".json")))

top_transaction = pd.DataFrame(column_5)

top_transaction["States"] = top_transaction["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
top_transaction["States"] = top_transaction["States"].str.replace("-"," ")
top_transaction["States"] = top_transaction["States"].str.title()
top_transaction["States"] = top_transaction["States"].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli and Daman Diu")

# -----------------------------------------------------------------------------------------------------------------------------------------


#                                                             6) Top User

path_6 = "D:/PhonePe_Project/pulse/data/top/user/country/india/state/" #top users path
top_user_list = os.listdir(path_6)

column_6 = {"States":[], "Years":[], "Quarter":[], "Pincodes":[], "RegisteredUser":[]}

for state in top_user_list:
    present_states = path_6+state+"/"
    top_year_list = os.listdir(present_states)

    for year in top_year_list:
        present_year = present_states+year+"/"
        top_file_list = os.listdir(present_year)

        for file in top_file_list:
            present_file = present_year+file
            data = open(present_file,"r")
            K = json.load(data)

            for i in K["data"]["pincodes"]:
                name = i["name"]
                registereduser = i["registeredUsers"]
                column_6["Pincodes"].append(name)
                column_6["RegisteredUser"].append(registereduser)
                column_6["States"].append(state)
                column_6["Years"].append(year)
                column_6["Quarter"].append(int(file.strip(".json")))


top_user = pd.DataFrame(column_6)

top_user["States"] = top_user["States"].str.replace("andaman-&-nicobar-islands","Andaman and Nicobar")
top_user["States"] = top_user["States"].str.replace("-"," ")
top_user["States"] = top_user["States"].str.title()
top_user["States"] = top_user["States"].str.replace("dadra-&-nagar-haveli-&-daman-&-diu","Dadra and Nagar Haveli and Daman Diu")

# -----------------------------------------------------------------------------------------------------------------------------------------

#                                                         MySQL Connection

host=""      # give your host name 
user=""      # give your user name
password=""  # give your password 
database=""  # give your database name

mydb=mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)
cursor = mydb.cursor()

# -----------------------------------------------------------------------------------------------------------------------------------------


#  Create & Insert ->  "Aggregate Transaction" Table

create_query1 = '''CREATE TABLE if not exists aggregate_transaction (States varchar(100),
                                                                   Years int,
                                                                   Quarter int,
                                                                   Transaction_type varchar(100),
                                                                   Transaction_count bigint,
                                                                   Transaction_amount bigint
                                                                   )'''
cursor.execute(create_query1)
mydb.commit()

for index, row in aggre_transaction.iterrows():
    insert_query1 = '''INSERT INTO aggregate_transaction (States, Years, Quarter, Transaction_type, Transaction_count, Transaction_amount)
                                                            values(%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Transaction_type"],
              row["Transaction_count"],
              row["Transaction_amount"]
              )
    cursor.execute(insert_query1,values)
    mydb.commit()

# -----------------------------------------------------------------------------------------------------------------------------------------

# Create & Insert -> "Aggregate User" Table

create_query2 = '''CREATE TABLE if not exists aggregate_user (States varchar(100),
                                                              Years int,
                                                              Quarter int,
                                                              Brands varchar(100),
                                                              Transaction_count bigint,
                                                              Percentage float)'''
cursor.execute(create_query2)
mydb.commit()

for index, row in aggre_user.iterrows():
    insert_query2 = '''INSERT INTO aggregate_user (States, Years, Quarter, Brands, Transaction_count, Percentage)
                                                    values(%s,%s,%s,%s,%s,%s)'''

    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Brands"],
              row["Transaction_count"],
              row["Percentage"])
    cursor.execute(insert_query2, values)
    mydb.commit()

# -----------------------------------------------------------------------------------------------------------------------------------------

# Create & Insert "Map Transaction" Table

create_query3 = '''CREATE TABLE if not exists map_transaction(States varchar(100),
                                                               Years int,
                                                               Quarter int,
                                                               District varchar(100),
                                                               Transaction_count bigint,
                                                               Transaction_amount float)'''
cursor.execute(create_query3)
mydb.commit()

for index, row in map_transaction.iterrows():
            insert_query3 = '''INSERT INTO map_transaction (States, Years, Quarter, District, Transaction_count, Transaction_amount)
                               values (%s,%s,%s,%s,%s,%s)'''

            values = (
                row["States"],
                row["Years"],
                row["Quarter"],
                row["District"],
                row["Transaction_count"],
                row["Transaction_amount"]
            )
            cursor.execute(insert_query3, values)
            mydb.commit()

# -----------------------------------------------------------------------------------------------------------------------------------------

# Create & Insert "Map User" Table

create_query4 = '''CREATE TABLE if not exists map_user (States varchar(100),
                                                        Years int,
                                                        Quarter int,
                                                        Districts varchar(100),
                                                        RegisteredUser bigint,
                                                        AppOpens bigint)'''
cursor.execute(create_query4)
mydb.commit()

for index, row in map_user.iterrows():
    insert_query4 = '''INSERT INTO map_user (States, Years, Quarter, Districts, RegisteredUser, AppOpens)
                        values (%s,%s,%s,%s,%s,%s)'''
    
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Districts"],
              row["RegisteredUser"],
              row["AppOpens"])
    cursor.execute(insert_query4, values)
    mydb.commit()

# -----------------------------------------------------------------------------------------------------------------------------------------

# Create & Insert "Top Transaction" Table

create_query5 = '''CREATE TABLE if not exists top_transaction (States varchar(100),
                                                                Years int,
                                                                Quarter int,
                                                                Pincodes int,
                                                                Transaction_count bigint,
                                                                Transaction_amount bigint)'''
cursor.execute(create_query5)
mydb.commit()

for index, row in top_transaction.iterrows():
    insert_query5 = '''INSERT INTO top_transaction (States, Years, Quarter, Pincodes, Transaction_count, Transaction_amount)
                                                    values(%s,%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Pincodes"],
              row["Transaction_count"],
              row["Transaction_amount"])
    cursor.execute(insert_query5, values)
    mydb.commit()

# -----------------------------------------------------------------------------------------------------------------------------------------

# Create & Insert "Top User" Table

create_query6 = '''CREATE TABLE if not exists top_user (States varchar(100),
                                                        Years int,
                                                        Quarter int,
                                                        Pincodes int,
                                                        RegisteredUser bigint
                                                        )'''
cursor.execute(create_query6)
mydb.commit()

for index, row in top_user.iterrows():
    insert_query6 = '''INSERT INTO top_user (States, Years, Quarter, Pincodes, RegisteredUser)
                                            values(%s,%s,%s,%s,%s)'''
    values = (row["States"],
              row["Years"],
              row["Quarter"],
              row["Pincodes"],
              row["RegisteredUser"])
    cursor.execute(insert_query6, values)
    mydb.commit()

# -----------------------------------------------------------------------------------------------------------------------------------------

#                                                          CREATE DATAFRAMES FROM SQL
#   MySQL DB Connection

host=""      # give your host name 
user=""      # give your user name
password=""  # give your password 
database=""  # give your database name

mydb=mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
    )
cursor = mydb.cursor()

# -----------------------------------------------------------------------------------------------------------------------------------------

# Aggregated_transaction

cursor.execute("select * from aggregate_transaction;")
table1 = cursor.fetchall()
Aggre_trans = pd.DataFrame(table1,columns = ("States", "Years", "Quarter", "Transaction_type", "Transaction_count", "Transaction_amount"))

# -----------------------------------------------------------------------------------------------------------------------------------------

#  Aggregated_user

cursor.execute("select * from aggregate_user")
table2 = cursor.fetchall()
Aggre_user = pd.DataFrame(table2,columns = ("States", "Years", "Quarter", "Brands", "Transaction_count", "Percentage"))

# -----------------------------------------------------------------------------------------------------------------------------------------

#  Map_transaction

cursor.execute("select * from map_transaction")
table3 = cursor.fetchall()
Map_trans = pd.DataFrame(table3,columns = ("States", "Years", "Quarter", "Districts", "Transaction_count", "Transaction_amount"))

# -----------------------------------------------------------------------------------------------------------------------------------------

#  Map_user

cursor.execute("select * from map_user")
table4 = cursor.fetchall()
Map_user = pd.DataFrame(table4,columns = ("States", "Years", "Quarter", "Districts", "RegisteredUser", "AppOpens"))

# -----------------------------------------------------------------------------------------------------------------------------------------

#  Top_transaction

cursor.execute("select * from top_transaction")
table5 = cursor.fetchall()
Top_trans = pd.DataFrame(table5,columns = ("States", "Years", "Quarter", "Pincodes", "Transaction_count", "Transaction_amount"))

# -----------------------------------------------------------------------------------------------------------------------------------------

#  Top_user

cursor.execute("select * from top_user")
table6 = cursor.fetchall()
Top_user = pd.DataFrame(table6, columns = ("States", "Years", "Quarter", "Pincodes", "RegisteredUser"))

# -----------------------------------------------------------------------------------------------------------------------------------------

def animate_all_amount():
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response =requests.get(url)
    data1 = json.loads(response.content)
    state_names_tra = [feature["properties"]["ST_NM"] for feature in data1["features"]]
    state_names_tra.sort()

    df_state_names_tra = pd.DataFrame({"States":state_names_tra})

    frames = []

    for year in Map_user["Years"].unique():
        for quarter in Aggre_trans["Quarter"].unique():

            at1 = Aggre_trans[(Aggre_trans["Years"]==year)&(Aggre_trans["Quarter"]==quarter)]
            atf1 = at1[["States","Transaction_amount"]]
            atf1 = atf1.sort_values(by="States")
            atf1["Years"]=year
            atf1["Quarter"]=quarter
            frames.append(atf1)

    merged_df = pd.concat(frames)

    fig_tra = px.choropleth(merged_df, geojson= data1, locations= "States", featureidkey= "properties.ST_NM", color= "Transaction_amount",
                            color_continuous_scale= "Sunsetdark", range_color= (0,4000000000), hover_name= "States", title = "TRANSACTION AMOUNT",
                            animation_frame="Years", animation_group="Quarter")

    fig_tra.update_geos(fitbounds= "locations", visible =False)
    fig_tra.update_layout(width =600, height= 700)
    fig_tra.update_layout(title_font= {"size":25})
    return st.plotly_chart(fig_tra)

# -----------------------------------------------------------------------------------------------------------------------------------------

def payment_count():
    attype= Aggre_trans[["Transaction_type", "Transaction_count"]]
    att1= attype.groupby("Transaction_type")["Transaction_count"].sum()
    df_att1= pd.DataFrame(att1).reset_index()
    fig_pc= px.bar(df_att1,x= "Transaction_type",y= "Transaction_count",title= "TRANSACTION TYPE and TRANSACTION COUNT",
                color_discrete_sequence=px.colors.sequential.Redor_r)
    fig_pc.update_layout(width=600, height= 500)
    return st.plotly_chart(fig_pc)

# -----------------------------------------------------------------------------------------------------------------------------------------

def animate_all_count():
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response= requests.get(url)
    data1= json.loads(response.content)
    state_names_tra= [feature["properties"]["ST_NM"]for feature in data1["features"]]
    state_names_tra.sort()

    df_state_names_tra= pd.DataFrame({"States":state_names_tra})


    frames= []

    for year in Aggre_trans["Years"].unique():
        for quarter in Aggre_trans["Quarter"].unique():

            at1= Aggre_trans[(Aggre_trans["Years"]==year)&(Aggre_trans["Quarter"]==quarter)]
            atf1= at1[["States", "Transaction_count"]]
            atf1=atf1.sort_values(by="States")
            atf1["Years"]=year
            atf1["Quarter"]=quarter
            frames.append(atf1)

    merged_df = pd.concat(frames)

    fig_tra= px.choropleth(merged_df, geojson= data1, locations= "States",featureidkey= "properties.ST_NM",
                        color= "Transaction_count", color_continuous_scale="Sunsetdark", range_color= (0,3000000),
                        title="TRANSACTION COUNT", hover_name= "States", animation_frame= "Years", animation_group= "Quarter")

    fig_tra.update_geos(fitbounds= "locations", visible= False)
    fig_tra.update_layout(width= 600, height= 700)
    fig_tra.update_layout(title_font={"size":25})
    return st.plotly_chart(fig_tra)

# -----------------------------------------------------------------------------------------------------------------------------------------

def payment_amount():
    attype= Aggre_trans[["Transaction_type","Transaction_amount"]]
    att1= attype.groupby("Transaction_type")["Transaction_amount"].sum()
    df_att1= pd.DataFrame(att1).reset_index()
    fig_tra_pa= px.bar(df_att1, x= "Transaction_type", y= "Transaction_amount", title= "TRANSACTION TYPE and TRANSACTION AMOUNT",
                    color_discrete_sequence= px.colors.sequential.Blues_r)
    fig_tra_pa.update_layout(width= 600, height= 500)
    return st.plotly_chart(fig_tra_pa)

# -----------------------------------------------------------------------------------------------------------------------------------------

def reg_all_states(state):
    mu= Map_user[["States","Districts","RegisteredUser"]]
    mu1= mu.loc[(mu["States"]==state)]
    mu2= mu1[["Districts", "RegisteredUser"]]
    mu3= mu2.groupby("Districts")["RegisteredUser"].sum()
    mu4= pd.DataFrame(mu3).reset_index()
    fig_mu= px.bar(mu4, x= "Districts", y= "RegisteredUser", title= "DISTRICTS and REGISTERED USER",
                color_discrete_sequence=px.colors.sequential.Bluered_r)
    fig_mu.update_layout(width= 1000, height= 500)
    return st.plotly_chart(fig_mu)

# -----------------------------------------------------------------------------------------------------------------------------------------

def transaction_amount_year(sel_year):
    url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response= requests.get(url)
    data1= json.loads(response.content)
    state_names_tra= [feature["properties"]['ST_NM']for feature in data1["features"]]
    state_names_tra.sort()

    year= int(sel_year)
    atay= Aggre_trans[["States","Years","Transaction_amount"]]
    atay1= atay.loc[(Aggre_trans["Years"]==year)]
    atay2= atay1.groupby("States")["Transaction_amount"].sum()
    atay3= pd.DataFrame(atay2).reset_index()

    fig_atay= px.choropleth(atay3, geojson= data1, locations= "States", featureidkey= "properties.ST_NM",
                            color= "Transaction_amount", color_continuous_scale="rainbow", range_color=(0,800000000000),
                            title="TRANSACTION AMOUNT and STATES", hover_name= "States")

    fig_atay.update_geos(fitbounds= "locations", visible= False)
    fig_atay.update_layout(width=600,height=700)
    fig_atay.update_layout(title_font= {"size":25})
    return st.plotly_chart(fig_atay)

# -----------------------------------------------------------------------------------------------------------------------------------------

def payment_count_year(sel_year):
    year= int(sel_year)
    apc= Aggre_trans[["Transaction_type", "Years", "Transaction_count"]]
    apc1= apc.loc[(Aggre_trans["Years"]==year)]
    apc2= apc1.groupby("Transaction_type")["Transaction_count"].sum()
    apc3= pd.DataFrame(apc2).reset_index()

    fig_apc= px.bar(apc3,x= "Transaction_type", y= "Transaction_count", title= "PAYMENT COUNT and PAYMENT TYPE",
                    color_discrete_sequence=px.colors.sequential.Brwnyl_r)
    fig_apc.update_layout(width=600, height=500)
    return st.plotly_chart(fig_apc)

# -----------------------------------------------------------------------------------------------------------------------------------------

def transaction_count_year(sel_year):
    url= "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    response= requests.get(url)
    data1=json.loads(response.content)
    state_names_tra= [feature["properties"]["ST_NM"]for feature in data1["features"]]
    state_names_tra.sort()

    year= int(sel_year)
    atcy= Aggre_trans[["States", "Years", "Transaction_count"]]
    atcy1= atcy.loc[(Aggre_trans["Years"]==year)]
    atcy2= atcy1.groupby("States")["Transaction_count"].sum()
    atcy3= pd.DataFrame(atcy2).reset_index()

    fig_atcy= px.choropleth(atcy3, geojson=data1, locations= "States", featureidkey= "properties.ST_NM",
                            color= "Transaction_count", color_continuous_scale= "rainbow",range_color=(0,3000000000),
                            title= "TRANSACTION COUNT and STATES",hover_name= "States")
    fig_atcy.update_geos(fitbounds= "locations", visible= False)
    fig_atcy.update_layout(width=600, height= 700)
    fig_atcy.update_layout(title_font={"size":25})
    return st.plotly_chart(fig_atcy)

# -----------------------------------------------------------------------------------------------------------------------------------------

def payment_amount_year(sel_year):
    year= int(sel_year)
    apay = Aggre_trans[["Years", "Transaction_type", "Transaction_amount"]]
    apay1= apay.loc[(Aggre_trans["Years"]==year)]
    apay2= apay1.groupby("Transaction_type")["Transaction_amount"].sum()
    apay3= pd.DataFrame(apay2).reset_index()

    fig_apay= px.bar(apay3, x="Transaction_type", y= "Transaction_amount", title= "PAYMENT TYPE and PAYMENT AMOUNT",
                    color_discrete_sequence=px.colors.sequential.Burg_r)
    fig_apay.update_layout(width=600, height=500)
    return st.plotly_chart(fig_apay)

# -----------------------------------------------------------------------------------------------------------------------------------------

def reg_state_all_RU(sel_year,state):
    year= int(sel_year)
    mus= Map_user[["States", "Years", "Districts", "RegisteredUser"]]
    mus1= mus.loc[(Map_user["States"]==state)&(Map_user["Years"]==year)]
    mus2= mus1.groupby("Districts")["RegisteredUser"].sum()
    mus3= pd.DataFrame(mus2).reset_index()

    fig_mus= px.bar(mus3, x= "Districts", y="RegisteredUser", title="DISTRICTS and REGISTERED USER",
                    color_discrete_sequence=px.colors.sequential.Cividis_r)
    fig_mus.update_layout(width= 600, height= 500)
    return st.plotly_chart(fig_mus)

# -----------------------------------------------------------------------------------------------------------------------------------------

def reg_state_all_TA(sel_year,state):
    year= int(sel_year)
    mts= Map_trans[["States", "Years","Districts", "Transaction_amount"]]
    mts1= mts.loc[(Map_trans["States"]==state)&(Map_trans["Years"]==year)]
    mts2= mts1.groupby("Districts")["Transaction_amount"].sum()
    mts3= pd.DataFrame(mts2).reset_index()

    fig_mts= px.bar(mts3, x= "Districts", y= "Transaction_amount", title= "DISTRICT and TRANSACTION AMOUNT",
                    color_discrete_sequence= px.colors.sequential.Darkmint_r)
    fig_mts.update_layout(width= 600, height=  500)
    return st.plotly_chart(fig_mts)

# -----------------------------------------------------------------------------------------------------------------------------------------

def ques1():
    brand= Aggre_user[["Brands","Transaction_count"]]
    brand1= brand.groupby("Brands")["Transaction_count"].sum().sort_values(ascending=False)
    brand2= pd.DataFrame(brand1).reset_index()

    fig_brands= px.pie(brand2, values= "Transaction_count", names= "Brands", color_discrete_sequence=px.colors.sequential.dense_r,
                       title= "Top Mobile Brands of Transaction_count")
    return st.plotly_chart(fig_brands)

# -----------------------------------------------------------------------------------------------------------------------------------------

def ques2():
    lt= Aggre_trans[["States", "Transaction_amount"]]
    lt1= lt.groupby("States")["Transaction_amount"].sum().sort_values(ascending= True)
    lt2= pd.DataFrame(lt1).reset_index().head(10)

    fig_lts= px.bar(lt2, x= "States", y= "Transaction_amount",title= "STATES WITH LOWEST TRANSACTION AMOUNT",
                    color_discrete_sequence= px.colors.sequential.Oranges_r)
    return st.plotly_chart(fig_lts)

# -----------------------------------------------------------------------------------------------------------------------------------------

def ques3():
    htd= Map_trans[["Districts", "Transaction_amount"]]
    htd1= htd.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=False)
    htd2= pd.DataFrame(htd1).head(10).reset_index()

    fig_htd= px.pie(htd2, values= "Transaction_amount", names= "Districts", title="TOP 10 DISTRICTS OF HIGHEST TRANSACTION AMOUNT",
                    color_discrete_sequence=px.colors.sequential.Emrld_r)
    return st.plotly_chart(fig_htd)

# -----------------------------------------------------------------------------------------------------------------------------------------

def ques4():
    htd= Map_trans[["Districts", "Transaction_amount"]]
    htd1= htd.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=True)
    htd2= pd.DataFrame(htd1).head(10).reset_index()

    fig_htd= px.pie(htd2, values= "Transaction_amount", names= "Districts", title="TOP 10 DISTRICTS OF LOWEST TRANSACTION AMOUNT",
                    color_discrete_sequence=px.colors.sequential.Greens_r)
    return st.plotly_chart(fig_htd)

# -----------------------------------------------------------------------------------------------------------------------------------------

def ques5():
    sa= Map_user[["States", "AppOpens"]]
    sa1= sa.groupby("States")["AppOpens"].sum().sort_values(ascending=False)
    sa2= pd.DataFrame(sa1).reset_index().head(10)

    fig_sa= px.bar(sa2, x= "States", y= "AppOpens", title="Top 10 States With AppOpens",
                color_discrete_sequence= px.colors.sequential.deep_r)
    return st.plotly_chart(fig_sa)

# -----------------------------------------------------------------------------------------------------------------------------------------

def ques6():
    sa= Map_user[["States", "AppOpens"]]
    sa1= sa.groupby("States")["AppOpens"].sum().sort_values(ascending=True)
    sa2= pd.DataFrame(sa1).reset_index().head(10)

    fig_sa= px.bar(sa2, x= "States", y= "AppOpens", title="Lowest 10 States With AppOpens",
                color_discrete_sequence= px.colors.sequential.dense_r)
    return st.plotly_chart(fig_sa)

# -----------------------------------------------------------------------------------------------------------------------------------------

def ques7():
    stc= Aggre_trans[["States", "Transaction_count"]]
    stc1= stc.groupby("States")["Transaction_count"].sum().sort_values(ascending=True)
    stc2= pd.DataFrame(stc1).reset_index()

    fig_stc= px.bar(stc2, x= "States", y= "Transaction_count", title= "STATES WITH LOWEST TRANSACTION COUNT",
                    color_discrete_sequence= px.colors.sequential.Jet_r)
    return st.plotly_chart(fig_stc)

# -----------------------------------------------------------------------------------------------------------------------------------------

def ques8():
    stc= Aggre_trans[["States", "Transaction_count"]]
    stc1= stc.groupby("States")["Transaction_count"].sum().sort_values(ascending=False)
    stc2= pd.DataFrame(stc1).reset_index()

    fig_stc= px.bar(stc2, x= "States", y= "Transaction_count", title= "STATES WITH HIGHEST TRANSACTION COUNT",
                    color_discrete_sequence= px.colors.sequential.Magenta_r)
    return st.plotly_chart(fig_stc)

# -----------------------------------------------------------------------------------------------------------------------------------------

def ques9():
    ht= Aggre_trans[["States", "Transaction_amount"]]
    ht1= ht.groupby("States")["Transaction_amount"].sum().sort_values(ascending= False)
    ht2= pd.DataFrame(ht1).reset_index().head(10)

    fig_lts= px.bar(ht2, x= "States", y= "Transaction_amount",title= "STATES WITH HIGHEST TRANSACTION AMOUNT",
                    color_discrete_sequence= px.colors.sequential.Oranges_r)
    return st.plotly_chart(fig_lts)

# -----------------------------------------------------------------------------------------------------------------------------------------

def ques10():
    dt= Map_trans[["Districts", "Transaction_amount"]]
    dt1= dt.groupby("Districts")["Transaction_amount"].sum().sort_values(ascending=True)
    dt2= pd.DataFrame(dt1).reset_index().head(50)

    fig_dt= px.bar(dt2, x= "Districts", y= "Transaction_amount", title= "DISTRICTS WITH LOWEST TRANSACTION AMOUNT",
                color_discrete_sequence= px.colors.sequential.Mint_r)
    return st.plotly_chart(fig_dt)

# -----------------------------------------------------------------------------------------------------------------------------------------

#                                                    streamlit part

st.set_page_config(layout= "wide")

st.title(":blue[PhonePe Data Visualization and Exploration]")
tab1, tab2, tab3 = st.tabs(["***HOME***","***EXPLORE DATA***","***TOP CHARTS***"])

# -----------------------------------------------------------------------------------------------------------------------------------------

with tab1:
    col1= st.columns(1)[0]

    with col1:
        image = Image.open("D:/PhonePe_Project/Phonepe_Logo.jpg")
        st.image(image)
        st.subheader(":green[INDIA'S BEST TRANSACTION APP]")
        st.markdown("PhonePe  is an Indian digital payments and financial technology company")
        st.write("****FEATURES****")
        st.write("   **=> Credit & Debit card linking**")
        st.write("   **=> Bank Balance check**")
        st.write("   **=> Money Storage**")
        st.write("   **=> PIN Authorization**")
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")


    col2= st.columns(1)[0]
    

    with col2:
        st.write("**=> Easy Transactions**")
        st.write("**=> One App For All Your Payments**")
        st.write("**=> Your Bank Account Is All You Need**")
        st.write("**=> Multiple Payment Modes**")
        st.write("**=> PhonePe Merchants**")
        st.write("**=> Multiple Ways To Pay**")
        st.write("    ==> 1.Direct Transfer & More")
        st.write("    ==> 2.QR Code")
        st.write("**=> Earn Great Rewards**")

    col3= st.columns(1)[0]

    with col3:
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.markdown(" ")
        st.write("**=> No Wallet Top-Up Required**")
        st.write("**=> Pay Directly From Any Bank To Any Bank A/C**")
        st.write("**=> Instantly & Free**")

# -----------------------------------------------------------------------------------------------------------------------------------------
              
with tab2:
    sel_year = st.selectbox("select the Year",("All", "2018", "2019", "2020", "2021", "2022", "2023"))
    if sel_year == "All" :
        col1, col2 = st.columns(2)
        with col1:
            animate_all_amount()
            payment_count()
            
        with col2:
            animate_all_count()
            payment_amount()

        state=st.selectbox("select the state",('Andaman And Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                                'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                                'Dadra & Nagar Haveli & Daman & Diu', 'Delhi', 'Goa',
                                                'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
                                                'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep',
                                                'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
                                                'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan',
                                                'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                                'Uttarakhand', 'West Bengal'))
        reg_all_states(state)

    else:
        col1,col2= st.columns(2)

        with col1:
            transaction_amount_year(sel_year)
            payment_count_year(sel_year)

        with col2:
            transaction_count_year(sel_year)
            payment_amount_year(sel_year)
            state= st.selectbox("select the state",('Andaman And Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                                'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                                'Dadra & Nagar Haveli & Daman & Diu', 'Delhi', 'Goa',
                                                'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
                                                'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep',
                                                'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
                                                'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan',
                                                'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                                'Uttarakhand', 'West Bengal'))
            reg_state_all_RU(sel_year,state)
            reg_state_all_TA(sel_year,state)

# -----------------------------------------------------------------------------------------------------------------------------------------

with tab3:
    ques= st.selectbox("select the question",('Top Brands Of Mobiles Used','States With Lowest Trasaction Amount',
                                  'Districts With Highest Transaction Amount','Top 10 Districts With Lowest Transaction Amount',
                                  'Top 10 States With AppOpens','Least 10 States With AppOpens','States With Lowest Trasaction Count',
                                 'States With Highest Trasaction Count','States With Highest Trasaction Amount',
                                 'Top 50 Districts With Lowest Transaction Amount'))
    if ques=="Top Brands Of Mobiles Used":
        ques1()

    elif ques=="States With Lowest Trasaction Amount":
        ques2()

    elif ques=="Districts With Highest Transaction Amount":
        ques3()

    elif ques=="Top 10 Districts With Lowest Transaction Amount":
        ques4()

    elif ques=="Top 10 States With AppOpens":
        ques5()

    elif ques=="Least 10 States With AppOpens":
        ques6()

    elif ques=="States With Lowest Trasaction Count":
        ques7()

    elif ques=="States With Highest Trasaction Count":
        ques8()

    elif ques=="States With Highest Trasaction Amount":
        ques9()

    elif ques=="Top 50 Districts With Lowest Transaction Amount":
        ques10()


# -----------------------------------------------------------------------------------------------------------------------------------------
