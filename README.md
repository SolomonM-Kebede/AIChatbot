# AIChatbot
After I have downloaded llama3.1 and deepSeek-r1 locally, I used these LLMs to create a local chatbot and integrated them(since they are trained). I used Ollama to download those models(you can even run them directly from your terminal). I also used Langchain and Gradio  to improve my UI experience.
# Which LLM?
I am using, in this case, the llama3.1 model, but anyone can change that only by changing the model name after downloading the necessary LLM.

# UI experience

I am using Gradio, which provides local and public host addresses to use the chatbot with a better UI. 

# Which other option to permanent UI for public use 

It is possible to use the Hagging face platform with LLM API so that anyone can use your chatbot without having access to your LLM. 


# How to Run(without using Hagging face directly with your local LLM)
	1.	Make sure Ollama is running locally.(with llama3.1, deepseek-r1 or any other prefered LLM)
	2.	Clone the repo:
        git clone https://github.com/SolomonM-Kebede/AIChatbot.git
        cd AIChatbot
    3. Install requirments 
        pip install -r requirments.txt
    4. run the app.py