from google import genai
from google.genai import types
import io
import httpx
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

long_context_pdf_path = "https://www.nasa.gov/wp-content/uploads/static/history/alsj/a17/A17_FlightPlan.pdf"

# Retrieve and upload the PDF using the File API
doc_io = io.BytesIO(httpx.get(long_context_pdf_path).content)

sample_doc = client.files.upload(
  # You can pass a path or a file-like object here
  file=doc_io,
  config=dict(
    mime_type='application/pdf')
)

prompt = "Summarize this document"

response = client.models.generate_content(
  model="gemini-2.5-flash",
  contents=[sample_doc, prompt])
print(response.text)