import json
from typing import Optional, Any

class MusicAnalyzer:
    """
    Handles API calls to analyze sheet music features using a constrained prompt.
    """
    def __init__(self, client, model: str = "gemini-2.5-flash"):
        self.client = client
        self.model = model
        self.prompt_template = """
You are an expert AI musicologist and accessibility tutor.
Analyze the uploaded sheet music to translate its core structure and feeling.

GOAL: The analysis must be structured and descriptive for three target groups:
1. **Novice/Beginner** who cannot read traditional sheet music.
2. **Someone who is Deaf/Hard of Hearing** to appreciate how the music *feels*.
3. **Visualization System** requiring highly structured, quantitative data.

FOCUS ON: Extracting features that convey the music's **emotional trajectory, physical movement, and texture.**

--- RESPONSE FORMAT (MUST be a single JSON object) ---
{{
    "title": "Piece Title or Placeholder",
    "composer": "Composer Name or Unknown",
    "key_signature": "Major/Minor (e.g., 'C Major', 'A Minor')",
    "time_signature": "Time structure (e.g., '4/4', '3/4')",
    "initial_tempo": {{
        "bpm": "90",
        "description": "Tempo term (e.g., 'Andante', 'A slow, walking pace')",
        "term": "Andante"
    }},
    "initial_dynamics": {{
        "level": "p", 
        "description": "Loudness term (e.g., 'soft', 'Quiet')",
        "articulation": "Texture (e.g., 'smoothly', 'sharp/staccato')"
    }},
    "overall_mood": "Emotional quality (e.g., 'Calm and reflective', 'Energetic and playful')",
    "structural_analysis": [
        {{
            "section_id": "A",
            "feature_focus": "Melody",
            "description": "Melody contour (e.g., 'mostly low, rising sharply in the middle')",
            "pitch_range_midinotes": "List of MIDI notes (e.g., [60, 62, 64...])"
        }},
        {{
            "section_id": "B",
            "feature_focus": "Rhythm",
            "description": "Rhythmic pattern (e.g., 'Fast, repeating sixteenth notes')",
            "pattern_notation": "Simplified rhythm notation (e.g., 'ti-ti-ta')"
        }}
    ],
    "repeating_motifs": [
        {{
            "type": "Rhythmic",
            "description": "A consistent, simple beat.",
            "duration": "2 measures"
        }}
    ]
}}
--- END OF RESPONSE FORMAT ---

Return ONLY the JSON object. Do not include any explanation or markdown text outside the JSON block.
"""

    def extract_features(self, uploaded_file: Any) -> Optional[dict]:
        """
        Calls the Gemini model to analyze the file and extract structured musical features.

        Args:
            uploaded_file: The client.files.File object returned by FileUploader.

        Returns:
            A Python dictionary containing the extracted features, or None on failure.
        """
        if uploaded_file is None:
            return None

        print("\n--- 2. Starting Feature Extraction via Gemini ---")
        try:
            # Pass both the file and the highly constrained prompt
            response = self.client.models.generate_content(
                model=self.model,
                contents=[uploaded_file, self.prompt_template],
            )
            
            # The model is strictly instructed to return ONLY the JSON object
            raw_text = response.text.strip()
            
            # Attempt to parse the JSON output
            # Clean up potential markdown code block wrappers (e.g., ```json...```)
            if raw_text.startswith("```json"):
                raw_text = raw_text.lstrip("```json").rstrip("```")
            elif raw_text.startswith("```"):
                raw_text = raw_text.lstrip("```").rstrip("```")
                
            music_features = json.loads(raw_text)
            print("SUCCESS: Musical features extracted and parsed.")
            return music_features
            
        except json.JSONDecodeError as e:
            print(f"ERROR: Failed to parse model output as JSON. Check model's adherence to format: {e}")
            print(f"Raw Output (First 200 chars): {raw_text[:200]}...")
            return None
        except Exception as e:
            print(f"ERROR: Gemini API call failed during feature extraction: {e}")
            return None