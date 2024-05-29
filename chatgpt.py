from openai import OpenAI
import os

client = OpenAI(
    # This is the default and can be omitted
    #api_key=os.environ.get("OPENAI_API_KEY"),
    api_key="",
)


async def perform_request(usermessage):
    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": usermessage}],
        stream=True,
    )
    out = ""
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            out += chunk.choices[0].delta.content

    return out