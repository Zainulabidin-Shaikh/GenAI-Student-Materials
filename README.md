# KGP Talkie: GenAI Student Materials

Start with Day 1. Each day has a PDF handout. Coding days also have a notebook. Small lesson files are in that day's assets folder.

## Set up once on Windows

Install Python 3.12. Open PowerShell in this folder. Create a course environment so its packages stay together:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --prefix .venv --name kgp-talkie --display-name "KGP Talkie (course)"
```

Double-click `start-notebooks.cmd` to open Jupyter with this environment. Open a notebook from its `notebooks` folder and select **KGP Talkie (course)**. Run its cells from top to bottom. The saved outputs show an earlier class run. Your model replies and scores may differ.

## Set up local AI models

Install and open Ollama before Day 15. Run these commands once to download the two course models:

```powershell
ollama pull llama3.2
ollama pull nomic-embed-text
ollama list
```

`llama3.2` writes replies. `nomic-embed-text` turns text into number vectors for search. Keep Ollama open while you use these lessons.

For Day 9, follow [the image data steps](day-09/data/README.md) first. Image training takes longer than the small table lessons.

## Lessons

| Day | Topic | Files |
| --- | --- | --- |
| 01 | AI, ML and DL: First Steps | [Handout](day-01/handout.pdf) |
| 02 | Python Basics: Values, Choices, Loops and Functions | [Handout](day-02/handout.pdf) / [Notebook 1](day-02/notebooks/part-1.ipynb) / [Notebook 2](day-02/notebooks/part-2.ipynb) / [Notebook 3](day-02/notebooks/part-3.ipynb) |
| 03 | Pandas: Read and Clean Tables (with NumPy introduction) | [Handout](day-03/handout.pdf) / [Notebook](day-03/notebooks/practice.ipynb) |
| 04 | Matplotlib and Seaborn: Build and Read Charts | [Handout](day-04/matplotlib.pdf) / [Handout](day-04/seaborn.pdf) / [Notebook 1](day-04/notebooks/matplotlib.ipynb) / [Notebook 2](day-04/notebooks/seaborn.ipynb) |
| 05 | Linear Regression: Predict a Number | [Handout](day-05/handout.pdf) / [Notebook](day-05/notebooks/practice.ipynb) |
| 06 | Logistic Regression: Choose a Class | [Handout](day-06/handout.pdf) / [Notebook](day-06/notebooks/practice.ipynb) |
| 07 | KNN: Learn From Nearby Examples | [Handout](day-07/handout.pdf) / [Notebook](day-07/notebooks/practice.ipynb) |
| 08 | Neural Networks: From Inputs to Predictions | [Handout](day-08/handout.pdf) / [Notebook](day-08/notebooks/practice.ipynb) |
| 09 | CNN: Learn Patterns in Images | [Handout](day-09/handout.pdf) / [Notebook](day-09/notebooks/practice.ipynb) |
| 10 | RNN: Read Text in Order | [Handout](day-10/handout.pdf) / [Notebook](day-10/notebooks/practice.ipynb) |
| 11 | LSTM: Keep Useful Context | [Handout](day-11/handout.pdf) / [Notebook](day-11/notebooks/practice.ipynb) |
| 12 | Transformer Inputs: Tokens and Embeddings | [Handout](day-12/handout.pdf) |
| 13 | Inside a Transformer Block | [Handout](day-13/handout.pdf) |
| 14 | How a Transformer Generates Text | [Handout](day-14/handout.pdf) |
| 15 | Write Clear Prompts | [Handout](day-15/handout.pdf) / [Notebook](day-15/notebooks/practice.ipynb) |
| 16 | Give Each Message a Role | [Handout](day-16/handout.pdf) / [Notebook](day-16/notebooks/practice.ipynb) |
| 17 | Teach the Answer Pattern With Examples | [Handout](day-17/handout.pdf) / [Notebook](day-17/notebooks/practice.ipynb) |
| 18 | Run a Language Model With Ollama | [Handout](day-18/handout.pdf) / [Notebook](day-18/notebooks/practice.ipynb) |
| 19 | Control a Local Model's Replies | [Handout](day-19/handout.pdf) / [Notebook](day-19/notebooks/practice.ipynb) |
| 20 | Connect Python to a Local LLM | [Handout](day-20/handout.pdf) / [Notebook](day-20/notebooks/practice.ipynb) |
| 21 | Build Prompts With Reusable Templates | [Handout](day-21/handout.pdf) / [Notebook](day-21/notebooks/practice.ipynb) |
| 22 | Join Steps Into a Chain | [Handout](day-22/handout.pdf) / [Notebook](day-22/notebooks/practice.ipynb) |
| 23 | Choose a Path or Run Two Tasks | [Handout](day-23/handout.pdf) / [Notebook](day-23/notebooks/practice.ipynb) |
| 24 | Turn Replies Into Checked Data | [Handout](day-24/handout.pdf) / [Notebook](day-24/notebooks/practice.ipynb) |
| 25 | Keep a Conversation's History | [Handout](day-25/handout.pdf) / [Notebook](day-25/notebooks/practice.ipynb) |
| 26 | Build a Chatbot Students Can Use | [Handout](day-26/handout.pdf) / [Notebook](day-26/notebooks/practice.ipynb) |
| 27 | Read a PDF Before Asking an LLM | [Handout](day-27/handout.pdf) / [Notebook](day-27/notebooks/practice.ipynb) |
| 28 | Turn a Webpage Into Useful Text | [Handout](day-28/handout.pdf) / [Notebook](day-28/notebooks/practice.ipynb) |
| 29 | Read Word, Excel, and PowerPoint Files | [Handout](day-29/handout.pdf) / [Notebook](day-29/notebooks/practice.ipynb) |
| 30 | Choose a Document Converter | [Handout](day-30/handout.pdf) / [Notebook](day-30/notebooks/practice.ipynb) |
| 31 | Split Long Text Into Useful Chunks | [Handout](day-31/handout.pdf) / [Notebook](day-31/notebooks/practice.ipynb) |
| 32 | Find Related Text With Embeddings | [Handout](day-32/handout.pdf) / [Notebook](day-32/notebooks/practice.ipynb) |
| 33 | Choose What Search Returns | [Handout](day-33/handout.pdf) / [Notebook](day-33/notebooks/practice.ipynb) |
| 34 | Answer From Your Own Documents | [Handout](day-34/handout.pdf) / [Notebook](day-34/notebooks/practice.ipynb) |
| 35 | Check RAG Answers and Summaries | [Handout](day-35/handout.pdf) / [Notebook](day-35/notebooks/practice.ipynb) |
| 36 | Give a Model a Small Python Tool | [Handout](day-36/handout.pdf) / [Notebook](day-36/notebooks/practice.ipynb) |
| 37 | Return Tool Results to the Model | [Handout](day-37/handout.pdf) / [Notebook](day-37/notebooks/practice.ipynb) |
| 38 | Build an Agent That Uses Tools | [Handout](day-38/handout.pdf) / [Notebook](day-38/notebooks/practice.ipynb) |
| 39 | Let an Agent Search Documents | [Handout](day-39/handout.pdf) / [Notebook](day-39/notebooks/practice.ipynb) |
| 40 | Ask a Small Database in Plain English | [Handout](day-40/handout.pdf) / [Notebook](day-40/notebooks/practice.ipynb) |
| 41 | Turn Profile Text Into Clear Fields | [Handout](day-41/handout.pdf) / [Notebook](day-41/notebooks/practice.ipynb) |
| 42 | Extract a Resume Into Checked JSON | [Handout](day-42/handout.pdf) / [Notebook](day-42/notebooks/practice.ipynb) |
| 43 | Build a Resume Upload App | [Handout](day-43/handout.pdf) / [Notebook](day-43/notebooks/practice.ipynb) |
| 44 | Prepare a Local LLM App for Deployment | [Handout](day-44/handout.pdf) / [Notebook](day-44/notebooks/practice.ipynb) |

## Run the two apps

From this repo folder, run one command at a time:

```powershell
.\.venv\Scripts\python.exe -m streamlit run day-26/app.py
.\.venv\Scripts\python.exe -m streamlit run day-43/app.py
```

Day 26 is a chat app. Day 43 reads a PDF resume and returns data. Use the fictional resumes in its assets folder for practice.

## Get class updates

Use `git pull` before class, or download the latest repo ZIP. Keep your own practice copies outside this repo if you want to keep your edits. The KGP Talkie team updates this repo from the source course.
