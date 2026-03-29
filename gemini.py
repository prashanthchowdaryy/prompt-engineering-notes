# -----------------------------------------
# GEMINI RAG APP (STREAMLIT)
# -----------------------------------------
import streamlit as st
import google.generativeai as genai

# -----------------------------------------
# CONFIGURATION
# -----------------------------------------
st.set_page_config(
    page_title="Gemini RAG App",
    page_icon="🤖",
    layout="centered"
)

st.title("Prompt Engineering using Gemini")

# -----------------------------------------
# API KEY INPUT
# -----------------------------------------
api_key = st.text_input("🔑 Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)

    # Load model
    model=genai.GenerativeModel('models/gemini-3.1-flash-lite-preview')

    # -----------------------------------------
    # DUMMY RETRIEVER FUNCTION
    # -----------------------------------------
    def retriever_info(query):
        """
        Replace this with:
        - Vector DB (FAISS)
        - Pinecone
        - PDF search
        """

        if "india" in query.lower():
            return "India has one of the fastest growing economies in the world."
        elif "ai" in query.lower():
            return "Artificial Intelligence is transforming industries globally."
        elif "elon musk" in query.lower():
            return "Elon Musk is the CEO of Tesla and SpaceX."
        else:
            return "No relevant information found."

    # -----------------------------------------
    # RAG FUNCTION
    # -----------------------------------------
    def rag_query(query):

        # Step 1: Retrieve context
        retrieved_info = retriever_info(query)

        # Step 2: Create augmented prompt
        augmented_prompt = f"""
Use the following context to answer the question clearly.

Context:
{retrieved_info}

Question:
{query}

Answer:
"""

        # Step 3: Generate response
        response = model.generate_content(augmented_prompt)

        return response.text

    # -----------------------------------------
    # USER INPUT
    # -----------------------------------------
    user_query = st.text_input("Ask something...")

    if st.button("Generate Response") and user_query:
        with st.spinner("Thinking..."):
            answer = rag_query(user_query)

            st.markdown("### 🤖 AI Response")
            st.write(answer)

# -----------------------------------------
# FOOTER
# -----------------------------------------
st.markdown("---")
st.markdown("Built by Prashanth 🚀")
