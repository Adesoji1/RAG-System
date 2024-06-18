# RAG System with LLAMAIndex and OpenAI

This repository contains a Google Colab notebook that demonstrates how to build a Retrieval-Augmented Generation (RAG) system using LLAMAIndex, FAISS, and the OpenAI API. The system processes text from H.P. Lovecraft's story ["The Colour Out of Space"](https://www.hplovecraft.com/writings/texts/fiction/cc.aspx), stores the embedded text in a vector database, and uses it to enhance query responses with relevant context.

## Table of Contents

- [Setup Instructions](#setup-instructions)
- [Prerequisites](#prerequisites)
- [Notebook Walkthrough](#notebook-walkthrough)
- [How It Works](#how-it-works)
- [Running the Notebook](#running-the-notebook)
- [License](#license)

## Setup Instructions

1. Clone this repository or download the notebook file.
2. Open the notebook in Google Colab.
3. Follow the steps in the notebook to install the necessary libraries and set up the environment.

## Prerequisites

- Google Colab
- OpenAI API key

## Notebook Walkthrough

### 1. Install Required Libraries

The notebook installs the following libraries:
- `llama-index`
- `faiss-cpu or faiss-gpu`
- `openai`
- `requests`

### 2. Set Up OpenAI API Key

Set your OpenAI API key to authenticate and use the OpenAI API for embeddings and completions.

### 3. Download and Process Text

The notebook downloads the text of "The Colour Out of Space" from the provided URL and chunks it into smaller, configurable pieces.

### 4. Embed Text using OpenAI API

Each text chunk is embedded using OpenAI's text embedding model.

### 5. Store Vectors in FAISS

The embeddings are stored in a FAISS index for efficient similarity search.

### 6. Build the RAG System

The notebook sets up a RAG system to process a query, retrieve relevant chunks from the vector database, and enhance the query response with the top K results.

## How It Works

1. **Text Chunking**: The text is divided into smaller chunks to make it manageable for embedding and retrieval.
2. **Embedding**: Each chunk is converted into a vector representation using OpenAI's embedding model.
3. **Vector Storage**: The vectors are stored in a FAISS index, which allows for efficient similarity searches.
4. **Query Processing**: When a query is made, the system searches the FAISS index to find the most relevant chunks.
5. **Context Enhancement**: The top K results from the search are used to enhance the context of the query response.

## Running the Notebook

1. Open the notebook in Google Colab.
2. Run each cell step-by-step to process the text, embed it, store the vectors, and set up the RAG system.
3. Modify the query as needed and observe the enhanced responses.

### Example Query

The example query used in the notebook is:
```
What happened on November 1st, 1907?
```

### Example Output

The system will provide a contextually enhanced answer based on the most relevant text chunks retrieved from the vector database.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

