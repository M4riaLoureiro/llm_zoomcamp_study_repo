import streamlit as st
from rag import rag
#from database import save_conversation, save_feedback
import time

# Course options
courses = ['machine-learning-zoomcamp', 'data-engineering-zoomcamp', 'mlops-zoomcamp']

def main():
    st.title("RAG Function Invocation")

    # Course selection
    course = st.selectbox("Select Course", courses)

    user_input = st.text_input("Enter your question:")

    if st.button("Ask"):
        with st.spinner('Processing...'):
            output = rag(user_input, course)
            st.success("Completed!")
            st.write(output)

            """ conversation_id = save_conversation(user_input, output, course)
            
            if st.button("+1"):
                save_feedback(conversation_id, 1)
            if st.button("-1"):
                save_feedback(conversation_id, -1)
            """

if __name__ == "__main__":
    main()