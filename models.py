from typing import List
from pydantic import BaseModel, Field

class Candidate(BaseModel):
    first_last_name: str = Field(description="The candidate's name in this format: Last, First Name")
    phone_number: str = Field(description="Phone number")
    email: str = Field(description="Email address")
    # skills: List[str] = Field(description="List of skills mentioned in the resume")
    # experience_years: int = Field(description="Number of years of professional experience")
    # education: str = Field(description="Highest level of education attained")
    # previous_companies: List[str] = Field(description="List of previous companies worked at")
    # linkedin_url: str = Field(description="LinkedIn profile URL")
    # github_url: str = Field(description="GitHub profile URL")
    
    class Config:
        extra = "forbid"

class Filters(BaseModel):
    experience: bool = Field(description="does the candidate have 5+ years of professional software development experience.")
    degree: bool = Field(description="does the candidate have a Bachelor's degree in computer science or related field (or equivalent experience)")
    
    class Config:
        extra = "forbid"

fluffernutter = """
Fluff refers to unnecessary or overly verbose content in a resume that does not add meaningful value or context. 
This can include excessive jargon, filler phrases, or irrelevant information that distracts from the candidate's qualifications.
This also includes buzzwords or clichés that do not provide concrete evidence of skills or achievements.
Examples of fluff include:
- Using vague terms like "hardworking" or "team player" without specific examples.
- Including long lists of skills without context or demonstration of proficiency.
- Overly detailed descriptions of minor tasks that do not highlight significant accomplishments.
- Repetitive information that does not contribute new insights about the candidate's abilities or experience.
A resume with minimal fluff is concise, focused, and highlights the candidate's key qualifications and achievements effectively.
"""

class FluffAnalysis(BaseModel):
    fluff_level: str = Field(description=f"Overall fluff level: no fluff, some fluff, lots of fluff --based on the following definition: {fluffernutter.strip()}")
    fluff_analysis: str = Field(description="Detailed analysis of fluff in the resume")

    class Config:
        extra = "forbid"

class FitmentScore(BaseModel):
    fitment_score: int = Field(description="Fitment score from no fit, some fit, to full fit based on how well the candidate's experience and skills match the job description")
    fitment_analysis: str = Field(description="Detailed analysis of the candidate's fitment for the role")

    class Config:
        extra = "forbid"

class ShouldInterview(BaseModel):
    should_interview: str = Field(description="Decision on whether the candidate should be interviewed: from yes, to meh, to no")
    interview_analysis: str = Field(description="Detailed analysis supporting the interview decision")

    class Config:
        extra = "forbid"

responsibilities = """
•	Design and develop new applications and features.
•	Maintain and enhance legacy applications.
•	Collaborate with business and technical teams to align solutions with requirements.
•	Perform testing, debugging, and performance tuning.
•	Deliver high-quality code using established standards, patterns, and practices.
"""

class Responsibilities(BaseModel):
    responsibilities_score: int = Field(description=f"Score from 1-5 on how well the candidate's experience matches the job responsibilities: {responsibilities.strip()}")
    responsibilities_analysis: str = Field(description=f"Detailed analysis of how the candidate's experience aligns with the job responsibilities: {responsibilities.strip()}")

    class Config:
        extra = "forbid"

required_skills = """
•	Bachelor’s degree in computer science or related field (or equivalent experience).
•	5+ years of professional development experience.
•	Full-stack experience with:
o	Backend: ASP.NET Core (.NET 8+), C#, EF Core
o	Frontend: Angular 18+, TypeScript, JavaScript, HTML, CSS
o	Database: SQL Server (T-SQL, schema design, performance tuning)
•	Experience with Git and CI/CD pipelines.
•	Strong understanding of web application architecture, SOLID principles, TDD, and DDD.
•	Excellent problem-solving, communication, and collaboration skills.
"""

class RequiredSkills(BaseModel):
    required_skills_score: int = Field(description=f"Score from 1-5 on how well the candidate's skills aligns with the required skills: {required_skills.strip()}")
    required_skills_analysis: str = Field(description=f"Detailed analysis of how the candidate's skills aligns with the required skills: {required_skills.strip()}")

    class Config:
        extra = "forbid"

preferred_skills = """
•	Exposure to or interest in Machine Learning / AI.
o	Experience integrating LLM-based solutions for document analysis, search, or automation.
o	Familiarity with vector databases, embeddings, or retrieval-augmented generation
•	Oil & Gas or land administration industry experience.
•	Master’s degree in computer science or related field.
"""

class PreferredSkills(BaseModel):
    preferred_skills_score: int = Field(description=f"Score from 1-5 on how well the candidate's skills matches the preferred skills: {preferred_skills.strip()}")
    preferred_skills_analysis: str = Field(description=f"Detailed analysis of how the candidate's skills aligns with the preferred skills: {preferred_skills.strip()}")

    class Config:
        extra = "forbid"

technical_environment = """
•	Architecture: Modular Monolith, Clean Architecture, Domain-Driven Design
•	Frameworks: .NET 8, ASP.NET Core MVC, MediatR, Ardalis Specifications
•	Frontend: Angular 18+ with Bootstrap 4 or 5
•	Database: SQL Server 2019+ (including JSON and graph features)
•	DevOps: Azure DevOps, Git, CI/CD pipelines
•	Hosting: On-prem IIS and SQL Server
•	Other Tools: Serilog structured logging, Power BI integration, Gulp asset pipeline
"""

class TechnicalEnvironment(BaseModel):
    technical_environment_score: int = Field(description=f"Score from 1-5 on how well the candidate's experience matches the technical environment: {technical_environment.strip()}")
    technical_environment_analysis: str = Field(description=f"Detailed analysis of how the candidate's experience aligns with the technical environment: {technical_environment.strip()}")

    class Config:
        extra = "forbid"

working_conditions = """
•	Work performed in a hybrid environment with company equipment.
•	Candidates required to work onsite at least 2 days per week
"""

class WorkingConditions(BaseModel):
    working_conditions_score: int = Field(description=f"Score from 1-5 on how well the candidate's experience matches the working conditions: {working_conditions.strip()}")
    working_conditions_analysis: str = Field(description=f"Detailed analysis of how the candidate's experience aligns with the working conditions: {working_conditions.strip()}")

    class Config:
        extra = "forbid"