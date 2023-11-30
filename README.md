# AppRouterBot: Next.js Routing Expert

## Overview
AppRouterBot is a chatbot finetuned on the Next.js app router documentation. This repository houses both the training pipeline for the chatbot and a Next.js application to interact with the trained model.

## Project Structure
- **`/chatbot`**: Contains the Python code for crawling the Next.js documentation, generating training data, and training the Llama-2-13b.
- **`/web-app`**: A simple Next.js application to interact with the trained chatbot model.

## Workflow
1. **Data Crawling**: A Crawler targets relevant Next.js documentation pages, extracting the pages for training and saving them.
2. **Data Transformation**: The TrainingDataGenerator processes the crawled data and formats it into a JSONL structure using GPT-4, suitable for fine-tuning a chat model.
3. **Model Training**: We utilize Replicate to train the Llama-2-13b model with the generated data.
4. **Hosting and Interaction**: The trained model is hosted in Replicate and made accessible through the simple nextjs app.

## Getting Started

## Contributing

## License
