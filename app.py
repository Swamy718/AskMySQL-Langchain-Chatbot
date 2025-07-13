import streamlit as st
from urllib.parse import quote_plus
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq
import os
os.environ['GROQ-API_KEY']=st.secrets['GROQ_API_KEY']

st.set_page_config(page_title="MySQL Chatbot")
st.title("🛢️ AskMySQL – Natural‑Language MySQL Assistant")
st.text("An AI-powered chatbot built with LangChain that allows users to ask natural language questions and get accurate responses from a MySQL database.")
host=st.text_input("🔌Enter your Host",placeholder="localhost")
username=st.text_input(" 👤Enter the Username",placeholder="root")
raw_password=st.text_input("🔒 Enter the Password",type="password")
database=st.text_input(" 📂 Enter the Database Name",placeholder="student")
button=st.button("Clear Chat")
if button:
    st.session_state.pop("messages", None)
if "messages" not in st.session_state:
    st.session_state.messages=[]

if username and raw_password  and database:
    if "db" not in st.session_state:
        try:
            password=quote_plus(raw_password)
            db_uri = f"mysql+pymysql://{username}:{password}@{host}/{database}"
            st.session_state.db = SQLDatabase.from_uri(db_uri)
            st.success("✅ Connected to MySQL")
            
        except Exception as e:
            st.error(f"❌ Connection failed: {e}")
            st.stop()
else:
    st.info("ℹ️ Please enter all database credentials to connect.")

input=st.chat_input("Ask your question")
for role,message in st.session_state.messages:
    st.chat_message(role).write(message)
if input:
    st.chat_message("user").write(input)
    st.session_state.messages.append(("user",input))
    llm=ChatGroq(model="Llama3-8b-8192")
    toolkit=SQLDatabaseToolkit(db=st.session_state.db,llm=llm)
    agent=initialize_agent(
        tools=toolkit.get_tools(),
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        handle_parsing_errors=True,
        verbose=True
    )
    with st.spinner("Thinking…"):
     response = agent.run(input)
    st.chat_message("assistant").write(response)
    st.session_state.messages.append(("assistant",response))
    
