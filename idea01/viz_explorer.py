import pathlib
import os
from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import json

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

with open("/workspaces/g-api-scratch/idea01/inaccessible-toile.json", 'r', encoding='utf-8') as f:
	json_string = f.read()


glyph_score = f"""
A flat graphic visualization where each musical element is represented by geometric shapes. Circles = melody, triangles = harmony, squares = rhythm, stars = ornaments. Each shape is colored by pitch class (C=red, D=orange, etc.) and arranged horizontally by time. Include a minimal legend explaining shape and color mappings. Style it like an elegant Bauhaus-inspired infographic — balanced, geometric, clean vector design, subtle shadows and spacing. Refer {json_string} for guidance on building the visualization.
"""

chromatic_landscape = f"""
A 3D generative terrain representing music as a flowing landscape. The X-axis shows time, Y-axis shows pitch, and height shows amplitude or volume. Use a glowing wireframe or softly shaded surface colored by instrument groups — cool hues for strings, warm for brass, bright for percussion. Add gentle fog and lighting for depth, and a small inset legend explaining axes and color meanings. The result should look like a mountain range made of sound waves. High-detail, cinematic, realistic lighting. Refer {json_string} for guidance on building the visualization.
"""

harmonic_spiral = f"""
A circular spiral visualization of music resembling a chromatic nautilus shell. The spiral expands outward, representing time radiating from the center. Angular position encodes pitch class, radius encodes time, and color encodes tonal family. Thick glowing lines trace each musical thread. Include a soft circular gradient background, luminous threads, and a subtle legend explaining color, pitch, and time mapping. Elegant, futuristic, symmetric, high-detail infographic art. Refer {json_string} for guidance on building the visualization.
"""

constellation_score = f"""
A cosmic data-art visualization representing sheet music as a constellation map in a starry night sky. Each musical note is a glowing colored dot; pitch determines vertical position, time flows left to right, duration determines circle size, and dynamics determine glow intensity. Use a dark navy background with subtle grid lines and thin trails connecting notes. Add a neat corner legend showing color → pitch, size → duration, glow → dynamics. Ethereal, high-resolution, balanced composition, scientific yet poetic. Refer {json_string} for guidance on building the visualization.
"""

styles = {"glyph": "glyph_score", "landscape": "chromatic_landscape", "spiral": "harmonic_spiral", "constellation": "constellation_score"}

response_art_config = types.GenerateContentConfig(
    response_modalities=[types.Modality.IMAGE, types.Modality.TEXT] # Request both image and potentially text
)

for style in styles:
	response_art = client.models.generate_content(
		model="gemini-2.0-flash-exp-image-generation",
		contents=[styles[style]],
		config=response_art_config
	)

	try:
		for part in response_art.candidates[0].content.parts:
			if part.inline_data:
				image = Image.open(BytesIO(part.inline_data.data))
				image.save(f"/workspaces/g-api-scratch/idea01/images/{styles[style]}.png")
				print(f"\nGenerated abstract music visualization saved as {styles[style]}.png")
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