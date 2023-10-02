from google.cloud import speech

# Initialize the SpeechClient
client = speech.SpeechClient.from_service_account_file('key.json')

file_name = 'Llamada.wav'

with open(file_name, 'rb') as file:
    content = file.read()

audio_file = speech.RecognitionAudio(content=content)

config = speech.RecognitionConfig(
    sample_rate_hertz=8000,
    
    language_code='en-ES',
    enable_automatic_punctuation=True,
)

# Use asynchronous recognition to get the operation
operation = client.long_running_recognize(config=config, audio=audio_file)

# Wait for the operation to complete
response = operation.result()

# Print the transcribed text
for result in response.results:
    print("Transcript: {}".format(result.alternatives[0].transcript))
