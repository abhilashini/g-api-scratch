import pathlib
import os
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

# Initialize Gemini client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 1️⃣ Upload the sheet music file (PDF, MusicXML, etc.)
file_path = pathlib.Path("/workspaces/g-api-scratch/idea01/inaccessible-toile.pdf")

uploaded_file = client.files.upload(file=file_path)

# 2️⃣ Extract musical features / understanding via Gemini
prompt_extract_features = """
You are an AI music tutor.
Analyze the uploaded sheet music for a beginner who cannot read music.
Return structured JSON including:
- notes (pitch, duration, time)
- tempo
- loudness/dynamics
- repeating motifs
Keep it concise and structured for downstream visualization.
"""

response_features = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[uploaded_file, prompt_extract_features],
)

music_features_text = ""
for part in response_features.candidates[0].content.parts:
    if part.text:
        music_features_text += part.text

print("=== Extracted Musical Features ===")
print(music_features_text)

# 3️⃣ Generate beginner-friendly description
prompt_description = f"""
You are an AI music tutor.
Given the following musical features:

{music_features_text}

Explain in simple, beginner-friendly terms:
- Rhythm and tempo
- Pitch motion (high/low)
- Emotions conveyed
- Repeating patterns or motifs

Keep it under 150 words.
"""

response_description = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=[prompt_description],
)

description_text = ""
for part in response_description.candidates[0].content.parts:
    if part.text:
        description_text += part.text

print("\n=== Beginner-Friendly Description ===")
print(description_text)

# 4️⃣ Generate abstract art visualization from features + description
prompt_art = f"""
Create an abstract art visualization of a music piece.
- Use high notes → tight spirals or peaks, bright colors
- Use low notes → gentle waves, darker blues
- Fast tempo → dense energetic patterns
- Slow tempo → spread-out, soft patterns
- Repeating motifs → repeated visual elements
The visualization should be linearly progressing (left to right) and interpretable.
Include the following description in your creative interpretation for guidance:

{description_text}
"""

glyph_score = f"""
A flat graphic visualization where each musical element is represented by geometric shapes. Circles = melody, triangles = harmony, squares = rhythm, stars = ornaments. Each shape is colored by pitch class (C=red, D=orange, etc.) and arranged horizontally by time. Include a minimal legend explaining shape and color mappings. Style it like an elegant Bauhaus-inspired infographic — balanced, geometric, clean vector design, subtle shadows and spacing. Refer {description_text} for guidance on building the visualization.
"""

styles = {"glyph": "glyph_score"}

# --- MODIFIED PART STARTS HERE ---

response_art_config = types.GenerateContentConfig(
    response_modalities=[types.Modality.IMAGE, types.Modality.TEXT] # Request both image and potentially text
)

response_art = client.models.generate_content(
    model="gemini-2.0-flash-exp-image-generation",
    contents=[glyph_score],
    config=response_art_config
)

# 5️⃣ Save generated image
try:
    # Assuming the image is returned in the first part's inline_data
    for part in response_art.candidates[0].content.parts:
        if part.inline_data:
            image = Image.open(BytesIO(part.inline_data.data))
            image.save(f"../images/{styles["glyph"]}.png")
            print(f"\nGenerated abstract music visualization saved as {styles["glyph"]}.png")
            break # Assuming only one image per part or first image is sufficient
    else:
        print("\nNo inline_data found in the image generation response. Image might not have been generated.")
        # If the model returns text instead of image data upon failure or for specific requests,
        # you might want to print that for debugging.
        for part in response_art.candidates[0].content.parts:
            if part.text:
                print(f"Model response text: {part.text}")

except Exception as e:
    print(f"\nError saving generated image: {e}")
    print("Full response from imagen-3.0-generate model (for debugging):")
    # This will attempt to print the entire response object if an error occurs
    # to help diagnose issues if the image data isn't where expected.
    print(response_art)
# --- MODIFIED PART ENDS HERE ---