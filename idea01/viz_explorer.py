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
	sheet_data_raw_string = f.read()
	sheet_data = json.loads(sheet_data_raw_string)

styles = {"glyph": "glyph_score", "landscape": "chromatic_landscape", "spiral": "harmonic_spiral", "constellation": "constellation_score", "watercolor": "watercolor_flow"}

response_art_config = types.GenerateContentConfig(
	response_modalities=[types.Modality.IMAGE, types.Modality.TEXT] # Request both image and potentially text
)

for name, prompt in GraphicScorePrompts.get_prompt_list():
	
	# 1. DYNAMICALLY EXTRACT KEY DATA FROM THE SHEET_DATA DICTIONARY
	try:
		data_summary = {
			"title": sheet_data.get("title", "The Music"),
			"key_mood": sheet_data.get("key_signature", "Neutral").split(" ")[0],
			"time_signature": sheet_data.get("time_signature", "N/A").split(" ")[0],
			"initial_tempo_desc": sheet_data.get("initial_tempo", {}).get("description", "A moderate pace"),
			"initial_tempo_term": sheet_data.get("initial_tempo", {}).get("description", "A moderate pace").split(" ")[0].strip("()"),
			"initial_dynamics_desc": sheet_data.get("initial_dynamics", {}).get("description", "Quiet"),
			"initial_dynamics_term": sheet_data.get("initial_dynamics", {}).get("level", "p"),
			"initial_articulation_term": sheet_data.get("initial_dynamics", {}).get("articulation", "smoothly"),
			"rhythm_highlight": sheet_data.get("repeating_motifs", [{}])[0].get("description", "A consistent, simple beat."),
		}
	except Exception as e:
		print(f"Error extracting data for narration: {e}")
		continue # Skip this loop if data extraction fails
		
	# 2. ASSEMBLE THE NARRATION PROMPT
	narration_prompt_text = f"""
	Based on the following musical summary for '{data_summary['title']}' 
	and the visual style described in the visualization prompt below, create a unique, 
	creative, and helpful narration (maximum 70 words) for a beginner/non-musician/deaf user. 
	
	The narration MUST include a beginner-friendly description of the music's highlight 
	(the steady rhythm) and key features (starting speed and softness). 
	
	IMPORTANT: Include the exact technical musical term in parentheses (e.g., 'soft (p)') 
	next to its beginner-friendly description, using the terms provided in the summary.
	
	--- MUSIC SUMMARY ---
	Style: {data_summary['key_mood']} Key, {data_summary['time_signature']} time.
	Start: {data_summary['initial_tempo_desc']} ({data_summary['initial_tempo_term']}), {data_summary['initial_dynamics_desc']} ({data_summary['initial_dynamics_term']}), {data_summary['initial_articulation_term']} texture.
	Highlight: {data_summary['rhythm_highlight']}
	
	--- VISUALIZATION PROMPT STYLE ---
	{prompt.format(json_string=sheet_data)}
	"""
	
	# 3. Call the text model for narration
	try:
		response_narration = client.models.generate_content(
			model="gemini-2.5-flash", 
			contents=[narration_prompt_text]
		)
		narration = response_narration.text.strip()
	except Exception as e:
		narration = f"[Error generating narration: {e}]"
		
	print(f"\n--- Visualization: {name} ---")
	print(f"NARRATION: {narration}")
	
	# 4. Prepare JSON sheet data string for the image model (must be a string)
	sheet_data_string = json.dumps(sheet_data)

	# 5. GENERATE IMAGE
	try:
		response_art = client.models.generate_content(
			model="gemini-2.0-flash-exp-image-generation",
			contents=[prompt.format(json_string=sheet_data_string)], 
			config=response_art_config
		)

		# 6. SAVE IMAGE
		for part in response_art.candidates[0].content.parts:
			if part.inline_data:
				image = Image.open(BytesIO(part.inline_data.data))
				image.save(f"/workspaces/g-api-scratch/idea01/images/{name}.png")
				print(f"STATUS: Image saved as {name}.png")
				break 
		else:
			print("STATUS: No image data found in the response.")

	except Exception as e:
		print(f"ERROR: Failed to generate or save image for {name}: {e}")
		print(f"Full response for debugging: {response_art}")