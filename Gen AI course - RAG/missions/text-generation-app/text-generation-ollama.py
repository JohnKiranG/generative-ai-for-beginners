import requests

url = "http://localhost:11434/api/generate"

payload = {
    "model": "llama3",
    "prompt": "Explain Agentic AI in 3 lines.",
    "stream": False
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    print("\nModel Response:\n")
    print(data["response"])
else:
    print("Error:", response.status_code, response.text)


# # 2nd version with streaming

# import requests
# import json

# url = "http://localhost:11434/api/generate"

# # Why Streaming = True? at both places
# # 1. In the payload: This tells the server to send the response in a streaming manner.
# # 2. In the requests.post call: This tells the client to handle the response as a stream.

# payload = {
#     "model": "llama3",
#     "prompt": "Explain Agentic AI in exactly 300 words.",
#     "stream": True
# }

# response = requests.post(url, json=payload, stream=True)

# if response.status_code == 200:
#     print("\nModel Response:\n")
#     for line in response.iter_lines():
#         if line:
#             data = json.loads(line.decode("utf-8"))
#             print(data.get("response", ""), end="")
# else:
#     print("Error:", response.status_code, response.text)