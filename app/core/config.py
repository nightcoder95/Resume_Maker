from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    A class to hold all the application settings.
    It inherits from Pydantic's BaseSettings, which can automatically
    read variables from the environment or a .env file.
    """
    # The name of the database to use in MongoDB.
    DATABASE_NAME: str = "resume_app_db"
    
    # The full connection string for the MongoDB database.
    # Pydantic will look for an environment variable named 'DATABASE_URL'
    # to populate this field.
    DATABASE_URL: str

    # This nested class tells Pydantic-Settings to look for a .env file
    # in the project's root directory.
    model_config = SettingsConfigDict(env_file=".env")


# Create a single, reusable instance of the Settings class.
# When any other part of our app needs a setting, they can import this `settings` object.
settings = Settings()
