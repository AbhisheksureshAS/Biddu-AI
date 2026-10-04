from dotenv import load_dotenv
load_dotenv()

from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_groq import ChatGroq
from langgraph.checkpoint.memory import MemorySaver
from langchain.agents import create_agent
import streamlit as st


@st.cache_resource
def get_agent():
    llm = ChatGroq(
        model="openai/gpt-oss-120b",
        streaming=True
    )
    search = GoogleSerperAPIWrapper()
    agent = create_agent(
        model=llm,
        tools=[search.run],
        system_prompt="You are a helpful assistant that can answer questions using Google search. Use the tool to find information and provide accurate answers also make sure you use hinglish language and make sure u use words like biddu just like munna bhai mbbs movie",
        checkpointer=MemorySaver()
    )
    return agent
agent=get_agent()


st.title("🤖 AI CHAT BOT")
st.subheader('FASTer than CHATGPT')
query=st.chat_input('Ask Anything')
if 'chat_history' not in st.session_state:
    st.session_state['chat_history']=[]

for i in st.session_state['chat_history']:
    st.chat_message(i['role']).markdown(i['content'])

if query:
    st.session_state['chat_history'].append({'role':'user','content': query})
    st.chat_message('user').markdown(query)
    res=agent.invoke(
        {'messages':[{'role':'user','content':query}]},
        {'configurable':{'thread_id':'my_bot'}},
        stream_mode='messages'
    )
    ai_container=st.chat_message('assistant')
    with ai_container:
        space= st.empty()
        message=""
        for i in res:
            message += i[0].content
            space.write(message)
        st.session_state['chat_history'].append({'role':'assistant','content': message})