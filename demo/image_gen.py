from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO

client = genai.Client()

# print(list(client.models.list()))
# print("\n\n")

prompt = (
    "Generate image of an abstract art with swirls and clouds in vibrant colours."
)

response_config = types.GenerateContentConfig(
    response_modalities=[types.Modality.IMAGE, types.Modality.TEXT] # Request both image and potentially text
)

response = client.models.generate_content(
    model="gemini-2.0-flash-exp-image-generation",
    contents=[prompt],
    config=response_config
)

print(response)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(BytesIO(part.inline_data.data))
        image.save("generated_image.png")
