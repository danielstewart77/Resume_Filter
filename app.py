import os
import csv
import re
import json

import concurrent.futures
from extraction import extract_text_from_pdf
from llm import extract_using_text
from models import Candidate, Filters, FitmentScore, FluffAnalysis, Responsibilities, RequiredSkills, PreferredSkills, ShouldInterview, TechnicalEnvironment, WorkingConditions

# Path to the resumes directory
RESUMES_FOLDER = "resumes/"
OUTPUT_CSV = "developer.csv"

# List to store candidates' selection criteria
candidates_list = []

# Iterate through the files in the resumes folder
for file_name in os.listdir(RESUMES_FOLDER):
    # Skip non-PDF files
    if not file_name.endswith('.pdf'):
        continue
    
    # Extract candidate name from filename (remove .pdf extension)
    candidate_name = os.path.splitext(file_name)[0]
    
    # Determine file path
    resume_path = os.path.join(RESUMES_FOLDER, file_name)
    
    # Read and extract text from the file
    text_resume = extract_text_from_pdf(file_path=resume_path) if os.path.exists(resume_path) else ""
    text_coverletter = ""  # No cover letter processing in simple loop

    # Combine text from resume and cover letter
    combined_text = f"{text_resume}\n{text_coverletter}"

    llm_model = "gpt-4.1"

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = {
            "candidate": executor.submit(extract_using_text, combined_text, llm_model, Candidate),
            "filters": executor.submit(extract_using_text, combined_text, llm_model, Filters),
            "responsibilities": executor.submit(extract_using_text, combined_text, llm_model, Responsibilities),
            "requiredSkills": executor.submit(extract_using_text, combined_text, llm_model, RequiredSkills),
            "preferredSkills": executor.submit(extract_using_text, combined_text, llm_model, PreferredSkills),
            "technicalEnvironment": executor.submit(extract_using_text, combined_text, llm_model, TechnicalEnvironment),
            "workingConditions": executor.submit(extract_using_text, combined_text, llm_model, WorkingConditions),
            "fluffAnalysis": executor.submit(extract_using_text, combined_text, llm_model, FluffAnalysis),
        }

    results = {key: f.result() for key, f in futures.items()}

    # Serialize results to JSON string for the secondary extractions    
    results_json = json.dumps({k: v.model_dump() if hasattr(v, 'model_dump') else v for k, v in results.items()})
    
    results["fitment"] = extract_using_text(
        results_json,
        llm_model,
        FitmentScore
    )

    results_json = json.dumps({k: v.model_dump() if hasattr(v, 'model_dump') else v for k, v in results.items()})

    results["shouldInterview"] = extract_using_text(
        results_json,
        llm_model,
        ShouldInterview
    )

    # Combine all extracted data into a single dictionary
    candidate_data = {
        "first_last_name": candidate_name,
        **results["candidate"].model_dump(),
        **results["filters"].model_dump(),
        **results["responsibilities"].model_dump(),
        **results["requiredSkills"].model_dump(),
        **results["preferredSkills"].model_dump(),
        **results["technicalEnvironment"].model_dump(),
        **results["workingConditions"].model_dump(),
        **results["fluffAnalysis"].model_dump(),
        **results["fitment"].model_dump(),
        **results["shouldInterview"].model_dump(),
    }
    
    # Add candidate to the list
    candidates_list.append(candidate_data)

# Save to CSV
if candidates_list:  # Only write if we have candidates
    with open(OUTPUT_CSV, mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = candidates_list[0].keys()  # Get field names from the first candidate
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(candidates_list)  # Write all candidates

    print(f"Processed {len(candidates_list)} candidates. Data saved to {OUTPUT_CSV}")
else:
    print("No candidates were processed.")
