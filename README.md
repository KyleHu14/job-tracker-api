# Instructions for Starting the Project

1. Start the venv by running the command "./venv/Scripts/activate"

2. Run the command "uvicorn app.main:app"

  

# Structure of Project

	app # App : Root Folder
	├── models # Models : Contains the pydantic schemas used in its respective routes file
	│ └── job_app.py
	├── api # API : Contains all files API related
	│ └── routes # Routes : Contains all API routes that are registered in main.py
	│ └── job_app.py
	├── __init__.py
	└── main.py
	
# Documentation
## Job App 
### GET /jobapp
Returns a list of job applications. Each job application is represented by an object with the following string fields : "id", "title", "company_name", "location", "status", "date", "user_email", "link".