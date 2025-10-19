class GraphicScorePrompts:
	"""
	A class containing highly descriptive prompt templates for generating
	various experimental and graphic music score visualizations.

	Each prompt is engineered to include deterministic, quantitative mapping rules
	to maximize visual consistency (structural similarity) across generation runs
	for the same input data.
	"""

	# Placeholder for musical data reference (replace with actual data string when using)
	json_string = "JSON_DATA_STRING_FOR_MAPPING"
 
	chromatic_landscape = f"""
A **precise, cinematic 3D generative landscape visualization** of music. The terrain undulates organically, resembling a majestic **mountain range sculpted from sound waves**.
- The **X-axis** is **time**. **Time progression must be strictly linear and uniform.**
- The **Y-axis** (depth) **quantitatively indicates pitch**. Higher absolute pitch values must result in greater Y-axis depth (closer to the viewer).
- The **Z-axis** (vertical height of the terrain) **quantitatively corresponds to amplitude (dynamic level)**. The maximum height of peaks must be **directly proportional** to the peak dynamic level (e.g., Forte = 10 units high).

The landscape is rendered with a **glowing wireframe effect** using a **fixed scale**. **Colors shift based on instrument groups or mood**: Cool hues for legato/harmony; Warm accents for rhythmic emphasis/brass.

**Lighting and shadow direction must be fixed and consistent** (e.g., top-left source) for all renders. **Ethereal fog or mist** opacity must be **inversely proportional to the volume**.

The final output is a **high-detail, scalable visual experience**. Refer {json_string} for precise guidance on pitch, amplitude, and instrument mapping.
"""

	constellation_score = f"""
A **deterministic cosmic data-art visualization** transforming sheet music into an **expansive, ethereal constellation map** set against a deep, dark starry night sky.
- **Each musical note is a glowing colored dot ('star')**.
- Its **vertical position (Y-axis) must be strictly mapped to MIDI pitch number**.
- **Time flows linearly from left to right (X-axis)**. **Horizontal placement must be strictly proportional to duration**.
- The **size (radius) of each star** is **quantitatively proportional to the note's duration**. (e.g., Whole note = 10 units radius).
- The **intensity of the star's glow** is **quantitatively proportional to the note's dynamics/volume**. (e.g., pp=20% glow, ff=100% glow).

The **color of each star maps strictly to its note family (pitch class)** using a **fixed 12-color wheel**. **Thin, shimmering trails of stardust** connect consecutive notes, forming clear melodic pathways. **Chords** form distinct, compact **star clusters** with zero X-axis separation.

The final image must adhere to these **fixed scaling rules** for reproducibility. Refer {json_string} for quantitative data.
"""

	layered_graphic_score = f"""
A **deterministic, abstract, color-coded graphic music score** titled "Picnic," set against a subtle, light grid paper background. The score is organized into **four fixed-position horizontal single-line staves** labeled i, ii, iii, and iv. Time flows **strictly left to right and is metrically consistent**.

Musical events are depicted by **fixed geometric/painted shapes** placed over or around these lines.
- **Color** is the primary encoder, mapped **strictly by instrument (e.g., Red=Violins, Blue=Oboe)**.
- **Shape/Contour** dictates the **articulation and rhythmic structure** (e.g., sharp diagonal streaks for attacks, wavy contours for sustained texture, blocky shapes for rhythm). **Shape mapping must be consistent.**
- **Vertical displacement** from the central stave line **must be proportional to pitch deviation** from the tonic.

Each line must maintain a **consistent texture type** as specified (e.g., line i always sharp streaks, line iii always wavy contours). The final rendering should adhere to **fixed, repeatable mapping rules** for shape size and placement. Refer {json_string} for quantitative data.
"""

	watercolor_flow_prompt = f"""
	A **deterministic, flowing watercolor visualization of music**, rendered as a **dynamic, liquid abstract painting**. The canvas evokes continuous motion and emotional energy, with colors and strokes strictly mapped to musical data.

	**Musical Elements as Painterly Effects:**
	- **Brush Stroke Direction/Angle:** The **angle and curve of each stroke** directly encode **pitch movement magnitude**. A large pitch leap must result in a steeper curve/angle.
	- **Color Saturation:** The **intensity and vibrancy of the watercolor hues** encode **volume/dynamics**. Saturation must be **quantitatively proportional** to the dynamic level (e.g., *p* = 30% saturation, *f* = 90% saturation).
	- **Opacity/Transparency:** The **translucence of the washes** is **inversely proportional to sustain/duration**. A whole note must be a thick, opaque layer; a sixteenth note, a thin, transparent dab.
	- **Overall Flow Direction:** The **dominant direction of the visual current** across the canvas is **inversely proportional to tempo** (slower tempo = more horizontal/calm drift).

	**Harmonic Mood and Color Palette:**
	- **Major keys** use a **fixed warm palette**. **Minor keys** use a **fixed cool palette**.
	- Color blending intensity must be **proportional to the rate of harmonic change**.

	**Aesthetic:** The rendering must use **fixed digital watercolor brushes and textures** to minimize run-to-run variation, prioritizing **mapping accuracy** over unpredictable artistic flair. Refer {json_string} for data-driven consistency.
	"""

	panoramic_waveform_prompt = f"""
	A **deterministic panoramic visualization of music**, rendered as a **vast, undulating landscape of colorful waves**. The scene is expansive and immersive, with wave properties strictly mapped to musical parameters.

	**Waves as Musical Elements (Fixed Mapping):**
	- **Vertical Height (Amplitude):** The **vertical height** of the waves **must be strictly proportional to pitch register**. (e.g., Middle C = 5 units height).
	- **Horizontal Breadth/Length:** The **width of individual wave segments** is **quantitatively proportional to note duration/sustain**. (e.g., Half note = 10 units width).
	- **Color:** Color is the primary encoder for **timbre/instrument family**, using a **fixed set of high-contrast colors** (e.g., Red=Brass, Blue=Strings).
	- **Harshness/Softness of Wave Edges/Texture:** The **jaggedness or smoothness of wave crests** is **quantitatively proportional to the articulation** (sharpness for staccato, smoothness for legato) and **dynamic accent**.
	- **Overall Direction/Flow:** Time progression must be a **strictly linear horizontal flow**.

	**Aesthetic:** The final image must be rendered with a **consistent, fixed perspective and lighting scheme** to ensure identical musical data yields nearly identical visual output, emphasizing **data fidelity**. Refer {json_string} for quantitative mapping rules.
	"""
 
	light_painting_dynamic_score = f"""
A **dark, cinematic photo composition** featuring a musician (e.g., a violinist or cellist) playing in a completely dark studio, creating a **vibrant, dynamic light painting** that visualizes the music being played.

**Visual Elements and Mappings:**
- **The Light Paths (Melody/Gesture):** The core of the image is the **trail of light** emitted from the instrument's bow or movement. The **shape of this light path** directly follows the **melodic contour and expression** (e.g., smooth, sweeping waves for legato; sharp, jagged peaks for staccato/accents).
- **Light Source and Emission:** The light should appear to **emanate directly from the instrument or the action of the musician**, giving the impression that the sound itself is glowing and being visually painted in the air.
- **Light Color:** The **color of the light** encodes a specific musical parameter, ideally **pitch class or instrument/timbre**. Use a **chromatic color map** (e.g., blue for low register, red for mid, purple for high) or distinct colors for different instrument parts.
- **Light Intensity and Thickness:** The **brightness, thickness, and trailing length of the light trails** encode **dynamics and sustain**. Thicker, intensely bright trails represent loud, *forte* passages or sustained notes. Fainter, thinner trails represent quiet, *piano* sounds or staccato notes.

**Integration of Notation (Contextual Anchor):**
- **Superimposed Sheet Music:** A **clear, traditional sheet music staff** corresponding to the visualized passage must be **subtly superimposed** beneath or directly within the light painting area. This provides a visual **anchor for pitch and rhythm** against the abstract light forms. The staff itself should be rendered in a soft, non-distracting color (e.g., deep grey or faint white lines).

**Aesthetic:**
The final image should be a **high-contrast, long-exposure photograph** with a **dramatic, professional look**. The light trails must be **clean, luminous, and sharp**, contrasting vividly with the deep black background. The overall effect is a powerful, dynamic fusion of the abstract sound wave and its precise musical notation.
Refer {json_string} for guidance on extracting melody contour, pitch classes for color mapping, dynamics for intensity, and the exact sheet music to render beneath the light trails.
"""

	abstract_3d_ribbon_score = f"""
	A **mesmerizing, high-resolution 3D abstract sculpture of sound**, visualized as a **smooth, dynamically moving, intertwined cluster of luminous tubes or ribbons**, similar to twisted cables or thick ribbons. The rendering should be **hyper-realistic and artistic**, set against a clean, neutral studio background (e.g., soft gradient grey).

	**Structure and Flow:**
	- The overall form progresses **horizontally from left to right**, representing the musical timeline.
	- The entire structure appears to be **floating and suspended in motion**.

	**Musical Parameters as Physical Form:**
	- **Vertical Displacement (Y-axis):** The **vertical height** of the entire structure and the individual ribbons within it correspond to the **pitch register**. A high-pitched passage results in the structure floating higher; a bass line is represented lower.
	- **Ribbon Thickness (Radius):** The **radius or thickness of the individual tubes/ribbons** encodes **dynamics/amplitude**. Thick, voluminous tubes represent loud, *forte* passages, while thin, subtle threads represent quiet, *piano* moments.
	- **Twisting/Intertwining:** The degree to which the ribbons **twist, wrap, and intertwine around each other** signifies **harmonic complexity and polyphony**. A simple melody is a single, clean ribbon; a dense chord cluster or complex counterpoint is a tight, intricate braid or tangle of multiple tubes.
	- **Ribbon Color/Material:** The **color and material texture** of each individual ribbon designates a **specific instrumental timbre or melodic voice**. Use distinct, aesthetically pleasing colors (e.g., cool silver for strings, warm bronze for brass, electric blue for woodwinds). The material should suggest **soft, smooth, and flexible plastic or luminous fiber**.

	**Aesthetic:**
	The final image should be rendered with **soft, diffused studio lighting** that creates subtle highlights and shadows on the material, emphasizing the smooth, volumetric nature of the tubes. The composition is **elegant, clean, and architecturally beautiful**, translating the complexity of the music into a tangible, flowing, and aesthetically pleasing 3D object.
	Refer {json_string} for guidance on mapping pitch range, dynamics, polyphony, and instrumental timbres to the 3D structure.
	"""
 
	solar_chronometer_score_strokes = f"""
A **vibrant, high-resolution painterly visualization** titled "Solar Chronometer Score," set against a dark, smoky background. The composition is centered on a large, glowing, roughly circular form (the "Sun").

**The Core Layer (Harmony/Dynamics):**
- The central circle is entirely filled with **thick, highly visible, layered brushstrokes of warm colors** (e.g., saturated yellow and orange).
- The **thickness and density of these base strokes** encode the **overall dynamic level and harmonic intensity** of the piece (denser/thicker strokes for loud, harmonically rich passages). The texture should be highly tangible, like heavy impasto paint.

**The Structural Layer (Instrumental Parts):**
- Overlaying the textured background, draw **four distinct, horizontal, solid color blocks** (e.g., Red, Deep Green, Royal Purple, Pale Beige). These blocks represent four specific instrumental or vocal parts.
- On each block, draw **simple notation symbols** (small open circles, short black lines, dots) to denote the **pitch register and basic rhythmic events** specific to that instrumental part.

**The Expressive Layer (Melody/Gesture - Focus on Strokes):**
- **Dynamic, sweeping lines** are the key visual element, representing the piece's expressive gestures and active melodies. These lines must flow **around and through the central circle** and connect the structural staves.
- **Stroke Color:** Use **four contrasting, high-saturation colors** (e.g., electric blue, bright cyan, stark white, magenta) for these expressive lines, with each color representing a **different, prominent thematic or melodic line** (e.g., Solo Instrument 1, Solo Instrument 2, Lead Counter-melody).
- **Stroke Length/Curve:** **Long, sweeping curves and spirals** encode sustained, broad melodic movements or expressive crescendi. **Short, sharp, angled strokes** encode fast, accented, or percussive gestures.
- **Stroke Thickness:** The **thickness of these colored lines** varies to encode **volume/force** (thicker line = louder/more forceful gesture).

**Aesthetic:**
The final image should look like a **masterful abstract expressionist painting** with precise, geometric elements integrated. The interplay between the chaotic, thick background strokes and the clean, energetic colored lines should visually convey the emotional power and structured complexity of the music.
Refer {json_string} for guidance on mapping instrumental lines to color, dynamic changes to stroke thickness, and pitch/duration to stroke length/curve.
"""

	geometric_micro_notation_score = f"""
A **highly structured, abstract graphic music score** in the style of the provided reference image, resembling a **complex, two-dimensional architectural blueprint of sound**. The aesthetic is clean, precise, and minimalist, utilizing stark geometric forms and a limited color palette on a pristine white background.

**Central Axis and Time Flow:**
- The score is organized around a **dominant, thin horizontal black line** that traverses the entire width of the canvas, representing the primary **timeline**. Time flows strictly **left to right**.

**Two Primary Voices/Colors:**
- All geometric elements are rendered in one of **two distinct, contrasting solid colors**: **deep, dark red** and **dark, muted blue**. These colors represent two primary, distinct musical "voices" or layers.

**Geometric Elements and Their Arrangement:**
- **Vertical Lines:** Numerous thin vertical black lines extend both **above and below the central horizontal axis**. Their **lengths vary significantly**, visually indicating duration, pitch range, or dynamic extent. These lines form the foundational "stems" for other shapes.
- **Horizontal Lines:** Shorter horizontal lines, in either red or blue, connect vertical lines or extend from shapes, acting as connectors, markers, or structural indicators.
- **Solid Circles ($\bullet$)**: Used in both red and blue, these represent distinct, impactful musical events. Their **size varies** (small to medium), indicating relative duration or dynamics.
- **Solid Squares ($\blacksquare$)**: Also in red and blue, representing different types of events or articulations.
- **Solid Triangles ($\blacktriangle$ / $\blacktriangledown$)**: Pointing both upwards and downwards, primarily used within dense clusters, suggesting directional gestures or specific attacks.
- **Open Circles ($\circ$) and Open Squares ($\square$)**: These smaller, lighter shapes are predominantly used within the large "spires," indicating less emphatic or more numerous rapid events.

**Dense "Spires" / Clusters:**
- The composition features **two prominent, large, symmetrical, conical (or pyramidal) clusters** of shapes, extending both **upward and downward** from the central axis. These represent sections of **intense musical density, rapid activity, or wide-ranging pitch/dynamic sweeps**.
- These "spires" are densely packed with a mix of small solid and open circles, squares, and triangles, in both red and blue, creating a visually complex, granular texture. One spire is roughly to the left-center, the other to the right-center.

**Scattered Elements:**
- Various individual or small groups of colored geometric shapes (circles, squares, triangles) are **scattered sparsely** along the central timeline and attached to vertical lines between the main spires, representing isolated events or quieter passages.

**Balance and Negative Space:**
- The composition demonstrates a strong sense of **balance and visual rhythm**, with elements carefully placed relative to the central axis.
- The **pristine white background** dominates, providing maximum contrast for the crisp geometric forms and emphasizing their precision.

The final image should be a **high-resolution, visually striking work of minimalist information art**, conveying musical structure and texture through purely abstract, geometric means. Refer {json_string} for guidance on translating specific musical data (pitch, duration, dynamics, instrumentation for color coding, event types for shape) into this precise geometric language.
"""

	mandelbrot_music_prompt = f"""
A **dynamic and abstract visualization of music as a Mandelbrot set (or similar fractal)**, presented as a highly detailed, generative art piece. The image transforms musical parameters into the fractal's intricate geometry and vibrant colors.

**Fractal Generation Controlled by Music:**
- **Musical Complexity (Density/Polyphony/Dynamics) → Iteration Depth:** The **overall density and intricacy of the fractal's detail** is **directly proportional** to the musical complexity. Periods of intense polyphony, high note density, or forte dynamics result in a deeply iterated, highly detailed fractal structure. Quieter, sparser musical sections display a simpler, less iterated, or more 'zoomed out' view of the fractal.
- **Musical Form/Motif Development → Zoom Level:** The **zoom level into the fractal** evolves with the musical form. The piece might begin with a broad, zoomed-out view (representing the overall structure), and then gradually zoom in on specific, recurring fractal features as musical motifs are developed or repeated.
- **Key Changes/Harmonic Tension/Mood → Color Palette/Hue Shift:** The **color scheme and hue transitions** of the fractal's escape-time coloring algorithm are driven by the music's harmonic qualities. Major keys or consonant sections use a **fixed warm, harmonious palette**. Minor keys, dissonant passages, or moments of high harmonic tension shift to **fixed cooler, more contrasting, or agitated color palettes**.
- **Sectional Changes/Thematic Areas → Region of Interest:** Distinct **musical sections or thematic areas** are represented by **shifts in the rendered region of the Mandelbrot set**. The camera subtly pans or jumps to a new, recognizable location within the fractal's plane, creating visual landmarks corresponding to musical forms.
- **Dissonance/Accents/Noise → Controlled Glitches/Distortion:** Intense dissonance, sudden accents, or percussive noise elements in the music trigger **momentary visual glitches, subtle distortions, or sudden shifts in the rendering parameters** (e.g., a brief, sharp change in the fractal's formula or coloring) to mimic the sonic impact.

**Aesthetic:**
The final image should be **high-resolution, visually complex, and mesmerizing**. It's a generative art piece where the abstract beauty of the fractal is infused with the evolving character of the music. The colors should be luminous and seamlessly blended, creating an immersive experience that reveals hidden structures upon closer 'listening.'
Refer {json_string} for guidance on extracting relevant musical parameters for fractal control.
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
