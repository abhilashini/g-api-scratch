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
A **flat, minimalist infographic visualization** of music, rendered as a striking, **Bauhaus-inspired abstract composition**. The image features a clean, light grey or off-white background with a subtle grid. Musical elements are represented by **distinct geometric shapes:**
- **Circles** (crisp, solid fill) signify **melody**.
- **Triangles** (pointed upwards, solid fill) represent **harmony/accompaniment**.
- **Squares** (solid fill) denote **rhythm section elements**.
- **Stars** (small, five-pointed, slightly glowing) mark **accents or ornaments**.

Each shape's **color indicates its pitch class** according to a clear, intuitive spectrum (e.g., C=vibrant red, D=bright orange, E=sunny yellow, F=emerald green, G=sky blue, A=indigo, B=violet). The shapes are precisely **arranged horizontally from left to right to represent time progression**, with consistent spacing for beats and measures. Vertical alignment indicates relative pitch within its category (e.g., higher circles for higher melodic notes).

The overall composition should be **balanced, harmonious, and highly geometric**, evoking a sense of structured elegance. Use **clean vector lines, subtle drop shadows** for depth, and precise negative space. The shapes should appear as if floating on the canvas.

A **small, unobtrusive legend panel** is integrated into one corner (e.g., bottom left), clearly showing:
- A key of geometric shapes with their corresponding musical roles (Circle → Melody, Triangle → Harmony, etc.).
- A chromatic scale with its corresponding color mapping (C → Red, D → Orange, etc.).

The final image should be a **polished, high-resolution visual explainer**, combining information design with a sophisticated, timeless art aesthetic. Refer {json_string} for guidance on building the visualization, particularly for extracting motifs, dynamics, and pitch class mapping to colors and shape recurrence.
"""

chromatic_landscape = f"""
A **breathtaking, cinematic 3D generative landscape visualization** of music. The terrain undulates organically, resembling a majestic **mountain range sculpted from sound waves**.

- The **X-axis** spans the entire horizontal width, representing the **linear progression of time** through the musical piece.
- The **Y-axis** (depth into the image, front to back) subtly indicates **pitch**, with lower pitches appearing closer to the viewer and higher pitches receding slightly into the distance.
- The **Z-axis** (vertical height of the terrain) directly corresponds to **amplitude or dynamic level**, with towering peaks signifying loud, impactful sections and deep, serene valleys representing soft, subdued passages.

The entire landscape is rendered with a **glowing wireframe effect** or a **softly shaded, iridescent surface**. The **colors of the terrain shift based on implied instrument groups or overall harmonic mood**:
- **Cool hues** (deep blues, serene aquamarines, mystical purples) for smooth, legato sections or underlying harmonic support.
- **Warm accents** (fiery oranges, vibrant reds, golden yellows) for moments of strong rhythmic emphasis or brass-like textures.
- **Bright, sparkling highlights** (electric greens, crisp whites) for sharp percussive attacks or high-pitched, piercing melodic lines.

**Dramatic, realistic lighting** casts long shadows into valleys and bathes peaks in luminous glows, emphasizing the contours and emotional intensity. **Gentle, ethereal fog or mist** drifts through the lower valleys, adding depth and a sense of mystery, subtly reflecting the quieter dynamics.

A **minimalist, frosted glass or holographic inset legend** is positioned in a corner (e.g., top right), clearly explaining:
- The mapping of axes (X=Time, Y=Pitch, Z=Amplitude).
- The color scheme (e.g., Cool=Smooth, Warm=Impact, Bright=Accent).

The final output is a **high-detail, immersive visual experience**, like an art installation where the viewer "flies over" the musical composition, feeling its peaks and valleys. Refer {json_string} for guidance on building the visualization, especially for interpreting tempo, dynamics, and pitch ranges for terrain generation.
"""

harmonic_spiral = f"""
A **mesmerizing, elegant, and futuristic circular spiral visualization** of music, aesthetically resembling a **chromatic nautilus shell or an ancient celestial clock**.

- The central point is the beginning of the piece. The **spiral path expands gracefully outward from the center, representing the linear progression of time**.
- The **angular position** along the spiral (like hours on a clock face) consistently **encodes pitch class** (e.g., C at 12 o'clock, C# at 1 o'clock, D at 2 o'clock, wrapping chromatically).
- The **radius** from the center strictly corresponds to the **passage of time**, so earlier events are closer to the core, and later events are further out.
- **Tonal families or harmonic centers are conveyed by a subtle, evolving color gradient** that washes over the spiral and its background (e.g., a warm golden glow for F Major, transitioning to a cooler, introspective blue for a minor section).

**Each distinct musical thread (melody, harmony, bass)** is represented by a **thick, luminous, glowing line** that traces its unique path along the spiral. When harmonies occur, these lines converge or align radially, forming visually striking **"harmonic spokes" or "choral clusters"** that pulse with the musical moment.

The background is a **soft, radial gradient** that deepens from the center outward, enhancing the sense of depth and cosmic elegance. The entire composition embodies **perfect symmetry, high detail, and a sense of serene, organized complexity**.

A **subtle, integrated legend** (e.g., a translucent ring or a small panel) explains:
- The color mapping to tonal family.
- The angular position to pitch class.
- The radial expansion to time.

The final image should be a **high-resolution infographic art piece**, both scientifically precise in its data representation and beautifully poetic in its aesthetic. Refer {json_string} for guidance on building the visualization, specifically for interpreting time signatures, key signatures, and repeating motifs as patterns within the spiral.
"""

constellation_score = f"""
A breathtaking **cosmic data-art visualization** transforming sheet music into an **expansive, ethereal constellation map** set against a deep, dark starry night sky.

- **Each individual musical note is represented as a glowing, colored dot (a 'star')**.
- Its **vertical position (Y-axis)** on the canvas precisely determines its **pitch** (higher notes are higher up).
- **Time flows linearly from left to right (X-axis)** across the vast celestial expanse, mapping the musical timeline.
- The **size (radius) of each star's circle** is directly proportional to the note's **duration** (longer notes are larger stars).
- The **intensity of the star's glow** corresponds to the note's **dynamics/volume** (louder notes glow more brightly and expand their aura).

The **color of each star maps to its note family (pitch class)**, creating a visually distinct spectrum (e.g., C=vibrant red, D=sun-orange, E=lemon-yellow, F=forest-green, G=sky-blue, A=deep-indigo, B=royal-violet).

The background is a **dark navy or deep space black**, subtly overlaid with **fine, barely visible grid lines** to orient the viewer by measure and beat. **Thin, shimmering trails of stardust** gracefully connect consecutive notes, forming clear melodic pathways and highlighting the flow of the music. When **chords** occur, multiple stars align vertically at the same X-axis position, forming vibrant, momentary **star clusters**. **Repeating motifs** are visibly discernible as **recurring constellations or star patterns** that reappear across the map.

A **neat, minimalist corner legend** (e.g., top-left, rendered as translucent data overlay) clearly indicates:
- A chromatic scale of note colors (Color → Pitch).
- A visual example of dot sizes for different durations (Size → Duration).
- A gradient showing glow intensity for dynamics (Glow → Dynamics).

The final image should be **high-resolution, beautifully balanced, and emotionally evocative**—a scientific yet profoundly poetic visual translation of music. Refer {json_string} for guidance on building the visualization, especially for mapping individual notes, their pitches, durations, and dynamics to star properties.
"""

watercolor_flow = f"""
A flowing watercolor visualization of music represented as liquid brush strokes. Each stroke’s direction encodes pitch movement, color saturation encodes volume, opacity represents sustain, and flow direction corresponds to tempo. Major keys use warm tones, minor keys cool tones. The piece should evoke emotional energy rather than technical structure, resembling abstract watercolor art with motion and rhythm. Include a small artistic legend with brush samples explaining mappings. Painterly, expressive, high-resolution. Refer {json_string} for guidance on building the visualization, especially for mapping individual notes, their pitches, durations, and dynamics to star properties.
"""

styles = {"glyph": "glyph_score", "landscape": "chromatic_landscape", "spiral": "harmonic_spiral", "constellation": "constellation_score", "watercolor": "watercolor_flow"}

response_art_config = types.GenerateContentConfig(
    response_modalities=[types.Modality.IMAGE, types.Modality.TEXT] # Request both image and potentially text
)

for style in list(styles.keys())[-1:]:
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