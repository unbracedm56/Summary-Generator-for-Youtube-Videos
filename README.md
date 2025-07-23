# Summary Generator for Youtube Videos

A simple Streamlit app that summarizes the content of any YouTube video using **LangChain** and **Google's Gemini model**.

## Features

- Accepts any YouTube URL as input
- Uses `YoutubeLoader` from `langchain_community` to extract video transcript
- Splits text into chunks using `RecursiveCharacterTextSplitter`
- Crafts structured prompt via `PromptTemplate`
- Powered by Gemini (via `langchain_google_genai`) to generate concise, human-readable summaries

## 🛠️ Tech Stack

- `Streamlit` — frontend interface
- `LangChain` — orchestration of LLM workflow
- `GoogleGenerativeAI` — LLM integration (Gemini 2.0 Flash)

## 📂 Project Structure
```bash
├── app.py     # Streamlit UI
├── main.py    # LangChain logic: loading, splitting, prompting, summarizing
```

## Setup

1. Set your Google API Key in the environment:
   ```bash
   export GOOGLE_API_KEY="your-api-key"
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```
