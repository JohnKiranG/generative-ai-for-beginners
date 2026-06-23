
How to generate Hugging Face token?
✅ Step‑by‑step (UI way)

Go to 👉 https://huggingface.co
Sign in to your Hugging Face account
Click your profile picture (top‑right)
Select Settings
In the left sidebar, click Access Tokens

Direct link: https://huggingface.co/settings/tokens


Click “New token”

✅ Fill token details

Name: any name (e.g. python-app-token)
Role / Scope:

✅ Read → enough for Inference API
Write → only if pushing models/datasets


Click Generate token

📌 Copy the token immediately — you won’t see it again.
====================================================================



Recursion
	Concept: State, return/stop condition, Recursive Relation
	Fibonacci
	Reverse a String
Stack
Queue
LinkedList
	Reverse a Linked List
Tree
	DFS
	BFS
	Mirror tree of not of binary tree.

====================================================================

1: Intro

====================================================================

Gen AI 
	> Gen AI (Generative AI) is AI that can create new content—like text, images, code, or audio—based on the data it has learned from.


Multiple options to learn LLM
	> Using GitHub codespace
	> Using local machine
	> Jupiter Notebook / Google collab

Tools required
	> Install Git
	> Install VSCode
	> Install python3
	> Install OpenJDK
	> Python dotenv -> Load Environmental variables

Choose IDE
	> Miniconda or
	> VS code with python support extension or
	> Jupiter Notebook in browser

Choose LLM Providers
	> Open API
	> Azure API
	> Hugging Face
	> Ollama
	> LLM studio
	> Notebook LLM

Setup Ollama
	> Install ollama software
	> Verify installation using: ollama --version
	> Pull model: ollama pull llama3
	> Test model: ollama run llama3
	> Verify API endpoint: http://localhost:11434

Project Setup
	> 	ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\Users\\grandhikiran\\Downloads\\projects\\generative-ai-for-beginners\\.venv\\share\\jupyter\\labextensions\\@jupyter-widgets\\jupyterlab-manager\\static\\vendors-node_modules_d3-color_src_color_js-node_modules_d3-format_src_defaultLocale_js-node_m-09b215.2643c43f22ad111f4f82.js'
	> HINT: This error might have occurred since this system does not have Windows Long Path support enabled. You can find information on how to enable this at https://pip.pypa.io/warnings/enable-long-paths

	> Done these to fix:
		git config --global core.longpaths true (or)
		Move project to a shorter path (e.g., C:\src\gaib).
	> Clone the project
	> Open in VScode
	> Open powershell
	> Setup virtual env
	> 	Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

History 
	> AI (1956) > Machine Learning (1997) > Deep Learning (2012) > Gen AI (2021)

How LLM works? 
	> Tokenizer (converts chunk of text to numbers) - Open API Tokenizer for demo
	> Predict output tokens  > model predicts next token and uses it for next token (expanding window pattern)
	> selection process, probability distribution

	> https://platform.openai.com/tokenizer -> Visualize how tokens are created for models


====================================================================

2. Exploring and comparing different LLMs

====================================================================


New words
	> LLM (Large Language Model)
	> SLM (Small Language Model)
	> Tokens (Chunk of words into numbers)
	> Embeddings (Converting into vectors)
	> Transformers (Encoding and decoding)
	> Input to LLM = Prompt
		> System Prompt => Constrainsts given generally hidden
		> User Prompt => Actual question
	> Output of LLM = Completion
	> AI Agent
		> Tools > Given tools like APIs to communciate with external world
	> Grounding (Providing specific context)
		> Retrieval augmented generation (RAG)
	> Semantic Search
	> Vector Database : Pinecone, Weaviate, QDrant, Milvus, and Chroma
	> LangChain -> Library to build RAG Systems
	> LlamaIndex -> Another Library for vector index Retrieval
	> Hallucinations
	

Imp links:
	> https://learn.microsoft.com/en-us/collections/zpy7c8zmq6ky0z?WT.mc_id=academic-105485-koreyst -> Website to learn
	> https://microsoftlearning.github.io/ai-apps/chat-playground/ -> Chat playground
	> https://microsoftlearning.github.io/ai-apps/model-coder/ -> Model coder playground to build apps


====================================================================

https://www.youtube.com/@vizuara - in-depth concept builder - my fav
https://www.youtube.com/@krishnaik06 - small concepts in bits and pieces
https://www.youtube.com/@codebasics - same
https://www.youtube.com/@LangChain
https://www.youtube.com/@3blue1brown - For mathematical concepts
https://www.youtube.com/@khanacademy - For concepts

https://academy.langchain.com/collections?page=2

https://academy.langchain.com/?_gl=1*1h4ub5z*_gcl_au*MjEwNTQ4MzYzOS4xNzczOTkzMTcw*_ga*NjI4MTI4ODgxLjE3NzM5OTMxNzA.*_ga_47WX3HKKY2*czE3NzQwMDE5NjckbzIkZzEkdDE3NzQwMDIwMTUkajEyJGwwJGgw

Session 8---
Retrieval
Generation
Hugging face exploration for LLM models
Interaction and Evaluation
Guardrails
Assignment Discussion

PDF > Chunking > Embedding > Storing in DB > Query vector and Embedding chunk vector > Cosine similarity > Retrieval (chunks) > Re ranking (using LLM) > Generation (prompt template - role, do & don'ts) > 
