# AI Data Cleaning Tool

An intelligent, automated solution designed to streamline the data preparation process. By leveraging AI-driven logic, this tool detects anomalies, standardizes formats, and fills in missing values, transforming messy datasets into analyst-ready information with minimal manual intervention.

## 🚀 Tech Stack

* **Language:** Python 3.9+
* **AI/ML:** OpenAI GPT API (or local LLMs via LangChain)
* **Data Processing:** Pandas, NumPy
* **Interface:** Streamlit (for Web UI)
* **Environment Management:** Python-dotenv

## ✨ Features

* **Automated Error Detection:** Identifies outliers, null values, and structural inconsistencies using machine learning.
* **Smart Standardization:** Automatically corrects date formats, phone numbers, and addresses.
* **Natural Language Cleaning:** Describe how you want your data cleaned (e.g., "Remove rows where age is negative") and let the AI generate the logic.
* **Deduplication:** Uses fuzzy matching to find and merge duplicate records that are not exact matches.
* **Data Imputation:** Predicts and fills missing values based on existing patterns in the dataset.

## 🛠 How It Works

The tool operates in a three-stage pipeline:

1. **Profiling:** The system scans the uploaded CSV/Excel file to generate a "health report" of the data quality.
2. **AI Mapping:** The LLM analyzes the schema and suggests specific cleaning rules based on the column context.
3. **Transformation:** The tool executes the cleaning scripts using Pandas, providing a side-by-side comparison of the "Before" and "After" states for user approval.

## 🏁 Getting Started

### Prerequisites

* Python 3.9 or higher
* An OpenAI API Key (or access to a compatible LLM provider)

## 📥 Installation

1. **Clone the repository:**
```bash
git clone https://github.com/iosierra/ai-data-cleaning-tool.git
cd ai-data-cleaning-tool

```


2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```


3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Configure Environment Variables:**
Create a `.env` file in the root directory and add your API key:
```env
OPENAI_API_KEY=your_api_key_here

```



## 💡 How To Use

1. **Launch the application:**
```bash
streamlit run app.py

```


2. **Upload Data:** Drag and drop your CSV or XLSX file into the dashboard.
3. **Review Suggestions:** Look at the AI-generated cleaning suggestions (e.g., "Convert 'Date' column to YYYY-MM-DD").
4. **Execute & Export:** Click "Apply Cleaning" and download your processed, clean dataset.

---
