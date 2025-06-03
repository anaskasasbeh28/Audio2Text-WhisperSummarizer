# transcribe_and_summarize.py

import os
import openai

# ========================
# Configuration and Setup
# ========================

# Set your OpenAI API key here or set it as an environment variable outside the script
OPENAI_API_KEY = 'your-api-key-here'  # <-- Replace this with your actual API key or keep it empty to use environment variable

if OPENAI_API_KEY:
    os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY

openai.api_key = os.getenv('OPENAI_API_KEY')

if not openai.api_key:
    raise ValueError("OpenAI API key not found. Please set it in the script or as an environment variable.")


# ========================
# Function: Transcribe Audio
# ========================

def transcribe_audio(file_path: str) -> str:
    """
    Transcribe an audio file to text using OpenAI's Whisper model.

    Args:
        file_path (str): Path to the audio file (e.g., .mp3).

    Returns:
        str: Transcribed text from audio.
    """
    with open(file_path, 'rb') as audio_file:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )
    return transcript.text


# ========================
# Function: Summarize Text in Bullet Points
# ========================

def summarize_text_bullet_points(text: str) -> str:
    """
    Generate a bullet point summary of the given text using GPT-3.5-turbo.

    Args:
        text (str): Input text to summarize.

    Returns:
        str: Bullet point summary as a string.
    """
    system_message = {
        "role": "system",
        "content": "You are good at creating bullet point summaries and have knowledge of Warren Buffett."
    }
    user_message = {
        "role": "user",
        "content": f"Summarize the following in bullet point form:\n{text}"
    }

    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[system_message, user_message]
    )

    summary = response.choices[0].message.content
    return summary


# ========================
# Main Execution Logic
# ========================

def main():
    audio_file_path = "Warren+Buffett+On+Exposing+Business+Frauds+And+Deception.mp3"  # Change to your audio file path

    print("Starting transcription...")
    transcription = transcribe_audio(audio_file_path)
    print("\nTranscription Result:\n")
    print(transcription)

    print("\nGenerating summary in bullet points...")
    summary = summarize_text_bullet_points(transcription)
    print("\nSummary:\n")
    print(summary)


if __name__ == "__main__":
    main()