# AI Survey Bot Recommendation

This is a Streamlit app that allows users to answer a couple of questions and get a tailor-made response from an AI chatbot. The chatbot uses OpenAI GPT-3.5 Turbo to generate responses based on the user's input.

## Key files

- **app.py** - Main Streamlit app code
- **requirements.txt** - Python dependencies
- **setup.sh** - Heroku config script

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the environment variables:

   - Create a `.env` file in the root directory of the project.
   - Add the following variables to the `.env` file:

     ```plaintext
     OPENAI_API_KEY=your-openai-api-key
     EMAIL=your-email
     PASSWORD=your-password
     ```

4. Run the app:

   ```bash
   streamlit run app.py
   ```

## Usage

1. Open the app in your browser.
2. Answer the questions presented on the app.
3. Click the "Submit" button to get the chatbot response.
4. The chatbot response will be displayed on the app.
5. The chatbot response will also be sent to the email address provided.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.