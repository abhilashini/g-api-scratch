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
 
	chromatic_landscape = f"""
A **breathtaking, cinematic 3D generative landscape visualization** of music. The terrain undulates organically, resembling a majestic **mountain range sculpted from sound waves**.
- The **X-axis** is **time**.
- The **Y-axis** (depth) subtly indicates **pitch**.
- The **Z-axis** (vertical height of the terrain) corresponds to **amplitude or dynamic level**, with towering peaks signifying loud sections.

The landscape is rendered with a **glowing wireframe effect** or a **softly shaded, iridescent surface**. **Colors shift based on instrument groups or mood**: Cool hues (deep blues, aquamarines) for legato/harmony; Warm accents (oranges, golds) for rhythmic emphasis/brass.

**Dramatic, realistic lighting** casts long shadows. **Gentle, ethereal fog or mist** drifts through the lower valleys, adding depth and reflecting quiet dynamics.

The final output is a **high-detail, immersive visual experience**. Refer {json_string} for guidance on building the visualization.
"""

	constellation_score = f"""
A breathtaking **cosmic data-art visualization** transforming sheet music into an **expansive, ethereal constellation map** set against a deep, dark starry night sky.
- **Each musical note is a glowing colored dot ('star')**.
- Its **vertical position (Y-axis)** determines its **pitch**.
- **Time flows linearly from left to right (X-axis)**.
- The **size (radius) of each star** is proportional to the note's **duration**.
- The **intensity of the star's glow** corresponds to the note's **dynamics/volume**.

The **color of each star maps to its note family (pitch class)**. **Thin, shimmering trails of stardust** gracefully connect consecutive notes, forming clear melodic pathways. **Chords** form vibrant, momentary **star clusters**.

The final image should be **high-resolution, balanced, and emotionally evocative**. Refer {json_string} for guidance on building the visualization.
"""

	layered_graphic_score = f"""
A **vibrant, abstract, color-coded graphic music score** titled "Picnic," set against a subtle, light grid paper background. The score is organized into **four distinct horizontal single-line staves** labeled i, ii, iii, and iv. Time flows strictly **left to right**.

Musical events are depicted by **abstract, hand-painted/drawn shapes** placed over or around these lines.
- **Color** is the primary encoder (e.g., pitch, mood, or timbral instruction).
- **Shape/Contour** dictates the musical gesture (e.g., sharp diagonal streaks for attacks, wavy contours for sustained texture, blocky shapes for rhythm).
- **Vertical displacement** indicates pitch contour (slope up/down).

Each line has a distinct texture (e.g., sharp, angled streaks on line i; flowing, continuous patches with textured edges on line iii; low-lying repetitive shapes on line iv). The final rendering should have a **painterly quality** where the colors appear like acrylic or watercolor strokes. Refer {json_string} for guidance on building the visualization.
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

	Refer {json_string} for guidance on building the visualization, mapping pitch, dynamics, duration, timbre, and articulation to the wave properties.
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
- **Musical Complexity (Density/Polyphony/Dynamics) → Iteration Depth:** The **overall density and intricacy of the fractal's detail** is directly proportional to the musical complexity. Periods of intense polyphony, high note density, or forte dynamics result in a deeply iterated, highly detailed fractal structure. Quieter, sparser musical sections display a simpler, less iterated, or more 'zoomed out' view of the fractal.
- **Musical Form/Motif Development → Zoom Level:** The **zoom level into the fractal** evolves with the musical form. The piece might begin with a broad, zoomed-out view (representing the overall structure), and then gradually zoom in on specific, recurring fractal features as musical motifs are developed or repeated.
- **Key Changes/Harmonic Tension/Mood → Color Palette/Hue Shift:** The **color scheme and hue transitions** of the fractal's escape-time coloring algorithm are driven by the music's harmonic qualities. Major keys or consonant sections use a palette of **warm, harmonious, and blending colors** (e.g., gradients of blues, greens, purples). Minor keys, dissonant passages, or moments of high harmonic tension shift to **cooler, more contrasting, or agitated color palettes** (e.g., reds, oranges, sharp yellows, or high-contrast combinations).
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
