import os

from pydantic import BaseSettings

def return_full_path(filename: str = ".env") -> str:

	"""" Uses `os` to return the correct path of the `.env` file."""

	absolute_path = os.path.abspath(__file__)
	directory_name = os.path.dirname(absolute_path)
	full_path = os.path.join(directory_name, filename)

	return full_path
	

class Settings(BaseSettings):

	""" Uses pydantic to define settings for project """

	api_key: str
	db_name: str
	model_directory: str

	class Config:
		env_file = return_full_path(".env")


## Create instance of `Settings` class that will be imported
## in notebooks and the other modules of the project.

settings = Settings()