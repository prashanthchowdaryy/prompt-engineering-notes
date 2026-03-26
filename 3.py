#3. Generating prompt using python loop

topics = ["artificial intelligence", "space exploration", "ancient history"]
tones = ["serious", "humorous", "inspirational"]

# Create a list of prompts based on combinations of topics and tones
prompts = []
for topic in topics:
    for tone in tones:
        prompt = f"Write a {tone} story about {topic}."
        prompts.append(prompt)

# Print all generated prompts
for prompt in prompts:
    print(prompt)
    #=====================*==============
def create_summary_prompt(text):
    prompt_template = "Summarize the following text: {text}"
    return prompt_template.format(text=text)

# Example of using the template
input_text = "AI is rapidly changing the way we work, communicate, and solve problems."
summary_prompt = create_summary_prompt(input_text)
print("Generated Summary Prompt:", summary_prompt)