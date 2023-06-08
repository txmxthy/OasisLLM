<h1 align="center">Welcome to Oasis 🏝️</h1>



<h4 align="center"> 
    Democratizing LLMs and Enabling Offline Local Querying
</h4>

[//]: # (Repo Information Badges)
<p align="center">
 <a href="license">
	<img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge" alt="License"></a>
<a href="https://github.com/txmxthy/oasis/issues">
	<img src="https://img.shields.io/github/issues/txmxthy/oasis?style=for-the-badge" alt="issues - oasis"></a>
<a href="https://github.com/txmxthy/oasis">
	<img src="https://img.shields.io/github/stars/txmxthy/oasis?style=for-the-badge" alt="stars - oasis"></a>
<a href="https://github.com/txmxthy/oasis">
	<img src="https://img.shields.io/github/forks/txmxthy/oasis?style=for-the-badge" alt="forks - oasis"></a>
</p>


[//]: # (Tech Stack Badges)

<p align="center">
  <a href="https://www.python.org/">
		<img src="https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white" alt="Python"></a>
    <a href="https://www.trychroma.com/">
        <img src="https://img.shields.io/badge/Chroma-ff8a4b?style=for-the-badge&logo=chroma&logoColor=white" alt="Chroma"></a>
    <a href="https://python.langchain.com/en/latest/index.html">
        <img src="https://img.shields.io/badge/Lang%20Chain-d40a8d?style=for-the-badge&logo=langchain&logoColor=white" alt="LangChain"></a>
    <a href="https://huggingface.co/">
        <img src="https://img.shields.io/badge/Hugging%20Face-ffd21e?style=for-the-badge&logo=huggingface&logoColor=white" alt="Hugging Face"></a>
</p>

[//]: # (Version)
<p align="center">
  <img src="https://img.shields.io/badge/Version-0.0.1-blue?style=for-the-badge" alt="Version">
</p>

## About

Oasis transforms your files into vector embeddings, and enables offline querying.
We use [Chroma](https://www.trychroma.com/) to store the embeddings,
and [LangChain](https://python.langchain.com/en/latest/index.html) to query them.
There are a variety of open source models which can be configured to work with Oasis, the license of the models may
vary.
Models from [Hugging Face](https://huggingface.co/) are used by default.

You can run everything offline after the initial setup, with an assortment of compatible models available for selection
to be made available offline.

- The ingestion process uses `LangChain`
- Oasis uses a local LLM to process and understand questions from which it can generate a response.
- By using the pretrained models you are able to leverage the cutting edge models available online, and apply a large
  corpus of your own data to enable top-tier context aware and domain specific performance.
  - This context is taken from multiple sources across the local vector database via a similarity search.

## Ingestion:

Currently only .txt, .csv, and .pdf files are supported with more to come.
Place your files in the `/data/ingestion/` folder, and run `ingest.py` to absorb them into the local vector database.
Processing the files may take some time depending on the number of words/tokens in the files.

## Database

The database is kept at `/data/chroma/` - for a fresh start, delete the subdir `index` and run `ingest.py` again.

## Querying:

Run `main.py` to start the program and select the query option.
Loading the model may take some time.
Once it is loaded the shell will prompt you for a question, enter your question and submit it with enter.

The model will then search the local vector database for the most relevant documents, and use them as context to answer
your question. The time taken scales with GPU power.

The model will then print the answer as well as asking if the user would like to see its references. You can choose to
see the references before proceeding or not. You are then brought back to the question interface to submit another
question.

For a good query, be specific and give context!

## Installation

Install Oasis with Git

```bash
  git clone https://github.com/txmxthy/oasis.git
```

## Usage

To run oasis, ensure you have the pre-requisites installed, and you have followed the steps in docs/setup.md, then run
main.py

```bash
  python main.py
```

## Demo

Gif of Oasis in action to come

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.
Please adhere to this project's `code of conduct`.

