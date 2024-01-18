from langchain.llms import GooglePalm
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain.prompts import SemanticSimilarityExampleSelector
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts.prompt import PromptTemplate

from few_shots import few_shots

import os
from dotenv import load_dotenv
load_dotenv()
key = "AIzaSyAmLapsZN2YKgczh0Igfhxyy4tdZOW39G0"

memory = []

def get_few_shot_db_chain():                                                                   # Connect the database
    db_user = "root"
    db_password = "password123"
    db_host = "localhost"
    db_name = "mydatabase"

    db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",
                              sample_rows_in_table_info=3)
    llm = GooglePalm(google_api_key=key, temperature=0.2)                                      # Create an LLM object                              

    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')    # Using vector embeddings and saving in  
    to_vectorize = [" ".join(example.values()) for example in few_shots]                       # a vector database.
    vectorstore = Chroma.from_texts(to_vectorize, embedding=embeddings, metadatas=few_shots)
    example_selector = SemanticSimilarityExampleSelector(
        vectorstore=vectorstore,
        k=2,
    )
    mysql_prompt = """Act as a personal assistant who is also a MySQL expert. Address them in second person. Given an input question,
    first create a syntactically correct MySQL query to run, then look at the results of the query and return the answer to the input
    question. ALWAYS use creative text generation to provide the answer in a sentence format rather than just deterministic query values.
    You can order the results to return the most informative data in the database. Never query for all columns from a table. You must query
    only the columns that are needed to answer the question. Wrap each column name of each table in backticks (`).
    Pay attention to use only the column names you can see in the tables below. Be careful to not query for columns that do not exist.
    Also, pay attention to which column is in which table. 
    Pay attention to use CURDATE() function to get the current date, if the question involves "today".

    Use the following format:

    Question: Question here
    SQLQuery: Query to run with no pre-amble
    SQLResult: Result of the SQLQuery
    Answer: Final answer here
    
    No pre-amble.
    """

    example_prompt = PromptTemplate(
        input_variables=["Question", "SQLQuery", "SQLResult", "Answer", ],
        template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",
    )

    few_shot_prompt = FewShotPromptTemplate(
        example_selector=example_selector,
        example_prompt=example_prompt,
        prefix=mysql_prompt,
        suffix=PROMPT_SUFFIX,
        input_variables=["input", "table_info", "top_k"],                                       # These variables are used in the prefix and                                                                                                 #suffix
    )
    chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)
    return chain