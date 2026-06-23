from ollama import chat
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv()  # reads .env file

# 🔐 Add your HF token here
HF_TOKEN = os.getenv("HUGGING_FACE_API_KEY")

hf_client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    token=HF_TOKEN
)


def query_local(prompt):
    try:
        response = chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )
        return response["message"]["content"], "LOCAL"
    except Exception as e:
        print("Local failed:", e)
        return None, None


def query_hf(prompt):
    try:
        response = hf_client.chat_completion(
            prompt,
            max_tokens=300
        )
        return response.choices[0].message["content"], "HUGGINGFACE"
    except Exception as e:
        print("HF failed:", e)
        return None, None


def hybrid_query(prompt):
    # response, source = query_local(prompt)

    # if response:
    #     return response, source

    print("Falling back to Hugging Face...")
    response, source = query_hf(prompt)

    return response, source


if __name__ == "__main__":
    prompt = "Explain benefits of hybrid AI architecture."

    result, source = hybrid_query(prompt)

    print(f"\nResponse Source: {source}")
    print("\nModel Output:\n")
    print(result)