from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from chat import get_response

# Initialize FastAPI app
app = FastAPI()

# Setup static files and templates
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust origins as needed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index(request: Request):
    """Serve the main HTML template."""
    return templates.TemplateResponse("base.html", {"request": request})

@app.post("/predict")
async def predict(request: Request):
    """Handle predictions."""
    data = await request.json()
    text = data.get("message")
    
    # TODO: Check if text is valid
    response = get_response(text)
    return JSONResponse(content={"answer": response})

# Production entry point
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=50100)
