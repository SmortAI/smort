# Dockerfile, Image, Container

FROM python:3.6

ADD main.py . 

RUN apt-get python-pyaudio
RUN pip install SpeechRecogntion 

CMD ["python", "./main.py"]