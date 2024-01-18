import streamlit as st
from langchain_instance import get_few_shot_db_chain, memory
from streamlit_chat import message
import streamlit_scrollable_textbox as stx

st.set_page_config(page_title = "Jarvis", layout="wide",menu_items = {'Report a bug': 'mailto:dehal.gagan2209@gmail.com'})

def setup_pages():
    session_state = st.session_state
    if not hasattr(session_state, "page"):
        session_state.page = "Welcome"                                            # Set default page to 'Welcome'

    if session_state.page == "Welcome":
        show_welcome_page()
    elif session_state.page == "Jarvis 2.0":
        show_jarvis_2_page()
        
        
        
def show_welcome_page():
    st.title("Welcome Gagan, Jarvis at your service.")                            # Add the necessary introductory information on the 
    st.subheader("These are the dataframes you're currently connected to: ")      # homepage
    st.subheader("LinkedIn Connections")
    st.subheader("LinkedIn Invitations")
    st.subheader("Instagram Posts Liked")
    st.subheader("Instagram Following")
    st.subheader("Instagram Advertisers")
    
    if st.button("Go to Chat"):
        st.session_state.page = "Jarvis 2.0"                                      # Add a button to redirect to the second page that 
                                                                                  # contains the chat layout.
        
        
        
        
def show_jarvis_2_page():
    header = st.container()
    header.title("Jarvis 2.0")
    header.write("""<div class='fixed-header'/>""", unsafe_allow_html=True)      # Create a fixed header that does not scroll away when
    st.markdown(                                                                 # the chat exceeds a single page.
    """
    <style>
        div[data-testid="stVerticalBlock"] div:has(div.fixed-header) {
            position: sticky;
            top: 2.1rem;
            background-color: black;
            z-index: 999;
            }
            .fixed-header {
                border-bottom: 1px solid black;
                }
    </style>
    """,
    unsafe_allow_html=True
    )
    question = st.chat_input("What would you like to know today Boss?")         # Insert a chat input for the user to ask questions.
    if question:
        with st.spinner("Thinking"):
            chain = get_few_shot_db_chain()                                         # Use the langchain code to process the question.
        #memory = chain.memory
            memory.append(question)
        
            response = chain.run(question)
            memory.append(response)
            for i in range(0, len(memory), 2):
                with st.chat_message("Gagan"):
                    st.write(memory[i])
                with st.chat_message("Jarvis", avatar = 'https://i0.wp.com/ioshacker.com/wp-content/uploads/2015/05/Jarvis-logo.jpg?w=500&ssl=1'):
                    st.write(memory[i+1])
        
            #st.markdown("---")
            

def set_background():
    st.markdown(f"""
            <style>
            .stApp {{background-image: url("https://vsthemes.org/uploads/nova/760430-1/bcc/c3fbcc59b131fa63a65095746533b683.webp"); 
                     background-attachment: fixed;
                     background-size: cover}}
         </style>
         """, unsafe_allow_html=True)
    
set_background()
setup_pages()

