# Audio Transcription and Bullet Point Summarization 🎙️📝

This project demonstrates how to transcribe an audio file to text using OpenAI's Whisper model, then generate a concise bullet-point summary of the transcribed text using GPT-3.5 Turbo.

---

## Features ✨

- Transcribes audio files (e.g., MP3) to text using Whisper API.
- Summarizes the transcription into bullet points using GPT-3.5 Turbo.
- Modular and clean Python code with easy-to-follow functions.
- Suitable for podcasts, interviews, lectures, or any audio content summarization.

---

## Requirements 📋

- Python 3.7 or higher
- OpenAI Python SDK (`openai` package)

Install dependencies using pip:

```bash
pip install openai
````

---

## Setup ⚙️

1. **Get your OpenAI API key** 🔑:
   Sign up at [OpenAI](https://platform.openai.com/) and create an API key.

2. **Set your API key** 🔐:
   You can either:

   * Replace the placeholder `'your-api-key-here'` in the script file `transcribe_and_summarize.py`, or
   * Export it as an environment variable in your terminal:

   ```bash
   export OPENAI_API_KEY="your-api-key"
   ```

3. **Prepare your audio file** 🎧:
   Place the audio file you want to transcribe in the project directory or provide the full path.

---

## Usage ▶️

Run the script with:

```bash
python Audio2Text-WhisperSummarizer.py
```

The script will:

* Transcribe the audio file to text.
* Print the transcription.
* Generate and print a bullet point summary of the transcription.

---

## Notes 📝

* The Whisper API currently supports audio files, not real-time streaming.
* Audio file formats supported: mp3, wav, m4a, etc.
* Make sure your audio file is clear for better transcription accuracy.
* Modify `audio_file_path` in the script to change the input audio.

---

## License 📄

MIT License. Free to use, modify, and share.


---
