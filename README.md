# ODE-Slope-Fields

This program is responsible for taking a user input which represents the slope of function y or the ordinary differential equation that needs solving in order to provide some qualitative information using slope fields. Using sympy and matplotlib, we plot this slope field after evluating the expression and defining variables. I plan on expanding this into Euler's method to provide an alternative approach that uses numerical methods instead.

If you'd simply like to use the public version available, reach out for access, and if you already have access, the link is here [RAG Finance App](https://rag-financial-analyst.streamlit.app)

## Features
- **Automated Data Collection**: Scheduled scripts scrape price changes and financial news articles.
- **Vector Database Integration**: Stores processed data in a vector database for efficient querying and retrieval.
- **Comprehensive Reports**: Combines textual analysis with numerical data for detailed financial insights.
- **Adaptability**: Dynamically adjusts reporting based on data availability for specified time periods.

## Installation

Clone the repository available here [RAG Finance App Repository](https://github.com/toritotony/RAG-Financial-Analyst).

## Usage

1. Create a virtual environment to isolate the packages being installed in Step 2.

2. Run `pip install -r requirements.txt` from the directory where your `requirements.txt` file is located.

3. Ensure the following environment variables are configured in a `config.env` file:
   - `OPENAI_API_KEY`
   - `PINECONE_API_KEY`
   - `PINECONE_API_ENV`
   - `PINECONE_INDEX`

4. Use your Task Scheduler and personalize the paths for your `example_scheduledtask.bat`, `example_webscrape.py`, `example_vectorstore.py` file (as well as renaming them to remove the 'example_' prefix) before automating the pipeline flow:
   - Reinstalls packages and libaries necessary for `webscrape.py` and `vectorstore.py`
   - Collect articles and price changes using the `webscrape.py` script.
   - Process and store data using the `vectorstore.py` script.

5. After adding your `config.env` file path into the `app.py` file and renaming it to `app.py`, run `streamlit run app.py` or deploy to streamlit (after adding the secrets to the streamlit app) from your virtual environment. This will output a local URL for you to visit the application. Reports will be generated based on available data and stored in the vector database. Certain reports are available now, with limited data on particular assets and stocks.

## Example Scripts

### Data Collection ('webscrape.py')
```
headers = {'User-Agent': 'Mozilla/5.0'}
url = "https://www.investing.com/news/"
webpage = requests.get(url, headers=headers)
trav = BeautifulSoup(webpage.content, "html.parser")
articles = trav.find_all('div', {'data-test': re.compile('homepage-news-list-item')})
```

### Data Storage ('vectorstore.py')
```
text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=0)
embeddings = OpenAIEmbeddings(model="text-embedding-ada-002", openai_api_key=OPENAI_API_KEY)
vectorstore.add_documents(documents=doc_splits)
```

## Dependencies

- **openai**
- **streamlit**
- **langchain & pinecone**: installed via pip when you install requirements.txt file

## Contributing
Contributions and feedback are welcome! Please open an issue to discuss your proposed changes before submitting a pull request. Ensure that all new code is properly tested and documented.

## License
This project is licensed under the [MIT License](https://opensource.org/license/mit)

