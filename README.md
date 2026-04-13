# ⚡ LLM Model Comparison Dashboard

A local benchmarking tool that runs the same prompt across multiple AI models and compares their speed and response quality side by side.

## What it does

- Run any prompt across multiple local LLMs simultaneously
- Measure and compare response times for each model
- View answers side by side to evaluate quality
- See a summary of the fastest model and speed difference

> Note: All models run locally — no API costs, no cloud, no internet required after initial setup.

## Demo

| Model      | Size   | Response Time |
| ---------- | ------ | ------------- |
| llama3.2   | 2 GB   | ~4-6s         |
| phi4-mini  | 3 GB   | ~10-30s       |
| qwen3.5:9b | 6.6 GB | ~25-35s       |

> Note: Response times vary depending on your hardware.

## Tech Stack

- Python
- Ollama — runs local LLMs
- Streamlit — web interface

## Setup

1. Clone the repository

```
git clone https://github.com/4RGUS/llm-benchmarking-dashboard.git
cd model-inference
```

2. Create a virtual environment

```
py -m venv venv
```

3. Activate the virtual environment

```
venv\Scripts\activate
```

> Note: Run this every time you open a new terminal before working on the project.

4. Install dependencies

```
py -m pip install -r requirements.txt
```

5. Install Ollama and pull the models

```
ollama pull llama3.2
ollama pull phi4-mini
ollama pull qwen3.5:9b
```

6. Run the app

```
streamlit run app.py
```

## How it works

1. Enter any prompt in the text box
2. Click **Run Benchmark**
3. The app runs your prompt through all 3 models one by one
4. Results are displayed side by side with response times and a progress bar
5. A summary at the bottom shows the fastest model and the speed difference

## Key insight

Model size alone does not determine speed. Architecture, quantization, and how Ollama loads the model all affect performance. This dashboard helps you make informed decisions about which model to use for your specific use case.

## Project structure

```
model-inference/
├── benchmark.py      # Runs models and returns results
├── app.py            # Streamlit web UI
├── requirements.txt  # Python dependencies
└── README.md         # This file
```
