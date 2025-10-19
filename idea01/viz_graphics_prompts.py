class GraphicScorePrompts:
	"""
	A class containing highly descriptive prompt templates for generating
	various experimental and graphic music score visualizations.

	Each attribute corresponds to a unique visualization style, using f-strings
	to allow a `json_string` (placeholder for musical data) to be embedded
	when the prompt is used.
	"""

	# Placeholder for musical data reference (replace with actual data string when using)
	json_string = "... music data structure ..."

	# --- 1. The Glyph Score (Bauhaus Infographic) ---
	glyph_score = f"""
A **flat, minimalist infographic visualization** of music, rendered as a striking, **Bauhaus-inspired abstract composition**. The image features a clean, light grey or off-white background with a subtle grid. Musical elements are represented by **distinct geometric shapes:**
- **Circles** (crisp, solid fill) signify **melody**.
- **Triangles** (pointed upwards, solid fill) represent **harmony/accompaniment**.
- **Squares** (solid fill) denote **rhythm section elements**.
- **Stars** (small, five-pointed, slightly glowing) mark **accents or ornaments**.

Each shape's **color indicates its pitch class** according to a clear, intuitive spectrum (e.g., C=vibrant red, D=bright orange, E=sunny yellow, etc.). The shapes are precisely **arranged horizontally from left to right to represent time progression**, with consistent spacing for beats and measures. Vertical alignment indicates relative pitch within its category.

The entire composition is **balanced, harmonious, and highly geometric**. Use **clean vector lines, subtle drop shadows** for depth, and precise negative space.

A **small, unobtrusive legend panel** is integrated, clearly showing the shape → role and color → pitch mappings. The final image should be a **polished, high-resolution visual explainer**. Refer {json_string} for guidance on building the visualization.
"""

	# --- 2. The Chromatic Landscape (3D Terrain) ---
	chromatic_landscape = f"""
A **breathtaking, cinematic 3D generative landscape visualization** of music. The terrain undulates organically, resembling a majestic **mountain range sculpted from sound waves**.
- The **X-axis** is **time**.
- The **Y-axis** (depth) subtly indicates **pitch**.
- The **Z-axis** (vertical height of the terrain) corresponds to **amplitude or dynamic level**, with towering peaks signifying loud sections.

The landscape is rendered with a **glowing wireframe effect** or a **softly shaded, iridescent surface**. **Colors shift based on instrument groups or mood**: Cool hues (deep blues, aquamarines) for legato/harmony; Warm accents (oranges, golds) for rhythmic emphasis/brass.

**Dramatic, realistic lighting** casts long shadows. **Gentle, ethereal fog or mist** drifts through the lower valleys, adding depth and reflecting quiet dynamics.

A **minimalist, holographic inset legend** explains the axis and color mappings. The final output is a **high-detail, immersive visual experience**. Refer {json_string} for guidance on building the visualization.
"""

	# --- 3. The Harmonic Spiral (Nautilus Shell) ---
	harmonic_spiral = f"""
A **mesmerizing, elegant, and futuristic circular spiral visualization** of music, aesthetically resembling a **chromatic nautilus shell or a celestial clock**.
- The **spiral path expands gracefully outward from the center, representing time progression**.
- The **angular position** (like a clock face) consistently **encodes pitch class**.
- **Tonal families or harmonic centers are conveyed by a subtle, evolving color gradient** that washes over the spiral (e.g., warm golden glow for Major, cool blue for minor).

**Each distinct musical thread** is represented by a **thick, luminous, glowing line** that traces its unique path. When harmonies occur, these lines converge or align radially, forming visually striking **"harmonic spokes" or "choral clusters"**.

The background is a **soft, radial gradient**. The entire composition embodies **perfect symmetry, high detail, and organized complexity**. A **subtle, integrated legend** explains the mappings. Refer {json_string} for guidance on building the visualization.
"""

	# --- 4. The Constellation Score (Cosmic Map) ---
	constellation_score = f"""
A breathtaking **cosmic data-art visualization** transforming sheet music into an **expansive, ethereal constellation map** set against a deep, dark starry night sky.
- **Each musical note is a glowing colored dot ('star')**.
- Its **vertical position (Y-axis)** determines its **pitch**.
- **Time flows linearly from left to right (X-axis)**.
- The **size (radius) of each star** is proportional to the note's **duration**.
- The **intensity of the star's glow** corresponds to the note's **dynamics/volume**.

The **color of each star maps to its note family (pitch class)**. **Thin, shimmering trails of stardust** gracefully connect consecutive notes, forming clear melodic pathways. **Chords** form vibrant, momentary **star clusters**.

A **neat, minimalist corner legend** indicates color → pitch, size → duration, and glow → dynamics. The final image should be **high-resolution, balanced, and emotionally evocative**. Refer {json_string} for guidance on building the visualization.
"""

	# --- 5. The Vocal Flowchart Score (Sequence Map) ---
	vocal_flowchart_score = f"""
A **clean, hand-drawn style infographic flowchart** visualizing a sequence of **abstract musical events** (derived from the original sheet music's interpretive elements). The aesthetic is highly legible and modular.

The flowchart consists of **multiple oval-shaped nodes** arranged in a generally **downward sequence**, connected by **smooth, directional arrows**. Time flows along the arrows.

**Node Content:** Each oval contains **concise text** describing a musical instruction or event (e.g., 'Crescendo, pizzicato strings', 'Sudden forte, brass fanfare', 'Decrescendo to silence').

**Arrows (Transitions):** Arrows indicate flow. **Thicker arrows** indicate a dynamic increase or acceleration. **Thinner arrows** indicate a dynamic decrease or deceleration.

**Node Styling:** The oval's **border or fill color** can be subtly used to convey overarching mood or instrument group (e.g., warm colors for assertive sections, cool colors for softer sections).

The final image should be an **intuitive, narrative-driven infographic** guiding an audience through the structural and expressive journey of the piece using visual cues, colors, and a clear sequential flow. Refer {json_string} for guidance on building the visualization.
"""

	# --- 6. The Graphic Score Cadenza (Cascading Texture) ---
	graphic_score_cadenza = f"""
A **monochrome, hand-drawn graphic music score fragment** titled "Cadenza," resembling a dynamic, **cascading arc of notes**. The style is pen-and-ink linear drawing.

The music flows as a **dense, accelerating cascade of points** that sweeps **downward and outward** in a wide, parabolic arc. It begins in the top-left with a single Bass Clef.

**Data Mapping:**
- **Notes** are represented by **small solid black circles ($bullet$)** (intense sound) and **small open circles ($circ$)** (lighter sound/harmonics).
- The **density** of the points increases in the center, suggesting a **crescendo or thick texture**.
- **Thin, free-flowing, looping lines** trail from the top and weave through the notes, representing **sustained gestures or glissandi**.

The entire cascade resolves into a **large, low-lying, hand-drawn cloudy formation** filling the bottom, symbolizing a diffuse, sustained sonic conclusion. The overall feeling is kinetic, chaotic, and elegant. Refer {json_string} for guidance on building the visualization.
"""

	# --- 7. The Layered Graphic Score (Color-Coded Timelines) ---
	layered_graphic_score = f"""
A **vibrant, abstract, color-coded graphic music score** titled "Picnic," set against a subtle, light grid paper background. The score is organized into **four distinct horizontal single-line staves** labeled i, ii, iii, and iv. Time flows strictly **left to right**.

Musical events are depicted by **abstract, hand-painted/drawn shapes** placed over or around these lines.
- **Color** is the primary encoder (e.g., pitch, mood, or timbral instruction).
- **Shape/Contour** dictates the musical gesture (e.g., sharp diagonal streaks for attacks, wavy contours for sustained texture, blocky shapes for rhythm).
- **Vertical displacement** indicates pitch contour (slope up/down).

Each line has a distinct texture (e.g., sharp, angled streaks on line i; flowing, continuous patches with textured edges on line iii; low-lying repetitive shapes on line iv). The final rendering should have a **painterly quality** where the colors appear like acrylic or watercolor strokes. Refer {json_string} for guidance on building the visualization.
"""

	# --- 8. The Stochastic Texture Map (Particle Cloud) ---
	stochastic_texture_map_score = f"""
An **abstract graphic music score** rendered as a **stochastic particle cloud map**, full of raw energy and textured detail. The visual style is monochromatic with specific color accents, against a clean white background.

The composition is dominated by a **large, irregularly shaped, diffuse cluster of black and dark grey particles**.
- **Dense, solid black patches** form the cores, representing **loud, complex, or sustained activity**.
- **Gradual scattering** indicates **decaying dynamics/reverberation**.

**Color Bursts** signify **timbral events or energy foci**: A **central, irregular "starburst" of vibrant red and muted yellow particles** marks the main climax, with smaller bursts marking secondary events. The overall aesthetic is raw, organic, and highly textural, like a magnified view of sound particles. Refer {json_string} for guidance on building the visualization.
"""

	# --- 9. The Choreographic Score (Tutti/Soloist Diagrams) ---
	choreographic_graphic_score = f"""
A sophisticated, experimental graphic music score combining choreographic diagrams and textural notation. The style is clean, diagrammatic, and uses primary color blocks.

**LEFT SIDE (Background Tuttimovement):** Features two stylized **color-blocked figures** overlaid with **dashed black lines and arrows** indicating specific choreographic movements, linked directly to **traditional rhythmic notation** placed below.

**RIGHT SIDE (Soloist and Harmonic Texture):**
- A **thick, sweeping, non-metrical black line** labeled "Solist" at the top defines the soloist's expressive contour.
- **Two parallel rectangular diagrams** function as a textural score (Tone Dots). These are vertically striped with **color blocks** (yellow/green) defining a **pitch axis** ("lower" to "higher").
- A **thick, oscillating black line** weaves dramatically through the color zones, detailing a complex, "swinging" harmonic sweep for the orchestra.

The final image must be **highly graphic and diagrammatic**, using bold lines and geometric simplicity to communicate complex performance instructions. Refer {json_string} for guidance on building the visualization.
"""

	# --- 10. The Antiquarian Color-Sphere Score (Parchment Map) ---
	antiquarian_color_sphere_score = f"""
A visualization of a music score in the style of an **Antiquarian Color-Sphere Map**. The image must be rendered on a background that convincingly simulates **ancient, textured, and mottled parchment paper** with irregularly **frayed edges**.

**Structure:** The score is arranged in **five distinct horizontal staves**.
**Data Mapping:** The staves are filled with **colored circles of widely varying sizes**.
- **Color** signifies **pitch or timbre** (e.g., deep green, rich red, yellow-orange).
- **Size** signifies **duration or amplitude** (Large circles = long/loud events).
- **Clusters** of circles indicate **chords or harmonic density**.

The circles are placed over a **diffuse, granular textural field** that follows the staves. A **vertical column of color samples** on the left acts as a visual legend. The final image should feel like a newly discovered, meaningful ancient document. Refer {json_string} for guidance on building the visualization.
"""

	watercolor_flow_prompt = f"""
	A **flowing watercolor visualization of music**, rendered as a **dynamic, liquid abstract painting**. The entire canvas evokes a sense of continuous motion and emotional energy, rather than technical structure.

	**Musical Elements as Painterly Effects:**
	- **Brush Stroke Direction/Angle:** The primary visual metaphor. The **angle and curve of each watercolor stroke** directly encode **pitch movement**. Strokes sweeping upwards represent rising pitches, downward strokes represent falling pitches, and horizontal strokes represent sustained pitches.
	- **Color Saturation:** The **intensity and vibrancy of the watercolor hues** encode **volume/dynamics**. Highly saturated, bold colors signify loud, forte passages, while desaturated, muted, and pastel tones represent soft, piano sections.
	- **Opacity/Transparency:** The **translucence of the watercolor washes** represents **sustain or duration**. Thick, opaque layers indicate long, sustained notes or chords, while thin, transparent washes or quick dabs signify short, staccato notes or rapid decays.
	- **Overall Flow Direction:** The **dominant direction of the visual current or stream** across the canvas corresponds to **tempo**. A calm, slow drift implies an Adagio, while a rapid, turbulent sweep implies an Allegro.

	**Harmonic Mood and Color Palette:**
	- **Major keys** are expressed through a dominant palette of **warm, inviting hues** (e.g., golden yellows, soft oranges, vibrant corals, warm greens).
	- **Minor keys** are expressed through a dominant palette of **cool, introspective hues** (e.g., deep blues, serene purples, muted teals, cool greys).
	- Color blending and gradients between these palettes indicate harmonic transitions or modulations.

	**Aesthetic:**
	The rendering should possess a genuine **painterly, expressive, and high-resolution watercolor aesthetic**. Edges should be soft and bleed slightly, colors should layer transparently, and visible brush textures should be evident. The composition should feel organic and fluid, directly mirroring the emotional ebb and flow of the music.

	**Legend:**
	Include a **small, elegantly integrated artistic legend** in one corner. This legend will display **miniature brush samples** (e.g., an upward stroke, a saturated blob, a transparent wash) with concise text labels explaining their corresponding musical mappings (e.g., "Upward Stroke = Rising Pitch," "Saturated = Loud," "Transparent = Sustain").

	The final image should be a beautiful fusion of abstract art and intuitive musical storytelling. Refer {json_string} for guidance on building the visualization, particularly for extracting pitch contours, dynamic changes, sustain, and key changes.
	"""

	panoramic_waveform_prompt = f"""
	A **breathtaking panoramic visualization of music**, rendered as a **vast, undulating landscape of colorful waves**. The scene is expansive and immersive, evoking the feeling of being immersed within the sound itself.

	**Waves as Musical Elements:**
	- **Vertical Height (Low/High):** The **amplitude of the waves** directly corresponds to **pitch**. Taller, more prominent waves represent higher pitches, while shorter, more subtle undulations represent lower pitches. This creates a clear visual hierarchy of the musical range.
	- **Horizontal Breadth/Length:** The **width or length of individual wave segments** encodes **duration or sustain**. Broad, sweeping waves indicate long, sustained notes or chords, while short, choppy wavelets represent brief, staccato events.
	- **Color:** Color is a primary encoder for **timbre, instrument family, or harmonic quality**.
		- **Vibrant, bright colors** (e.g., electric blues, fiery oranges, vivid greens) for prominent melodic lines or specific instrumental voices (e.g., trumpet fanfare).
		- **Muted, blended colors** (e.g., soft purples, deep teals, earthy browns) for harmonic accompaniment or textural elements.
		- **Color gradients within a wave** can show timbral shifts or evolving harmonies.
	- **Harshness/Softness of Wave Edges/Texture:** The **visual texture and definition of the waves** represent **articulation and dynamics**.
		- **Sharp, jagged, or turbulent wave crests** signify **harsh, accented, or dissonant musical moments** (e.g., a sudden forte, a percussive attack).
		- **Smooth, rolling, or gently swelling wave forms** signify **soft, legato, or consonant musical passages** (e.g., a quiet sustained string chord).
	- **Overall Direction/Flow:** A subtle, continuous flow across the panoramic view from left to right represents the progression of time and **tempo**.

	**Atmosphere and Lighting:**
	The scene should be rendered with **cinematic, atmospheric lighting** that enhances the mood of the music. For instance, a soft, diffused glow for quiet sections, and dramatic, high-contrast lighting for loud, intense passages. The background could be a subtly evolving gradient sky, reflecting the overall mood.

	**Aesthetic:**
	The final image should be **high-resolution, visually rich, and deeply immersive**, resembling a vibrant, fantastical landscape where the mountains and valleys are made of sound waves. It should convey the music's emotional and structural changes through the visual metaphor of a dynamic aquatic panorama.

	The absence of a traditional legend is intentional, as the goal is intuitive understanding through visual metaphor, but a very minimal textual hint in a corner about "Waves = Music" is acceptable. Refer {json_string} for guidance on building the visualization, mapping pitch, dynamics, duration, timbre, and articulation to the wave properties.
	"""

	@classmethod
	def get_prompt_list(cls):
		"""Returns a list of tuples: (attribute_name, prompt_string)."""
		return [
			(name, getattr(cls, name))
			for name in dir(cls)
			if not name.startswith("__")
			and name not in ("json_string", "get_prompt_list")
		]


# Example of how to import and access a prompt:
# from viz_graphics_prompts import GraphicScorePrompts
# prompt_to_test = GraphicScorePrompts.constellation_score.format(json_string=my_music_data)
# print(prompt_to_test)
