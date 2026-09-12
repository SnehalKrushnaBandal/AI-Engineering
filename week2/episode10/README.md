# **Episode 10 — Streaming LLM Responses**

## **📌 Overview**

Implemented streaming responses using the Groq API to receive and display
LLM-generated content incrementally instead of waiting for the complete response.

## **🧠 What I Learned**

- Normal LLM responses
- Streaming LLM responses
- Processing response chunks
- Displaying LLM responses in real time
- Difference between normal and streaming responses

## **🔄 Workflow**

1. Send User Prompt
2. Send Request to Groq API
3. LLM Generates Response
4. Receive Response in Chunks
5. Process Each Chunk
6. Display Response in Real Time

## **🛠️ Technologies Used**

- Python
- Groq API
- LLM
- python-dotenv

## **💻 Implementation**

The project demonstrates two approaches for receiving an LLM response:

1. **Normal Response** — The complete response is received before displaying it.

2. **Streaming Response** — The response is received and displayed incrementally using `stream=True`.

