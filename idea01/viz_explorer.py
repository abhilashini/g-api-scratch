import pathlib
import os
import traceback
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

CONSISTENCY_DISCLAIMER = (
	"\n"
	"=========================================================\n"
	"💡 **VISUALIZATION CONSISTENCY NOTE**\n"
	"While the visual structure (e.g., wave height, dot size, color mapping) is **strictly and quantitatively derived** "
	"from the musical data, image generation models retain an inherent artistic variability. "
	"Therefore, the exact perspective, lighting, texture, and style of this visualization may differ slightly "
	"from one run to the next, even with the same music file. The core musical information remains constant.\n"
	"========================================================="
)

response_art_config = types.GenerateContentConfig(
	response_modalities=[types.Modality.IMAGE, types.Modality.TEXT] # Request both image and potentially text
)

for name, prompt in GraphicScorePrompts.get_prompt_list():
	
	# 2a. DYNAMICALLY EXTRACT KEY DATA FOR NARRATION
		try:
			# Safely extract data for narration, using generic keys
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
			# Use traceback for descriptive error printing if data access fails unexpectedly
			print(f"\n--- ERROR in Data Extraction for {name} ---")
			print(f"FAILED to extract data using dictionary access: {e}")
			print("Traceback:\n" + traceback.format_exc())
			continue # Skip visualization for this prompt
			
		# 2b. ASSEMBLE GENERIC NARRATION PROMPT
		narration_prompt_text = f"""
		Based on the following musical summary for '{data_summary['title']}' 
		and the visual style described in the visualization prompt below, create a unique, 
		creative, and helpful narration (maximum 70 words) for a beginner/non-musician/deaf user. 
		
		The narration MUST use language that emphasizes the STRUCTURAL MAPPING (e.g., 'The waves rise and fall with the pitch contour...') rather than just emotional flair.
		
		IMPORTANT: Include the exact technical musical term in parentheses (e.g., 'soft (p)') 
		next to its beginner-friendly description, using the terms provided in the summary.
		
		--- MUSIC SUMMARY ---
		Style: {data_summary['key_mood']} Key, {data_summary['time_signature']} time.
		Start: {data_summary['initial_tempo_desc']} ({data_summary['initial_tempo_term']}), {data_summary['initial_dynamics_desc']} ({data_summary['initial_dynamics_term']}), {data_summary['initial_articulation_term']} texture.
		Highlight: {data_summary['rhythm_highlight']}
		
		--- VISUALIZATION PROMPT STYLE ---
		{prompt.format(json_string='[... music data is mapped here to the visualization rules specified in the prompt ...]')}
		"""
		
		# 2c. Call the text model for narration
		try:
			response_narration = client.models.generate_content(
				model="gemini-2.5-flash", 
				contents=[narration_prompt_text]
			)
			narration = response_narration.text.strip()
		except Exception as e:
			narration = f"[Error generating narration from API: {e}]"
			
		print(f"\n=======================================================")
		print(f"--- Visualization: {name} ---")
		print(f"NARRATION: {narration}")
		
		# 2d. GENERATE IMAGE (using the raw JSON string)
		try:
			response_art = client.models.generate_content(
				model="gemini-2.0-flash-exp-image-generation",
				contents=[prompt.format(json_string=sheet_data_raw_string)], 
				config=response_art_config
			)

			# 2e. SAVE IMAGE
			image_saved = False
			for part in response_art.candidates[0].content.parts:
				if part.inline_data:
					image = Image.open(BytesIO(part.inline_data.data))
					image_filename = f"/workspaces/g-api-scratch/idea01/images/{name}.png"
					image.save(image_filename)
					print(f"STATUS: Image saved as {image_filename}")
					image_saved = True
					break 
			
			if not image_saved:
				 print("STATUS: No image data found in the response.")

		except Exception as e:
			print(f"ERROR: Failed to generate or save image for {name}: {e}")
		
# 2f. PRINT SINGLE-BLOCK DISCLAIMER
print(CONSISTENCY_DISCLAIMER)