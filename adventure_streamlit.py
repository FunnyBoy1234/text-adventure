import streamlit as st 
from adventure_llm_services import get_ollama_response

st.title("Text Adventure Game")

if "messages" not in st.session_state:
    st.session_state.messages = []
    game_start = get_ollama_response([])
    st.session_state.messages.append({"role": "assistant", "content": game_start})

if "refresh" not in st.session_state:
    st.session_state.refresh = 0

for message in st.session_state.messages:
    with st.chat_message(message['role']):
        st.markdown(message["content"])

prompt = st.chat_input("Say something")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Thinking..."):
        next_round = get_ollama_response(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": next_round})
        with st.chat_message("assistant"):
            st.markdown(next_round)

def refresh_game():
    st.session_state.pop("messages", None)

st.button("Restart Game", on_click=refresh_game)
