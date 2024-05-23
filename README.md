# ArXiv LLM-powered article extraction
This project extracts all Articles of ArXiv related to computer science for a given day and uses then an LLM to filter then for given topics.

# Requirements
To run this project, you need an Anthropic API key and python >= 3.8.

Use this link to setup your Anthropic API key if you do not have one yet: https://console.anthropic.com/dashboard

You can install the required Python packages by running the following command:

```
pip install -r requirements.txt
```

# Setup
Clone this repository to your local machine.
Create a .env file in the project directory and add your Anthropic API key in the following format:

```
ANTHROPIC_API_KEY=your_api_key_here
```

Replace your_api_key_here with your actual Anthropic API key.

# Usage
To get all articles for a given day related to the topic you desire, follow these steps:

- Run completely the "article_extraction.ipynb" notebook. Notebook should take around 15 minutes to run as of today. Main bottleneck is currently API rate limits, which means I need to set up a timeout for LLM not to quickly reach max tokens per minute.
- Run the Streamlit application by executing the following command:

```
streamlit run app.py
```

The Streamlit application will open in your default web browser.
Follow the instructions provided in the Streamlit interface to play the game.
LLM used is currently Claude 3 Haiku, this may change depending on latest releases.

# Contributing
If you would like to contribute to this project, please follow these steps:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Make your changes and commit them with descriptive commit messages.
- Push your changes to your forked repository.
- Submit a pull request to the main repository, explaining your changes and their benefits.

# License
This project is licensed under the MIT License.

# Acknowledgments
- Claude-3 is developed by Anthropic.
- arXiv is a free distribution service and an open-access archive for nearly 2.4 million scholarly articles in the fields of physics, mathematics, computer science, quantitative biology, quantitative finance, statistics, electrical engineering and systems science, and economics.
