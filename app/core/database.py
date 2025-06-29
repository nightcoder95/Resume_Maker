import motor.motor_asyncio
from beanie import init_beanie

# Import our settings object and the Resume document model
from app.core.config import settings
from app.models.resume import Resume # Important: Beanie needs to know about all our Document models

async def init_db():
    """
    Initializes the database connection and Beanie.
    This function will be called when the FastAPI application starts up.
    """
    print("Connecting to MongoDB...")
    
    # Create an asynchronous client to connect to MongoDB.
    # We use the DATABASE_URL from our settings.
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URL)

    # Get the specific database from the client instance.
    # We use the DATABASE_NAME from our settings.
    database = client[settings.DATABASE_NAME]

    # Initialize Beanie. This links our Pydantic-based models to MongoDB collections.
    # We pass the database instance and a list of all our Beanie 'Document' models.
    # Beanie will create the collections and necessary indexes if they don't exist.
    await init_beanie(
        database=database, 
        document_models=[Resume] # Add other document models here in the future
    )
    
    print("Successfully connected to MongoDB and initialized Beanie!")