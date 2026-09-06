import ollama

response = ollama.chat(
    model="qwen3.5:4b",
    messages=[
        {
            "role": "user",
            "content": "弓道とは何ですか？短く答えてください。",
        }
    ],
)

print(response["message"]["content"])