\# Kyudo RAG Assistant



\## Project Goal



Build an Android application that answers questions about Japanese Kyudo

using Retrieval-Augmented Generation.



The final product should be suitable for demonstrating in software engineering

job interviews.



\## Architecture



The project uses a client-server architecture.



\### Android



Location:



android/



Technology:



\- Kotlin

\- Jetpack Compose

\- Material 3

\- Retrofit

\- Kotlin Coroutines



Responsibilities:



\- Chat UI

\- User input

\- Streaming response display

\- Conversation history

\- Source citation display

\- Settings



Do not implement RAG logic in Android.



\### Backend



Location:



backend/



Technology:



\- Python

\- FastAPI

\- Ollama

\- ChromaDB



Responsibilities:



\- Document ingestion

\- Chunking

\- Embedding generation

\- Vector retrieval

\- Prompt construction

\- LLM inference

\- Source citation



\## LLM Requirements



LLM inference must use Ollama locally.



Do not use:



\- OpenAI API

\- Gemini API

\- Claude API

\- other hosted LLM APIs



External APIs must not be required for normal inference.



\## RAG



The RAG pipeline must remain understandable.



Avoid hiding the entire implementation behind frameworks such as LangChain.



Separate:



\- document loader

\- chunker

\- embeddings

\- vector store

\- retriever

\- prompt builder

\- LLM client



\## Android UI



The UI should have a modern AI chat interface inspired by applications such

as ChatGPT, while keeping an original design.



Important elements:



\- full-screen conversation view

\- bottom message composer

\- rounded input field

\- streaming response rendering

\- Markdown support

\- light and dark themes

\- conversation history

\- source cards

\- loading states



\## Code Quality



Use:



\- clear module separation

\- meaningful naming

\- type hints in Python

\- Kotlin idioms

\- tests for important RAG components



Avoid overly large files.



\## Security



Never commit:



\- private PDF files

\- copyrighted Kyudo books

\- .env files

\- Chroma database files

\- model files

