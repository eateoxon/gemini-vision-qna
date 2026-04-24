from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
import io

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze")
async def analyze_image(
    image: UploadFile = File(...),
    question: str = Form(...)
):
    contents = await image.read()

    if len(contents) > MAX_FILE_SIZE:
        raise HTTPException(status_code=400, detail="Image exceeds 5MB limit")

    try:
        Image.open(io.BytesIO(contents))
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file")

    return {
        "message": "Image and question received successfully",
        "question": question
    }
