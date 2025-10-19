from google import genai
import json
from file_utilities import FileUploader
from analysis_utilities import MusicAnalyzer
from google.genai import types
from PIL import Image
from io import BytesIO
import json
import traceback
from viz_graphics_prompts import GraphicScorePrompts

# --- SETUP (Replace MockClient with your actual client initialization) ---
# client = genai.Client(...)
class MockClient:
    def __init__(self):
        self.files = self
        self.models = self
    def upload(self, file):
        class MockFile:
            name = str(file)
        return MockFile()
    def generate_content(self, model, contents, config=None):
        # MOCK response for feature extraction
        class MockResponse:
            class MockCandidate:
                class MockPart:
                    # Mocking a constrained JSON output for the prompt test
                    text = """
                    {
                        "title": "Inaccessible Toile",
                        "composer": "Anon.",
                        "key_signature": "C Minor",
                        "time_signature": "4/4",
                        "initial_tempo": {
                            "bpm": "100",
                            "description": "Moderato, a steady, measured speed",
                            "term": "Moderato"
                        },
                        "initial_dynamics": {
                            "level": "mf", 
                            "description": "Moderately loud",
                            "articulation": "smooth and connected (legato)"
                        },
                        "overall_mood": "Determined and slightly melancholy",
                        "structural_analysis": [
                            {
                                "section_id": "A",
                                "feature_focus": "Melody",
                                "description": "Melody stays in a mid-range, gently moving up and down like shallow waves.",
                                "pitch_range_midinotes": "[55, 60, 65, 67]"
                            }
                        ],
                        "repeating_motifs": [
                            {
                                "type": "Rhythmic",
                                "description": "A driving, consistent 'long-short-short' beat repeats every two measures.",
                                "duration": "2 measures"
                            }
                        ]
                    }
                    """
                content = type('MockContent', (object,), {'parts': [MockPart()]})
            candidates = [MockCandidate()]
            
        return MockResponse()

class MockTypes:
    def __init__(self):
        self.IMAGE = 'IMAGE'
        self.TEXT = 'TEXT'
    class GenerateContentConfig:
        def __init__(self, response_modalities):
            self.response_modalities = response_modalities

client = genai.Client()
# Assume FileUploader and MusicAnalyzer are the classes defined above
uploader = FileUploader(client)
analyzer = MusicAnalyzer(client)

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

# --- EXECUTION FLOW ---

# 1. Define the input file path (Simulating user upload of a PDF)
file_path_pdf = "/workspaces/g-api-scratch/idea01/beethoven-ludwig-van-sonata-282.pdf"

print("--- 1. File Upload Stage ---")
uploaded_file = uploader.upload_local_file(file_path_pdf)

# 2. Extract musical features
if uploaded_file:
    music_features_dict = analyzer.extract_features(uploaded_file)
    
    if music_features_dict:
        # 3. Output the result in a readable format
        print("\n=== FINAL EXTRACTED MUSICAL FEATURES (JSON) ===")
        # The dictionary can now be passed directly to the visualization class/function
        print(json.dumps(music_features_dict, indent=4))
    else:
        print("\nPROCESS HALTED: Could not generate structured musical features.")
else:
    print("\nPROCESS HALTED: Could not upload the source file.")
    
class ScoreProcessor:
    """
    Handles the final stage of the pipeline: generating narration and images 
    for all available prompts based on the extracted music features.
    """
    def __init__(self, client, prompts_class, art_config, disclaimer):
        self.client = client
        self.prompts_class = prompts_class
        self.art_config = art_config
        self.disclaimer = disclaimer

    def process_and_generate(self, sheet_data: dict[str, any], sheet_data_raw_string: str, output_dir: str = "/workspaces/g-api-scratch/idea01/images"):
        """
        Runs the full visualization generation loop.

        Args:
            sheet_data: The parsed music features (Python dict).
            sheet_data_raw_string: The raw JSON string of the features (used for image prompt).
            output_dir: The directory to save the generated images.
        """
        for name, prompt in self.prompts_class.get_prompt_list():
            
            # 1. DYNAMICALLY EXTRACT KEY DATA FOR NARRATION
            try:
                # Safely extract data for narration, using generic keys
                data_summary = {
                    "title": sheet_data.get("title", "The Music"),
                    "key_mood": sheet_data.get("key_signature", "Neutral").split(" ")[0],
                    "time_signature": sheet_data.get("time_signature", "N/A").split(" ")[0],
                    "initial_tempo_desc": sheet_data.get("initial_tempo", {}).get("description", "A moderate pace"),
                    "initial_tempo_term": sheet_data.get("initial_tempo", {}).get("term", "Moderato").strip("()"), # Use 'term' from the constrained JSON
                    "initial_dynamics_desc": sheet_data.get("initial_dynamics", {}).get("description", "Quiet"),
                    "initial_dynamics_term": sheet_data.get("initial_dynamics", {}).get("level", "p"),
                    "initial_articulation_term": sheet_data.get("initial_dynamics", {}).get("articulation", "smoothly"),
                    # Adjusting to the new JSON structure for motifs
                    "rhythm_highlight": sheet_data.get("repeating_motifs", [{}])[0].get("description", "A consistent, simple beat."),
                }
            except Exception as e:
                print(f"\n--- ERROR in Data Extraction for {name} ---")
                print(f"FAILED to extract data using dictionary access: {e}")
                print("Traceback:\n" + traceback.format_exc())
                continue # Skip visualization for this prompt
                
            # 2. ASSEMBLE GENERIC NARRATION PROMPT
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
            
            # 3. Call the text model for narration
            try:
                response_narration = self.client.models.generate_content(
                    model="gemini-2.5-flash", 
                    contents=[narration_prompt_text]
                )
                narration = response_narration.text.strip()
            except Exception as e:
                narration = f"[Error generating narration from API: {e}]"
                
            print(f"\n=======================================================")
            print(f"--- Visualization: {name} ---")
            print(f"NARRATION: {narration}")
            
            # 4. GENERATE IMAGE (using the raw JSON string)
            try:
                response_art = self.client.models.generate_content(
                    model="gemini-2.0-flash-exp-image-generation",
                    contents=[prompt.format(json_string=sheet_data_raw_string)], 
                    config=self.art_config
                )

                # 5. SAVE IMAGE
                image_saved = False
                for part in response_art.candidates[0].content.parts:
                    if part.inline_data:
                        image = Image.open(BytesIO(part.inline_data.data))
                        image_filename = f"{output_dir}/{name}.png"
                        image.save(image_filename)
                        print(f"STATUS: Image saved as {image_filename}")
                        image_saved = True
                        break 
                
                if not image_saved:
                    print("STATUS: No image data found in the response.")

            except Exception as e:
                print(f"ERROR: Failed to generate or save image for {name}: {e}")
            
        # 6. PRINT SINGLE-BLOCK DISCLAIMER
        print(self.disclaimer)