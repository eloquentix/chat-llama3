## Minimal LangChain llama3 chat

Python 3.8+
Ollama latest

Pull ollama models
```commandline
ollama pull llama3
etc...
```

Start Ollama model server (port is hardcoded in chat.py. change both if you need)
```commandline
OLLAMA_HOST=127.0.0.1:5151 ollama serve 
```

Start chat server
```commandline
python -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
python chat.py
```

Notes:
Needless to say you can change `LLM_MODEL = "llama3"` in chat.py to whatever supported by Ollama (https://ollama.com/library) and it should still work
