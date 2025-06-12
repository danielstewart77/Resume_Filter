import os
import csv
import re
from extraction import extract_text_from_pdf
from llm import extract_using_text
from models import SelectionCriteria

# Path to the resumes directory
RESUMES_FOLDER = "resumes/"
OUTPUT_CSV = "candidates_selection2.csv"

# List to store candidates' selection criteria
candidates_list = []

# Regex pattern to extract names from filenames
name_pattern = re.compile(r"^(.+),\s(.+?)\s(?:CL ML UL\s)?(?:Resume)?\.pdf$")

# Iterate through the files in the resumes folder
for file_name in os.listdir(RESUMES_FOLDER):
    match = name_pattern.match(file_name)
    if not match:
        continue  # Skip files that don't match the expected naming convention

    last_name, first_name = match.groups()
    candidate_name = f"{last_name}, {first_name}"  # Standardized format

    # Determine file paths
    resume_path = os.path.join(RESUMES_FOLDER, f"{last_name}, {first_name} Resume.pdf")
    coverletter_path = os.path.join(RESUMES_FOLDER, f"{last_name}, {first_name} CL ML UL.pdf")

    # Read and extract text from both files
    text_resume = extract_text_from_pdf(file_path=resume_path) if os.path.exists(resume_path) else ""
    text_coverletter = extract_text_from_pdf(file_path=coverletter_path) if os.path.exists(coverletter_path) else ""

    # Combine text from resume and cover letter
    combined_text = f"{text_resume}\n{text_coverletter}"

    # Extract features using LLM
    candidate: SelectionCriteria = extract_using_text(
        text=combined_text, llm_model="gpt-4o-2024-08-06", feature_model=SelectionCriteria
    )

    # Ensure extracted candidate data has the correct name format
    candidate.first_last_name = candidate_name

    # Append candidate's selection criteria to the list
    candidates_list.append(candidate.model_dump())

# Save to CSV
with open(OUTPUT_CSV, mode="w", newline="", encoding="utf-8") as csvfile:
    fieldnames = SelectionCriteria.__annotations__.keys()  # Get field names from Pydantic model
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(candidates_list)

print(f"Candidate selection saved to {OUTPUT_CSV}")
