import streamlit as st


def header_home():

    logo_url = "https://raw.githubusercontent.com/SyedMaaz786/ML_Models/main/snapclass.png"
    
    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; justify-content:center; margin-bottom:30px; margin-top:30px">
            <img src='{logo_url}' style='height:140px;' />
            <h1 style='text-align:center; color:#FFFFFF'>SNAP<br/>
            <span style="margin-left:40px;">CLASS</span>
            </h1>
        </div>   
                
                """, unsafe_allow_html=True)


def header_dashboard():

    logo_url = "https://raw.githubusercontent.com/SyedMaaz786/ML_Models/main/snapclass.png"

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; gap:10px">
            <img src='{logo_url}' style='height:85px;' />
            <h1 class="dashboard-title" style='text-align:left; color:#FFFFFF'>
                 SNAP<br/>CLASS
            </h1>
        </div>   
                
                """, unsafe_allow_html=True)