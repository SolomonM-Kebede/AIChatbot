
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import gradio as gr

template = """
Answer the question below.
Here is the conversation history: {chat}
Question: {question}
Answer:
"""

model = OllamaLLM(model="llama3.1")

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# # Initialize chat history outside the function
chat_history = ""

def chat_with_bot(user_input):
    global chat_history
    # Call the model
    result = chain.invoke({"chat": chat_history, "question": user_input})

    # Update the chat history
    chat_history += f"\nuser: {user_input}\nAI: {result}"

    return chat_history.strip()

chat_interface = gr.Interface(fn=chat_with_bot, inputs="text", outputs="text", title="Welcome to the AI Chatbot", description= "Chat with local DeepSeek R1 Model", )

chat_interface.launch(favicon_path="simple chat bot favicon png.png", share=True)
# if __name__ == "__main__":
#     chat_with_bot()