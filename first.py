#Simple Prompt Creation in Python

# Define a basic prompt
prompt = "Write a story about a squid game."

# Use the prompt with a generative AI model (example for OpenAI API)
print("Prompt created:", prompt)

=====

#2. Creating Prompts Based on User Input

# Example of creating a prompt based on user input
def create_prompt():
    topic = input("Enter the topic for the story: ")
    tone = input("Enter the tone (e.g., serious, humorous, adventurous): ")
   
    prompt = f"Write a {tone} story about {topic}."
    return prompt

# Generate prompt based on user input
user_prompt = create_prompt()
print("Generated Prompt:", user_prompt)

'''
f-string: The f before the string indicates that it’s an f-string,
which allows you to embed expressions inside the string.
The expressions are enclosed in curly braces {}. '''


#===================*===========
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

#============*=============
#5. Generating Multiple Prompts Dynamically Using Lists and Strings
def generate_prompts_from_data(data_list):
    prompts = []
    for item in data_list:
        prompt = f"Explain {item} in simple terms."
        prompts.append(prompt)
    return prompts

# Sample data list (e.g., topics to explain)
data_list = ["quantum computing", "machine learning", "climate change"]

# Generate prompts
prompts = generate_prompts_from_data(data_list)

# Print each prompt
for prompt in prompts:
    print(prompt)

#====================*=========
#6. Advanced Prompt Engineering
def create_stepwise_prompt(context):
    step1_prompt = f"Summarize this text: {context}"
   
    # Generate an AI summary (this is hypothetical code for an API)
    ai_summary = "This is a summary of the context."  # Placeholder for the actual AI API response
   
    step2_prompt = f"Based on the summary: '{ai_summary}', answer the following question: What are the key points?"
   
    return step1_prompt, step2_prompt

context = "Artificial intelligence has become a pivotal technology in the 21st century..."
step1, step2 = create_stepwise_prompt(context)

print("Step 1 Prompt:", step1)
print("Step 2 Prompt:", step2)

#====================*================
#7. Using Prompt Templates with f-Strings

def generate_flexible_prompt(action, subject, tone):
    prompt = f"Write a {tone} {action} about {subject}."
    return prompt

# Example inputs
action = "story"
subject = "the first human on Mars"
tone = "adventurous"

# Generate prompt
prompt = generate_flexible_prompt(action, subject, tone)
print("Generated Prompt:", prompt)