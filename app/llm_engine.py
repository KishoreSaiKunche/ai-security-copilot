import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_with_llm(log, threat):

    prompt = f"""
    You are a cybersecurity analyst.

    Log: {log}
    Threat: {threat}

    Explain the threat and suggest mitigation steps.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response['choices'][0]['message']['content']