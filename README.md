tool for downloading, transcribing and summarizing yt videos

if you just want to download and transcribe, you can skip the setup

to setup, run:
enter your deepseek api key

```console
foo@bar yt-transcribe $ python3 setup.py
enter your api key here:
```

to download run:

```console
foo@bar yt-transcribe $ python src/main.py download <video url>
```

this downloads the audio of the youtube video to the audios directory

to transcribe run:

```console
foo@bar yt-transcribe $ python src/main.py transcribe <file name>
```

this transcribes the audio file and creates a text file in the transcriptions directory with the transcribed text

to summarize run:

```console
foo@bar yt-transcribe $ python src/main.py summarize <file name>
```

this summarizes the text using the api key you provided and then
creates a file in the summaries directory with the summary
