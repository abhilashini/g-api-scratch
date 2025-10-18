from google import genai
from google.genai import types
import httpx
import pathlib
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Retrieve and encode the PDF byte
file_path = pathlib.Path("/workspaces/g-api-scratch/idea01/inaccessible-toile.pdf")

# Upload the PDF using the File API
sample_file = client.files.upload(
  file=file_path,
)

prompt_basic = "Summarize this document"
prompt_test = "You are an expert musician. I am a novice. Can you help me understand the attached score and what the notes mean?"
prompt_further = "You are an expert musician. I don't know music. Help me understand what this sheet music is doing and how I can familiarise myself with it."
prompt_translate = "Can you give carnatic music notes for this sheet music?"

response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[sample_file, prompt_translate])
print(response.text)