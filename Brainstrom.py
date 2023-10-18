import streamlit as st
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: rgb(228, 241, 247);
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

if 'var' not in st.session_state:
    st.session_state.var = {1:"aggressive",2:"aggressive",3:"aggressive",4:"aggressive",5:"aggressive",6:"aggressive",7:"aggressive" }

# Ideal matrix
ideal = pd.DataFrame([
    [0, 0, 0, 10, 10],
    [2, 2, 12, 2, 2],
    [2, 2, 6, 5, 5]
])
aggressive =pd.DataFrame([
    [10, 0, 0, 10, 10],
    [4, 10, 12, 8, 2],
    [2, 2, 10, 7, 5]
])

coservative= pd.DataFrame([
    [9, 5, 2, 10, 10],
    [2, 2, 19, 2, 2],
    [2, 2, 6, 5, 5]

])

# Matrices created by your team
team_matrices = {
    "team1":pd.DataFrame([
        [10, 10, 10, 10, 10],
        [10, 10, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],columns=['Watersports', 'Snowsports', 'Lawnsports', 'Fightsports', 'IndoorSports'], index=['A', 'B', 'C']),

    "team2":pd.DataFrame([
        [-1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],columns=['Watersports', 'Snowsports', 'Lawnsports', 'Fightsports', 'IndoorSports'], index=['AadASAs', 'BdADSDA', 'Cdasdasd']),

    "team3":pd.DataFrame([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],columns=['Watersports', 'Snowsports', 'Lawnsports', 'Fightsports', 'IndoorSports'], index=['A', 'B', 'C']),


    "team4":pd.DataFrame([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],columns=['Watersports', 'Snowsports', 'Lawnsports', 'Fightsports', 'IndoorSports'], index=['A', 'B', 'C']),

    "team5":pd.DataFrame([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],columns=['Watersports', 'Snowsports', 'Lawnsports', 'Fightsports', 'IndoorSports'], index=['A', 'B', 'C']),

    "team6":pd.DataFrame([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],columns=['Watersports', 'Snowsports', 'Lawnsports', 'Fightsports', 'IndoorSports'], index=['A', 'B', 'C']),

    "team7":pd.DataFrame([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ],columns=['Watersports', 'Snowsports', 'Lawnsports', 'Fightsports', 'IndoorSports'], index=['A', 'B', 'C']),
}
# st.write(team_matrices['team1'])

def calculate_similarity(ideal_matrix, team_matrix):
    ideal_matrix=ideal_matrix.to_numpy()
    team_matrix=team_matrix.to_numpy()
    similarity = cosine_similarity(ideal_matrix.flatten().reshape(1, -1), team_matrix.flatten().reshape(1, -1))
    return similarity[0][0]

def sumOfMatrix(mat):
        mat=mat.to_numpy()
        Sum = 0
    
        # Traverse in each row
        for i in range(3):
            # Traverse in column of that row
            for j in range(5):
    
                # Add element in variable sum
                Sum += mat[i][j]
    
        
        return Sum


if 'edited_matrices' not in st.session_state:
    st.session_state.edited_matrices = {team: matrix.copy() for team, matrix in team_matrices.items()}

# st.set_page_config(page_title="Client Experience 2.0", layout="wide", initial_sidebar_state="auto")
st.markdown("""
 <style>
 .block-container {
 padding-top: 1rem;
 padding-bottom: 0rem;

 padding-right: 5rem;
 }
 </style>
 """, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center;'>CE 2.0</h1>", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; font-size: 18px;'>Client Experience 2.0: This team has big potential led by one and only Nitish Bhai, invest today</p>", unsafe_allow_html=True)

# if st.session_state.selected_team != 8:
#     st.header("**Case Study:**")
#     st.write('''Client Experience or Customer Experience it does not matter we are MBA graduates, sab kuch ek hi hai. humko bus pagal banana hai. 
#                 Give us anything we will sell it. Pagal banane is our expertise. But today we will learn something important and useful, something which
#                 a B.Tech graduate would like to learn.
#                 ''')

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #6C92B5;
    width:290px;
    height:50px;

}
</style>""", unsafe_allow_html=True)


st.sidebar.markdown("<div style='margin-top: -20px;'></div>", unsafe_allow_html=True)
st.sidebar.image("logoha.png", width=200 )
home = st.sidebar.button("**Home 🏠**")
result = st.sidebar.button("**Results Summary**")
st.sidebar.header("Choose Team:")
team1_button = st.sidebar.button("**Team1**")
team2_button = st.sidebar.button("**Team2**")
team3_button = st.sidebar.button("**Team3**")
team4_button = st.sidebar.button("**Team4**")
team5_button = st.sidebar.button("**Team5**")
team6_button = st.sidebar.button("**Team6**")
team7_button = st.sidebar.button("**Team7**")


if 'selected_team' not in st.session_state:
        st.session_state.selected_team = 0


    
        
    
if home:
    st.session_state.selected_team=0
elif team1_button:
    st.session_state.selected_team = 1
    
elif team2_button:
    st.session_state.selected_team = 2
elif team3_button:
    st.session_state.selected_team = 3
elif team4_button:
    st.session_state.selected_team =4
elif team5_button:
    st.session_state.selected_team =5
elif team6_button:
    st.session_state.selected_team =6
elif team7_button:
    st.session_state.selected_team =7
elif result:
    st.session_state.selected_team =8

if st.session_state.selected_team != 8:
    st.header("**Case Study🔍:**")
    st.write('''Client Experience or Customer Experience it does not matter we are MBA graduates, sab kuch ek hi hai. humko bus pagal banana hai. 
                Give us anything we will sell it. Pagal banane is our expertise. But today we will learn something important and useful, something which
                a B.Tech graduate would like to learn.
                ''')




# If a team button is clicked, set the selected team
col1,col3=st.columns([2.5,1])

with col1:
    

    
    if st.session_state.selected_team==0:
        st.header("Instructions📝:")
        st.write("**Instruction 1**")
        st.write("**Instruction 2**")
        st.write("**Instruction 3**")
        st.write("**Instruction 4**")
        st.write("**Instruction 5**")


    if st.session_state.selected_team==1:

        
        st.header("Innovation Matrix💡:")
        st.write("Allocate your total budget according to the below matrix:")        
        st.write("**Team 1**")
        # df = pd.DataFrame(df, columns=['A', "B",'C','D','E'],index=['A','B','C','D','E'])
        
        edited_df = st.data_editor(st.session_state.edited_matrices["team1"],key=1)
        # df = edited_df.to_numpy()
        st.session_state.edited_matrices["team1"]=edited_df
        st.subheader("Your Balance is " + str(100-sumOfMatrix(edited_df)))



    if st.session_state.selected_team==2:
    
        st.header("Innovation Matrix💡:")
        st.write("Allocate your total budget according to the below matrix:")  
        st.write("**Team 2**")
        # df1 = pd.DataFrame(df, columns=['A', "B",'C','D','E'],index=['A','B','C','D','E'])
        
        edited_df = st.data_editor(st.session_state.edited_matrices["team2"],key=2)
        # df = edited_df.to_numpy()
        st.session_state.edited_matrices["team2"]=edited_df
        st.subheader("Your Balance is " + str(100-sumOfMatrix(edited_df)))




    if st.session_state.selected_team==3:
        
        st.header("Innovation Matrix💡:")
        st.write("Allocate your total budget according to the below matrix:")         
        st.write("**Team 3**")
        
        edited_df = st.data_editor(st.session_state.edited_matrices["team3"],key=3)
       
        st.session_state.edited_matrices["team3"]=edited_df
        st.subheader("Your Balance is " + str(100-sumOfMatrix(edited_df)))



        
    if st.session_state.selected_team==4:

        st.header("Innovation Matrix💡:")
        st.write("Allocate your total budget according to the below matrix:")     
        st.write("**Team 4**")
        
        edited_df = st.data_editor(st.session_state.edited_matrices["team4"],key=4)
        
        st.session_state.edited_matrices["team4"]=edited_df

        st.subheader("Your Balance is " + str(100-sumOfMatrix(edited_df)))


    
    if st.session_state.selected_team==5:
        st.header("Innovation Matrix💡:")
        st.write("Allocate your total budget according to the below matrix:")     
        st.write("**Team 5**")
       
        
        edited_df = st.data_editor(st.session_state.edited_matrices["team5"],key=5)
        
        st.session_state.edited_matrices["team5"]=edited_df

        st.subheader("Your Balance is " + str(100-sumOfMatrix(edited_df)))


    if st.session_state.selected_team==6:
        st.header("Innovation Matrix💡:")
        st.write("Allocate your total budget according to the below matrix:")     
        st.write("**Team 6**")
       
        edited_df = st.data_editor(st.session_state.edited_matrices["team6"],key=6)
       
        st.session_state.edited_matrices["team6"]=edited_df

        st.subheader("Your Balance is " + str(100-sumOfMatrix(edited_df)))


    if st.session_state.selected_team==7:
        st.header("Innovation Matrix💡:")
        st.write("Allocate your total budget according to the below matrix:")     
        st.write("**Team 7**")
        
        edited_df = st.data_editor(st.session_state.edited_matrices["team7"],key=7)
       
        st.session_state.edited_matrices["team7"]=edited_df

        st.subheader("Your Balance is " + str(100-sumOfMatrix(edited_df)))



       
with col3: 
    if st.session_state.selected_team!=0 and st.session_state.selected_team!=8:
    
        if int(100-sumOfMatrix(edited_df)) > 0:
                aggre = calculate_similarity(aggressive, edited_df)
                ideal=calculate_similarity(ideal, edited_df)
                conser=calculate_similarity(coservative, edited_df)
                if aggre > ideal and aggre > conser:
                        team_no=st.session_state.selected_team
                        st.session_state.var[team_no] = "aggre"
                        # ls.append(team_no)
                        # ls.append("234")


                    
                    
                        fig = go.Figure(go.Indicator(
                            mode="gauge+number",
                            value=aggre * 100,
                            title={'text': "<b>Maverick</b>"},
                            gauge={
                                'axis': {'range': [0, 100]},
                                'bar': {'color': "red"},
                                'steps': [
                                    {'range': [0, 50], 'color': "lightgray"},
                                    {'range': [50, 100], 'color': "lightgray"}
                                ]
                            }
                        ))
                        fig.update_layout(
                        width=330,  # Set your desired width in pixels
                        height=550,  # Set your desired height in pixels
                        margin=dict(t=0)
                    )
                        st.plotly_chart(fig)

                if ideal > conser and ideal > aggre:
                        team_no=st.session_state.selected_team
                        st.session_state.var[team_no] = "Balanced"
                    
                    
                        fig = go.Figure(go.Indicator(
                            mode="gauge+number",
                            value=ideal * 100,
                            title={'text': "<b>Prudent</b>"},
                            gauge={
                                'axis': {'range': [0, 100]},
                                'bar': {'color': "blue"},
                                'steps': [
                                    {'range': [0, 50], 'color': "lightgray"},
                                    {'range': [50, 100], 'color': "lightgray"}
                                ]
                            }
                        ))
                        fig.update_layout(
                        width=330,  # Set your desired width in pixels
                        height=550,  # Set your desired height in pixels
                        margin=dict(t=0)

                    )
                        st.plotly_chart(fig)

                if conser > ideal and conser > aggre:
                        team_no=st.session_state.selected_team
                        st.session_state.var[team_no] = "coservative"
                    
                        
                        fig = go.Figure(go.Indicator(
                            mode="gauge+number",
                            value=conser * 100,
                            title={'text': "<b>Old School</b>"},
                            gauge={
                                'axis': {'range': [0, 100]},
                                'bar': {'color': "yellow"},
                                'steps': [
                                    {'range': [0, 50], 'color': "lightgray"},
                                    {'range': [50, 100], 'color': "lightgray"}
                                ]
                            }
                        ))
                        fig.update_layout(
                        width=330,  # Set your desired width in pixels
                        height=550,  # Set your desired height in pixels
                        margin=dict(t=0)

                    )
                        st.plotly_chart(fig)

        else:
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.write(" ")
            st.warning('**Ooops, It looks like you have crossed your allocated budget limit**', icon="⚠️")
            


footer="""<style>
a:link , a:visited{
color: white;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
color: white;
text-align: right;
right-margin: 5;
}
</style>
<div class="footer">
<p>Powered By <a style=' text-align: right;right-margin:10;' href="https://healtharkinsights.com/analytics-demo/" target="_blank">HealthArk Analytics©</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)


if st.session_state.selected_team==8:
        
        st.header("Result Summary📖")

       
        categories = {
            "Maverick": {
                "emoji": "🎰",
                "text": "You believe in transformation",
            },
            "Prudent": {
                "emoji": "⚖️",
                "text": "Perfectly balanced",
            },
            "Old School": {
                "emoji": "⚓",
                "text": "Safe and secure, the old way",
            },
        }

        col1, col2 = st.columns(2)

        for category, info in categories.items():
            with col1:
                st.write(f"{info['emoji']} {category}")
                
            with col2:
                st.write(info['text'])

        st.header("Team Score Reports📑")
        # st.write(score)
        # st.write(st.session_state.var)



        # aggre > ideal and aggre > conser:
        st.markdown("<h3 style='font-size:24px;'>Team1</h3>",unsafe_allow_html=True)
        
        temp1=st.session_state.var[1]
        if temp1=="aggre":
            st.write("You are someone who is unconventional and independent in your approach, often taking risks that others might avoid: ")
            st.subheader(round(calculate_similarity(aggressive,st.session_state.edited_matrices["team1"])*100,2))

        if temp1=="Balanced":
            st.write("You are someone who conveys a sense of enthusiasm for risk while also exercising conventional approach when required")
            st.subheader(round(calculate_similarity(ideal,st.session_state.edited_matrices["team1"])*100,2))
        if temp1=="coservative":
            st.write("You are someone who adheres to traditional and established business practices rather than embracing modern or innovative approaches")
            st.subheader(round(calculate_similarity(coservative,st.session_state.edited_matrices["team1"])*100,2))
        st.write("")
        st.write("")
        st.write("")



        st.markdown("<h3 style='font-size:24px;'>Team2</h3>",unsafe_allow_html=True)
        
        temp2=st.session_state.var[2]
        if temp2=="aggre":
            st.write("You are someone who is unconventional and independent in your approach, often taking risks that others might avoid: ")
            st.subheader(round(calculate_similarity(aggressive,st.session_state.edited_matrices["team2"])*100,2))

        if temp2=="Balanced":
            st.write("You are someone who conveys a sense of enthusiasm for risk while also exercising conventional approach when required")
            st.subheader(round(calculate_similarity(ideal,st.session_state.edited_matrices["team2"])*100,2))
        if temp2=="coservative":
            st.write("You are someone who adheres to traditional and established business practices rather than embracing modern or innovative approaches")
            st.subheader(round(calculate_similarity(coservative,st.session_state.edited_matrices["team2"])*100,2))

        st.write("")
        st.write("")
        st.write("")



        st.markdown("<h3 style='font-size:24px;'>Team3</h3>",unsafe_allow_html=True)
        
        temp=st.session_state.var[3]
        if temp=="aggre":
            st.write("You are someone who is unconventional and independent in your approach, often taking risks that others might avoid: ")
            st.subheader(round(calculate_similarity(aggressive,st.session_state.edited_matrices["team3"])*100,2))

        if temp=="Balanced":
            st.write("You are someone who conveys a sense of enthusiasm for risk while also exercising conventional approach when required")
            st.subheader(round(calculate_similarity(ideal,st.session_state.edited_matrices["team3"])*100,2))
        if temp=="coservative":
            st.write("You are someone who adheres to traditional and established business practices rather than embracing modern or innovative approaches")
            st.subheader(round(calculate_similarity(coservative,st.session_state.edited_matrices["team3"])*100,2))

        st.write("")
        st.write("")
        st.write("")

        st.markdown("<h3 style='font-size:24px;'>Team4</h3>",unsafe_allow_html=True)
        
        temp=st.session_state.var[4]
        if temp=="aggre":
            st.write("You are someone who is unconventional and independent in your approach, often taking risks that others might avoid: ")
            st.subheader(round(calculate_similarity(aggressive,st.session_state.edited_matrices["team4"])*100,2))

        if temp=="Balanced":
            st.write("You are someone who conveys a sense of enthusiasm for risk while also exercising conventional approach when required")
            st.subheader(round(calculate_similarity(ideal,st.session_state.edited_matrices["team4"])*100,2))
        if temp=="coservative":
            st.write("You are someone who adheres to traditional and established business practices rather than embracing modern or innovative approaches")
            st.subheader(round(calculate_similarity(coservative,st.session_state.edited_matrices["team4"])*100,2))
        
        st.write("")
        st.write("")
        

        # st.markdown("<h3 style='font-size:24px;'>Team5</h3>",unsafe_allow_html=True)
        
        # temp=st.session_state.var[5]
        # if temp=="aggre":
        #     st.write("You are someone who is unconventional and independent in your approach, often taking risks that others might avoid: ")
        #     st.subheader(round(calculate_similarity(aggressive,st.session_state.edited_matrices["team5"])*100,2))

        # if temp=="Balanced":
        #     st.write("You are someone who conveys a sense of enthusiasm for risk while also exercising conventional approach when required")
        #     st.subheader(round(calculate_similarity(ideal,st.session_state.edited_matrices["team5"])*100,2))
        # if temp=="coservative":
        #     st.write("You are someone who adheres to traditional and established business practices rather than embracing modern or innovative approaches")
        #     st.subheader(round(calculate_similarity(coservative,st.session_state.edited_matrices["team5"])*100,2))

        # st.markdown("<h3 style='font-size:24px;'>Team6</h3>",unsafe_allow_html=True)
        
        # temp=st.session_state.var[6]
        # if temp=="aggre":
        #     st.write("You are someone who is unconventional and independent in your approach, often taking risks that others might avoid: ")
        #     st.subheader(round(calculate_similarity(aggressive,st.session_state.edited_matrices["team6"])*100,2))

        # if temp=="Balanced":
        #     st.write("You are someone who conveys a sense of enthusiasm for risk while also exercising conventional approach when required")
        #     st.subheader(round(calculate_similarity(ideal,st.session_state.edited_matrices["team6"])*100,2))
        # if temp=="coservative":
        #     st.write("You are someone who adheres to traditional and established business practices rather than embracing modern or innovative approaches")
        #     st.subheader(round(calculate_similarity(coservative,st.session_state.edited_matrices["team6"])*100,2))

        # st.markdown("<h3 style='font-size:24px;'>Team7</h3>",unsafe_allow_html=True)
        
        # temp=st.session_state.var[7]
        # if temp=="aggre":
        #     st.write("You are someone who is unconventional and independent in your approach, often taking risks that others might avoid: ")
        #     st.subheader(round(calculate_similarity(aggressive,st.session_state.edited_matrices["team7"])*100,2))

        # if temp=="Balanced":
        #     st.write("You are someone who conveys a sense of enthusiasm for risk while also exercising conventional approach when required")
        #     st.subheader(round(calculate_similarity(ideal,st.session_state.edited_matrices["team7"])*100,2))
        # if temp=="coservative":
        #     st.write("You are someone who adheres to traditional and established business practices rather than embracing modern or innovative approaches")
        #     st.subheader(round(calculate_similarity(coservative,st.session_state.edited_matrices["team7"])*100,2))
        
