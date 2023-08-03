import streamlit as st
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.schema import SystemMessage, HumanMessage
import openai
import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up OpenAI API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

def main():
    st.title("AI Survey Bot Recommendation")
    st.write("**Answer a couple of questions to get a tailor-made response.**")

    # Question 1
    name = st.text_input("**Question 1: What is your name?**")

    # Question 2
    company_name = st.text_input("**Question 2: What is your company name?**")

    # Question 3
    company_location = st.text_input("**Question 3: Where is your company located?**")

    # Question 4    
    st.write("**Question 4: Are any of these a problem in your business?**")
    # Create a list of problems
    problems = [
        "**Getting leads**",
        "**Closing sales**",
        "**Retaining customers**",
        "**Finding the right talent**",
        "**Not having enough time**",
        "**Customer support**",
        "**Strategic thinking**",
        "**Other**"
    ]
    # Create two columns with equal width
    col1, col2 = st.columns(2)
    # Loop through the problems and create checkboxes in each column
    for i, problem in enumerate(problems):
        # Use the modulo operator to alternate between columns
        if i % 2 == 0:
            col1.checkbox(label=problem, key=problem)
        else:
            col2.checkbox(label=problem, key=problem)
    # If Other is selected, prompt the user for more explanation
    other_problem = ""
    if st.session_state.get("Other"):
        other_problem = st.text_input("**Can you give a further explanation of the problem?**")

    # Question 5
    time_consumers = st.text_area("**Question 5: What are the three biggest time consumers or deficiencies of your business?**")

    # Question 6
    strategy_struggles = st.text_area("**Question 6: When coming up with strategy, what are the struggles there?**")

    # Question 7
    email = st.text_input("**Question 7: Enter your Email to get the custom answers sent to you**")

    # Submit button
    if st.button("Submit"):
        # Save the survey data and send it to the user
        send_survey_results(name, company_name, company_location, problems, other_problem, time_consumers, strategy_struggles, email)

def send_survey_results(name, company_name, company_location, problems, other_problem, time_consumers, strategy_struggles, email):
    # Generate chatbot response using OpenAI GPT-3.5 Turbo
    system_message_template = SystemMessagePromptTemplate.from_template(
        template="You are a helpful assistant that recommends AI tools based on user's business needs."
    )
    human_message_template = HumanMessagePromptTemplate.from_template(template="{text}")

    chat_prompt = ChatPromptTemplate.from_messages([system_message_template, human_message_template])

    messages = chat_prompt.format_prompt(text=f"I am {name}, representing {company_name} located in {company_location}. We are facing the following problems in our business: {', '.join(problems)}. {other_problem}. The three biggest time consumers or deficiencies in our business are: {time_consumers}. When coming up with strategy, we struggle with: {strategy_struggles}.").to_messages()

    messages_dict = []
    for message in messages:
        if isinstance(message, SystemMessage):
            messages_dict.append({"role": "system", "content": message.content})
        elif isinstance(message, HumanMessage):
            messages_dict.append({"role": "user", "content": message.content})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages_dict,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    # Extract the chatbot response
    chatbot_response = response.choices[0].message.content.strip()

    # Display the chatbot response
    st.subheader("Chatbot Response")
    st.write(chatbot_response)

    # Send the survey results to the user via email
    send_email(email, chatbot_response)

def send_email(email, message):
    # Set up the email parameters
    sender = "L.fanampe@gmail.com"
    receiver = email
    subject = "Chatbot Response"
    body = message

    # Create the email message
    email_message = MIMEText(body)
    email_message["Subject"] = subject
    email_message["From"] = sender
    email_message["To"] = receiver

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(email, password)
        server.sendmail(sender, receiver, email_message.as_string())

if __name__ == "__main__":
    main()
