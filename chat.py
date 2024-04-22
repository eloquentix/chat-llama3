import gradio
from langchain_community.chat_models import ChatOllama
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

OLLAMA_PORT = 5151
LLM_MODEL = "llama3"

llm = ChatOllama(model=LLM_MODEL, base_url=f"http://localhost:{OLLAMA_PORT}")
prompt = ChatPromptTemplate.from_template("""
I need an answer of at least 100 characters structured as Markdown to the following question:
{question}
""")

chain = prompt | llm | StrOutputParser()


def process_question(user_question):
    return chain.invoke({"question": user_question})


iface = gradio.Interface(fn=process_question,
                         inputs=gradio.Textbox(lines=2, placeholder="What's the best AI library out there?"),
                         outputs=gradio.Textbox(),
                         title="Llama3 (or whatever Ollama can serve)",
                         allow_flagging="never",
                         description="")

# Launch the interface
iface.launch(share=False)
