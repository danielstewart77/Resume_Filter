# Internship Resume Filter

This project automates the extraction and evaluation of candidate resumes and cover letters for internship selection, using Large Language Models (LLMs) and structured criteria.

## Features
- **Automated Resume & Cover Letter Parsing:** Extracts text from PDF resumes and cover letters in the `resumes/` folder.
- **LLM-Powered Feature Extraction:** Uses Azure OpenAI (or compatible LLM) to analyze candidate documents and extract structured information based on a Pydantic model.
- **Selection Criteria:** Evaluates candidates on experience, skills, project history, and more, including a 'fluff' analysis and fitment score.
- **CSV Output:** Saves structured candidate data to a CSV file for easy review and further processing.

## Project Structure
```
app.py                      # Main script to process resumes and generate CSV
extraction.py               # PDF text extraction logic
llm.py                      # LLM API integration and feature extraction
models.py                   # Pydantic model for selection criteria
requirements.txt            # Python dependencies
resumes/                    # Folder containing candidate resumes and cover letters
candidates_selection*.csv   # Output CSV files
```

## How It Works
1. Place candidate resumes and cover letters in the `resumes/` folder. Filenames should follow the format: `Last, First Resume.pdf` and `Last, First CL ML UL.pdf`.
2. Run the main script:
   ```powershell
   python app.py
   ```
3. The script will:
   - Extract text from each candidate's resume and cover letter
   - Use the LLM to extract structured features (skills, experience, etc.)
   - Save the results to `candidates_selection2.csv`

## Selection Criteria
The evaluation is based on the following fields (see `models.py`):
- Name, phone, email
- Years of experience (ML, NLP, Data Science)
- ML models and frameworks used
- Programming languages
- PDF and vector database experience
- Past projects
- Fluff level and analysis
- Fitment score (good/medium/poor fit)
- Interview recommendation

## Requirements
- Python 3.10+
- Azure OpenAI API key (set as `AZURE_OPENAI_API_KEY` in a `.env` file)
- See `requirements.txt` for dependencies

## Setup
1. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
2. Create a `.env` file with your Azure OpenAI API key:
   ```env
   AZURE_OPENAI_API_KEY=your_api_key_here
   ```
3. Place resumes and cover letters in the `resumes/` folder.

## Customization
- Adjust the selection criteria in `models.py` as needed.
- Change the LLM model name in `app.py` if using a different deployment.

## License
MIT License

---

*Created by Daniel Stewart, 2025.*
