# Required Ollama Python SDK Library
# To install: python -m pip install ollama
# -m pip allows you to run the pip module as a script, which is a common way to install Python packages.
# why -m pip? It ensures that you are installing the package for the correct Python version, especially if you have multiple versions of Python installed on your system. Using -m pip helps avoid issues with permissions and ensures that the package is installed in the appropriate environment.

# Without streaming
# from ollama import chat

# response = chat(
#     model='llama3',
#     messages=[
#         {"role": "user", "content": "Explain why local LLMs improve data privacy in 2 lines"}
#     ]
# )

# print("\nModel Response:\n")
# print(response['message']['content'])

# Using streaming to get the response in chunks as it's generated
from ollama import chat

stream = chat(
    model='llama3',
    messages=[
        {'role': 'user', 'content': 'Explain Agentic AI in 300 words. Please ensure not more than that.'}
    ],
    stream=True
)

print("\nModel Response:\n")

for chunk in stream:
    print(chunk['message']['content'], end='')