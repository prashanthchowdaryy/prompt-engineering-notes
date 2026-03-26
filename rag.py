# -----------------------------------------
# RAG (Retrieval Augmented Generation) Demo
# -----------------------------------------

from openai import OpenAI

# Create client (Add your API key here)
client = OpenAI(api_key="API")

# -----------------------------------------
# Dummy Retriever Function
# -----------------------------------------
def retriever_info(query):
    """
    This function simulates retrieving information
    In real-world, this will be replaced with:
    - Vector DB (FAISS)
    - Pinecone
    - Database search
    """

    if "elon musk" in query.lower():
        return "Elon Musk is the CEO of Tesla and SpaceX."
    elif "ai" in query.lower():
        return "Artificial Intelligence is a technology that enables machines to mimic human intelligence."
    else:
        return "No relevant information found."


# -----------------------------------------
# RAG Query Function
# -----------------------------------------
def rag_query(query):

    # Step 1: Retrieve context
    retrieved_info = retriever_info(query)

    # Step 2: Create augmented prompt
    augmented_prompt = f"""
Use the following retrieved context to answer the question.

Context:
{retrieved_info}

Question:
{query}

Answer clearly:
"""

    # Step 3: Send to LLM
    response = client.chat.completions.create(
        model="gpt-4o-mini",   # fast + cheap
        messages=[
            {"role": "user", "content": augmented_prompt}
        ],
        max_tokens=150,
        temperature=0.7,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )

    # Step 4: Return response
    return response.choices[0].message.content.strip()


# -----------------------------------------
# Main Program
# -----------------------------------------
if __name__ == "__main__":

    print("=== RAG Prompt System ===")

    while True:
        query = input("\nAsk something (or type 'exit'): ")

        if query.lower() == "exit":
            print("Exiting...")
            break

        answer = rag_query(query)
        print("\nAI Response:\n", answer)