import openai

# Set your OpenAI API key here
openai.api_key = "your-api-key-here"

def generate_essay(prompt, max_tokens=800):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are an academic writing assistant."},
                {"role": "user", "content": f"Write an essay on: {prompt}"}
            ],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        essay = response['choices'][0]['message']['content'].strip()
        return essay
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    user_prompt = input("Enter your essay prompt: ")
    print("\nGenerating essay...\n")
    essay = generate_essay(user_prompt)
    print(essay)
