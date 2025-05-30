from openai import OpenAI

def summarize(text: str, config: dict):
    """ sends text data to deepseek R1 and has it summarize the text """

    client = OpenAI(api_key=config["DEEPSEEK_API_KEY"], base_url="https://api.deepseek.com")
    response = client.chat.completions.create(
    model = "deepseek-chat",
    messages = [
        {"role": "system", "content": "You are to act as a summarizer, you are given text and you are to give bullet points and key notes summaries from the text"},
        {"role": "user", "content": text}
    ],
    stream=False
    )
    return (response.choices[0].message.content)