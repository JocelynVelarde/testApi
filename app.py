from flask import Flask, render_template, request, send_file
from google.cloud import speech
import os

app = Flask(__name__)

# Initialize the SpeechClient
client = speech.SpeechClient.from_service_account_file('key.json')

@app.route('/')
def index():
    return render_template('upload.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio_file' not in request.files:
        return "No file part"

    audio_file = request.files['audio_file']

    if audio_file.filename == '':
        return "No selected file"

    if audio_file:
        # Save the uploaded file temporarily
        file_path = 'temp_audio.mp3'
        audio_file.save(file_path)

        with open(file_path, 'rb') as file:
            content = file.read()

        audio = speech.RecognitionAudio(content=content)

        config = speech.RecognitionConfig(
            sample_rate_hertz=8000,
            language_code='en-ES',
            enable_automatic_punctuation=True,
        )

        # Use asynchronous recognition to get the operation
        operation = client.long_running_recognize(config=config, audio=audio)

        # Wait for the operation to complete
        response = operation.result()

        # Generate a transcription text
        transcript = ""
        for result in response.results:
            transcript += result.alternatives[0].transcript + " "

        # Save the transcription to a .txt file
        transcript_file_path = 'transcript.txt'
        with open(transcript_file_path, 'w') as txt_file:
            txt_file.write(transcript)

        # Clean up the temporary audio file
        os.remove(file_path)

        return send_file(transcript_file_path, as_attachment=True, download_name='transcript.txt')

if __name__ == '__main__':
    app.run(debug=True)
