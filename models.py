from typing import List
from pydantic import BaseModel, Field

class SelectionCriteria(BaseModel):
    first_last_name: str = Field(description="The candidate's name in this format: Last, First Name")
    phone_number: str = Field(description="Phone number")
    email: str = Field(description="Email address")
    years_experience: int = Field(description="Years of experience in ML, NLP, or data science (0-10)")
    ml_experience: List[str] = Field(description="List of ML models the candidate has experience with (e.g., classifiers, NER, LLMs)")
    pdf_processing_experience: bool = Field(description="Whether the candidate has experience extracting structured data from PDFs")
    programming_languages: List[str] = Field(description="Programming languages the candidate is proficient in")
    framework_experience: List[str] = Field(description="List of ML/NLP frameworks the candidate has used (e.g., TensorFlow, PyTorch, spaCy, Hugging Face)")
    vector_database_experience: bool = Field(description="Whether the candidate has experience using vector databases like pgvector, FAISS, or Pinecone")
    past_projects: List[str] = Field(description="List of past projects related to ML/NLP that the candidate has worked on")
    
    fluff_level: str = Field(
        description='''Assess how much 'fluff' is in the candidate's resume based on their level of detail. Fluff refers to vague or exaggerated claims without real substance.
                    Examples: 'Developed ML models' (no details): fluff, 'Built a classifier using TensorFlow' (some details): some fluff , 'Trained a BERT model for NER using PyTorch' (specific details): no fluff
                    Options: 'no fluff' (specific details showing actual knowledge),
                    'some fluff' (mentions skills but lacks depth or examples),
                    'lots of fluff' (claims skills but provides little to no evidence of real knowledge)'''
    )
    
    fluff_analysis: str = Field(
        description="Detailed notes on where fluff appears in the resume, including vague descriptions, missing technical details, or exaggerated claims."
    )

    fitment_score: int = Field(
        description='''Score candidate from good fit, medium fit, poor fit based on how well the candidate's experience and skills match this job description:
                    projects involving NLP, ML model development, and integration of Python APIs Angular and C#
                    As an intern, you will:
                    Curate and preprocess training data for ML models, including Named Entity Recognition (NER) and Classification tasks
                    Train, tune, and evaluate machine learning models
                    Develop Python code to interact with LLM APIs (e.g., Azure OpenAI and Ollama)
                    Create and maintain web APIs using Flask or WSGI
                    Integrate ML and API functionalities into C# and Angular-based applications'''
                    
    )

    should_interview: str = Field(
        description='''Decision on whether the candidate should be interviewed based on skills, fitment score, and fluff level.
                    Options: 'interview' (high skills, minimal fluff, good fitment score),
                    'maybe' (some skills, moderate fluff, average fitment score),
                    'no' (low skills, excessive fluff, poor fitment score)'''
    )
    
    class Config:
        extra = "forbid"
