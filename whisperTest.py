#descargar whisper desde github
#correr la siguiente linea en la terminal abriendola como administrador
#pip install git+https://github.com/openai/whisper.git 
#instalar chocolatey
#correr la siguiente linea en la terminal abriendola como administrador
#@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
#instalar ffmpeg
#correr la siguiente linea en la terminal abriendola como administrador
#choco install ffmpeg
#Y listo, ya puedes correr el siguiente codigo

import whisper

model = whisper.load_model('small')

#Asegurarse que el archivo de audio este en la misma carpeta que este archivo y tenga el mismo nombre
result = model.transcribe('LLamada.wav', fp16=False)
result['text']
print(result['text'])
