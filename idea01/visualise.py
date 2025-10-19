# --- ASSUMED IMPORTS ---
from google import genai
from google.genai import types
from file_utilities import FileUploader
from analysis_utilities import MusicAnalyzer
from score_processor import ScoreProcessor, response_art_config, CONSISTENCY_DISCLAIMER
from viz_graphics_prompts import GraphicScorePrompts
import json

client = genai.Client() 
file_path_pdf = "/workspaces/g-api-scratch/idea01/beethoven-ludwig-van-sonata-282.pdf"
output_image_dir = "/workspaces/g-api-scratch/idea01/images"

# Initialize the modular components
uploader = FileUploader(client)
analyzer = MusicAnalyzer(client)
processor = ScoreProcessor(
    client, 
    GraphicScorePrompts, 
    response_art_config, 
    CONSISTENCY_DISCLAIMER
)

# ====================================================================
# A S S E M B L E D   P I P E L I N E   E X E C U T I O N
# ====================================================================
def run_music_visualization_pipeline():
    """
    Executes the entire, three-stage music visualization pipeline in sequence:
    Upload -> Analyze -> Process (Narration & Images).
    """
    print("--- STARTING MUSIC VISUALIZATION PIPELINE ---")
    
    # STAGE 1: FILE UPLOAD (FileUploader)
    # ------------------------------------
    print("\n[STAGE 1/3] File Upload...")
    uploaded_file = uploader.upload_local_file(file_path_pdf)
    
    if not uploaded_file:
        print("PIPELINE ABORTED: File upload failed.")
        return

    # STAGE 2: FEATURE EXTRACTION (MusicAnalyzer)
    # ------------------------------------------
    print("\n[STAGE 2/3] Feature Extraction and Structuring...")
    music_features_dict = analyzer.extract_features(uploaded_file)
    
    if not music_features_dict:
        print("PIPELINE ABORTED: Structured feature extraction failed.")
        return

    # Prepare raw string for the image model (Stage 3)
    music_features_raw_string = json.dumps(music_features_dict)
    
    print("\n=== STAGE 2 RESULT: Extracted Data ===")
    print(json.dumps(music_features_dict, indent=4))

    # STAGE 3: VISUALIZATION PROCESSING (ScoreProcessor)
    # --------------------------------------------------
    print("\n[STAGE 3/3] Generating Narrations and Visualizations...")
    processor.process_and_generate(
        sheet_data=music_features_dict,
        sheet_data_raw_string=music_features_raw_string,
        output_dir=output_image_dir
    )
    
    print("\n--- PIPELINE EXECUTION COMPLETE ---")


if __name__ == "__main__":
    run_music_visualization_pipeline()