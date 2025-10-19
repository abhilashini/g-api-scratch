import pathlib
import os
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import json
from viz_graphics_prompts import GraphicScorePrompts

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

with open("/workspaces/g-api-scratch/idea01/inaccessible-toile.json", 'r', encoding='utf-8') as f:
	sheet_data = f.read()

styles = {"glyph": "glyph_score", "landscape": "chromatic_landscape", "spiral": "harmonic_spiral", "constellation": "constellation_score", "watercolor": "watercolor_flow"}

response_art_config = types.GenerateContentConfig(
	response_modalities=[types.Modality.IMAGE, types.Modality.TEXT] # Request both image and potentially text
)

for name, prompt in GraphicScorePrompts.get_prompt_list():
	
	response_art = client.models.generate_content(
		model="gemini-2.0-flash-exp-image-generation",
		contents=[prompt.format(json_string=sheet_data)],
		config=response_art_config
	)

	try:
		for part in response_art.candidates[0].content.parts:
			if part.inline_data:
				image = Image.open(BytesIO(part.inline_data.data))
				image.save(f"/workspaces/g-api-scratch/idea01/images/{name}.png")
				print(f"\nGenerated abstract music visualization saved as {name}.png")
				break # Assuming only one image per part or first image is sufficient
		else:
			print("\nNo inline_data found in the image generation response. Image might not have been generated.")
			for part in response_art.candidates[0].content.parts:
				if part.text:
					print(f"Model response text: {part.text}")

	except Exception as e:
		print(f"\nError saving generated image: {e}")
		print("Full response from imagen-3.0-generate model (for debugging):")
		print(response_art)