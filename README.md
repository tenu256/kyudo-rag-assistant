# Kyudo RAG Assistant

Android向けの弓道RAGチャットボットです。

弓道に関する資料を検索し、
ローカルLLMを利用して根拠付きの回答を生成します。

## Planned Architecture

### Android
- Kotlin
- Jetpack Compose
- Material 3

### Backend
- Python
- FastAPI
- ChromaDB

### AI
- Ollama
- Local LLM
- Local Embedding

## Project Structure

```text
kyudo-rag-assistant/
├── android/
├── backend/
├── docs/
├── README.md
├── AGENTS.md
└── .gitignore