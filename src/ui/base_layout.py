import streamlit as st



def style_background_home():

    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(135deg, #052E1C 0%, #064E3B 50%, #065F46 100%) !important;
                }

                .stApp div[data-testid="stColumn"]{
                    background-color:#BBF7D0       !important;
                    padding:2.5rem !important;
                    border-radius: 5rem !important;
                    }
        </style>  

                """
            ,unsafe_allow_html=True)
    

def style_background_dashboard():

    st.markdown("""
        <style>

                .stApp {
                    background: linear-gradient(135deg, #052E1C 0%, #064E3B 50%, #065F46 100%) !important;
                }

        </style>  

                """
            ,unsafe_allow_html=True)
    

    

def style_base_layout():
# asdasd
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Goldman:wght@400;700&family=Michroma&family=Sekuya&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Michroma&display=swap');

                
         /* Hide Top Bar of streamlit */
                
            #MainMenu, footer, header {
                visibility: hidden;
            }
                
            .block-container {
                padding-top:1.5rem !important;    
            }

            h1 {
                font-family: 'Goldman', sans-serif !important;
                font-size: 4.0rem !important;
                line-height:1.1 1important;
                margin-bottom:0rem !important;
            }
                
            .dashboard-title {
            font-size: 2.2rem !important;
            }    

            h2 {
                font-family: 'Michroma', sans-serif !important;
                font-size: 2rem !important;
                line-height:0.9 !important;
                margin-bottom:0rem !important;
                color:#FFFFFF !important;
            }
                
            .home-title {
            color: #000000 !important;
            }
                
            h3, h4, p {
                font-family: 'Outfit', sans-serif;    
            }
                
            h3 {
                color: #FFFFFF !important;}
                

            button{
                border-radius: 1.5rem !important;
                background-color: #10B981 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="secondary"]{
                border-radius: 1.5rem !important;
                background-color: #10B981 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
                }

            button[kind="tertiary"]{
                border-radius: 1.5rem !important;
                background-color: #FEF3C7 !important;
                color: #92400E !important;
                border: 1px solid #F59E0B !important;
                }

            button:hover{
                transform :scale(1.05)}

                div[data-testid="stTextInput"] label {
            color: #FFFFFF !important;
            }

            # Override Streamlit's default input styles  
             
            div[data-testid="stTextInput"] input {
                background-color: #ECFDF5 !important;
                color: #052E1C !important;
                border-radius: 12px !important;
            }

            div[data-testid="stTextInput"] input::placeholder {
                color: #6B7280 !important;
            }
                
            
            div[data-testid="stAudioInput"] label {
            color: #FFFFFF !important;
            }
                
            
            div[data-testid="stAlert"] {
                background-color: #FEF3C7 !important;   
                border: 1px solid #F59E0B !important;
                border-radius: 10px !important;
            }
            div[data-testid="stAlert"] p {
            color: #92400E !important;  
            font-weight: 600 !important;
            }       


            div[data-testid="stAlert"] {
                background-color: #FEF3C7 !important;  
                border: 1px solid #F59E0B !important;
                border-radius: 10px !important;
            }
            div[data-testid="stAlert"] p {
                color: #92400E !important;   
                font-weight: 600 !important;
            }     
                
        </style>""",unsafe_allow_html=True)