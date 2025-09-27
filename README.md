# LLM Practice Repository

This repository contains experiments and practice code for working with Large Language Models (LLMs). It's designed for learning, experimentation, and hands-on exploration of various LLM APIs and frameworks.

## 🚀 Features

- **Hands-on examples** of LLM workflows using LangChain
- **Testing different APIs** and frameworks (Groq, OpenAI, etc.)
- **Simple experiments** for learning and exploration
- **Modular code structure** for easy experimentation
- **Environment-based configuration** for secure API key management

## 📋 Prerequisites

- Python 3.8 or higher
- Git
- API keys for the LLM providers you want to use

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Amanatal11/llm-practice-.git
cd llm-practice-
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory and add your API keys:

```bash
# Copy the example file
cp .env.example .env

# Edit .env with your actual API keys
nano .env
```

Example `.env` file:
```env
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

## 📁 Project Structure

```
llm-practice-/
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── llm_test.py              # Basic LLM interaction example
└── venv/                    # Virtual environment (not tracked in git)
```

## 🧪 Usage Examples

### Basic LLM Interaction

Run the basic example to test your setup:

```bash
python llm_test.py
```

This will:
- Initialize a Groq LLM model (llama-3.1-8b-instant)
- Send a test message about variational autoencoders
- Display the response and metadata

### Customizing the Example

You can modify `llm_test.py` to:
- Change the model (e.g., to a different Groq model)
- Adjust temperature and other parameters
- Test different prompts and use cases
- Add more complex conversation flows

## 🔧 Available Models and APIs

### Groq (Currently Implemented)
- **llama-3.1-8b-instant**: Fast, efficient model for quick responses
- **llama-3.1-70b-versatile**: More capable model for complex tasks
- **mixtral-8x7b-32768**: Mixture of experts model

### Planned Integrations
- OpenAI GPT models
- Anthropic Claude models
- Local models via Ollama
- Hugging Face models

## 🎯 Learning Objectives

This repository helps you learn:

1. **LLM Integration**: How to connect to different LLM providers
2. **Prompt Engineering**: Crafting effective prompts for various tasks
3. **LangChain Framework**: Using LangChain for LLM application development
4. **API Management**: Handling API keys and rate limiting
5. **Response Processing**: Working with LLM outputs and metadata

## 🚧 Development Roadmap

- [ ] Add more LLM provider integrations
- [ ] Implement conversation memory and context management
- [ ] Add text processing and analysis examples
- [ ] Create RAG (Retrieval-Augmented Generation) examples
- [ ] Add streaming response examples
- [ ] Implement cost tracking and usage monitoring
- [ ] Add unit tests and examples

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🔗 Useful Resources

- [LangChain Documentation](https://python.langchain.com/)
- [Groq API Documentation](https://console.groq.com/docs)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## 📞 Support

If you have questions or run into issues:

1. Check the [Issues](https://github.com/Amanatal11/llm-practice-/issues) page
2. Create a new issue with detailed information
3. Include error messages and steps to reproduce

---

Happy coding and exploring the world of Large Language Models! 🚀
