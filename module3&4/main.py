#Generate Pydantic model for the given body
class RequestBody(BaseModel):
    length: int = 20

# Create a FastAPI endpoint that accepts a POST request with a JSON body containing a single field called "text" and returns a checksum of the text
@app.post('/checksum')
def checksum(body: RequestBody):
    # Add your checksum logic here
    pass

# run uvicorn server
# uvicorn main:app --reload
# open a web browser and navigate to http://
# localhost:8000/ui/index.html
