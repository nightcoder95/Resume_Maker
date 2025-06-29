from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from beanie import Document
from datetime import datetime
import uuid

class ContactInfo(BaseModel):
    """
    Model for the user's contact information.
    This will be an embedded object within the main Resume model.
    """
    # The '...' indicates that this field is required.
    full_name: str = Field(..., description="The user's full name.", min_length=1)
    # EmailStr ensures the string is a valid email.
    email: EmailStr = Field(..., description="The user's email address.")
    phone: Optional[str] = Field(None, description="The user's phone number.")
    linkedin_url: Optional[str] = Field(None, description="URL to the user's LinkedIn profile.")
    portfolio_url: Optional[str] = Field(None, description="URL to the user's personal portfolio or website.")


class Experience(BaseModel):
    """
    Model for a single job or work experience entry.
    """
    position: str = Field(..., description="The job title or position.")
    company: str = Field(..., description="The name of the company.")
    start_date: str = Field(..., description="When the user started this role.")
    end_date: Optional[str] = Field("Present", description="When the user left this role. 'Present' if current.")
    # A list of strings to describe responsibilities and achievements.
    responsibilities: List[str] = Field(..., description="A list of key responsibilities and accomplishments.")


class Education(BaseModel):
    """
    Model for a single education entry.
    """
    institution: str = Field(..., description="The name of the institution.")
    degree: str = Field(..., description="The degree or qualification obtained.")
    field_of_study: str = Field(..., description="The field of study.")
    graduation_year: Optional[int] = Field(None, description="The year of graduation.")

class Skill(BaseModel):
    """
    Model for a single skill.
    """
    name: str = Field(..., description="The name of the skill (e.g., Python, Project Management).")
    level: Optional[str] = Field(None, description="Proficiency level (e.g., Expert, Intermediate).")



# --- Main Schema for API interaction ---
# This is the model that our API endpoints will use to receive and send data.

class ResumeSchema(BaseModel):
    """
    The main schema for a resume. This defines the structure that API clients will interact with.
    """
    contact_info: ContactInfo = Field(..., description="User's contact details.")
    summary: str = Field(..., description="A professional summary or objective statement.")
    experience: List[Experience] = Field(..., description="A list of work experiences.")
    education: List[Education] = Field(..., description="A list of educational qualifications.")
    skills: List[Skill] = Field(..., description="A list of relevant skills.")

# --- Database Document Model ---
# This is the model that Beanie will use to store data in MongoDB.

class Resume(Document, ResumeSchema):
    """
    This is the model that represents a document in the MongoDB 'resumes' collection.
    It inherits all the fields from ResumeSchema.
    The 'Document' class from Beanie adds MongoDB-specific functionality.
    """
    # We add database-specific fields here.
    user_id: str = Field(..., description="The ID of the user who owns this resume.")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        # This tells Beanie which MongoDB collection to use for this model.
        name = "resumes"