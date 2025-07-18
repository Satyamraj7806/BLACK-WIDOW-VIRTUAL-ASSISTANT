# 🕷️ BLACK WIDOW – Your Personal AI Voice Assistant

**BLACK WIDOW** is a smart, Jarvis-style AI voice assistant built with Python. It can listen, respond, play music, fetch news, and answer your questions using OpenAI's GPT. It mimics virtual assistants like Alexa or Google Assistant with custom wake words and speech interaction — all run locally on your machine.

---

## 🧠 Key Features

### 🎙️ Wake Word Detection
- Listens constantly for trigger phrases like:
  - `widow`, `black widow`, `jarvis`, `vision`, and more.
- Once triggered, it prompts for a command and listens again.

### 🤖 OpenAI GPT-Powered Q&A
- After hearing your command, it sends your query to **OpenAI GPT-3.5-Turbo**.
- Responds in natural language.
- Example: "Who is Albert Einstein?", "What is quantum computing?"

> 🗝️ **Note:** You must use your own OpenAI API key in the `.env` file.

### 📰 News Headlines
- Fetches latest headlines using **NewsAPI**.
- Trigger: Just say "news" or something related to headlines.

### 🎵 Music Player
- Say commands like `"play believer"` or `"play Shape of You"` and it will play the matching file from your local music library.
- Uses `pygame` to play `.mp3` files.

### 🌐 Web Browsing
- Open common websites like:
  - `"open Google"`, `"open YouTube"`, `"open Facebook"`, etc.
- Uses Python’s built-in `webbrowser` module.

### 🔊 Voice Responses
- Uses `gTTS` (Google Text-to-Speech) for human-like speech.
- Audio playback done via `pygame`.

---

🗣️ Example Commands
"jarvis" → (wake word)

"what is the capital of India?"

"open YouTube"

"play believer"

"news"

"exit" → (to stop the assistant)

