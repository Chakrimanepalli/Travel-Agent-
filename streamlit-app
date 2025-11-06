import streamlit as st
import os
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from agent import travel_agent
import uuid

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Travel Agent Assistant",
    page_icon="✈️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1E88E5;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .user-message {
        background-color: #E3F2FD;
        margin-left: 20%;
    }
    .agent-message {
        background-color: #F5F5F5;
        margin-right: 20%;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'session_service' not in st.session_state:
    st.session_state.session_service = InMemorySessionService()
if 'runner' not in st.session_state:
    st.session_state.runner = Runner(
        agent=travel_agent,
        app_name="travel_agent_app",
        session_service=st.session_state.session_service
    )
if 'user_id' not in st.session_state:
    st.session_state.user_id = str(uuid.uuid4())
if 'session_id' not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

# Header
st.markdown('<h1 class="main-header">✈️ Travel Agent Assistant</h1>', unsafe_allow_html=True)
st.markdown(
    '<p class="sub-header">AI-powered hotel booking with MCP Toolbox & ADK</p>',
    unsafe_allow_html=True
)

# Sidebar
with st.sidebar:
    st.header("About")
    st.info(
        """
        This Travel Agent uses:
        - **Google ADK**
        - **MCP Toolbox**
        - **Gemini 2.0 Flash**
        """
    )
    
    st.header("Example Queries")
    example_queries = [
        "Find hotels in Basel",
        "Show me luxury hotels in Zurich",
        "Tell me about the Hilton Basel",
    ]
    
    for query in example_queries:
        if st.button(query, key=query):
            st.session_state.user_query = query

    if st.button("🗑️ Clear Conversation"):
        st.session_state.messages = []
        st.session_state.session_id = str(uuid.uuid4())
        st.rerun()

# Display chat
chat_container = st.container()
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(
                f'<div class="chat-message user-message"><strong>You:</strong> {message["content"]}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="chat-message agent-message"><strong>Agent:</strong> {message["content"]}</div>',
                unsafe_allow_html=True
            )

# Chat input
user_input = st.chat_input("Ask about hotels...")

if 'user_query' in st.session_state:
    user_input = st.session_state.user_query
    del st.session_state.user_query

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.spinner("🤔 Thinking..."):
        try:
            result = st.session_state.runner.run(
                user_id=st.session_state.user_id,
                session_id=st.session_state.session_id,
                new_message=user_input
            )
            
            agent_response = result.content if hasattr(result, 'content') else str(result)
            st.session_state.messages.append({"role": "agent", "content": agent_response})
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            st.error(error_msg)
            st.session_state.messages.append({"role": "agent", "content": error_msg})
    
    st.rerun()

st.markdown("---")
st.markdown("<p style='text-align: center;'>Built with Google ADK, MCP Toolbox & Streamlit</p>", unsafe_allow_html=True)