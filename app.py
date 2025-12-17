from fastapi import FastAPI, UploadFile, File
from video_analyzer import analyze_video

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Bird Counting API is running"}

@app.get("/health")
def health():
    return {"status": "OK"}

@app.post("/analyze_video")
async def analyze_video_api(
    video: UploadFile = File(...),
    fps_sample: int = 5,
    conf_thresh: float = 0.4
):
    return analyze_video(video.file, fps_sample, conf_thresh)
