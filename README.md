# AI Business Assistant

AI Business Assistant is a Streamlit application that provides tailor-made responses to business-related questions. It uses OpenAI's GPT-3.5 Turbo model to generate intelligent and helpful answers based on user input.

## Features
- Answer a couple of questions to get a tailor-made response
- Collects information about the user's name, company name, location, business problems, time consumers, strategy struggles, and email
- Uses the collected information to generate a chatbot response using GPT-3.5 Turbo
- Sends the chatbot response to the user via email

## Usage
1. Install the required dependencies: `pip install -r requirements.txt`
2. Set up the necessary environment variables in a `.env` file:
   - `OPENAI_API_KEY`: Your OpenAI API key
   - `EMAIL`: Your email address
   - `PASSWORD`: Your email password
3. Run the application: `streamlit run app.py`
4. Access the application in your browser at `http://localhost:8501`

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
