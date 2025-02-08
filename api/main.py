from fastapi import FastAPI, Depends

from di import select_dependencies
from lib.proto.protean import Protean


def injection():
    return select_dependencies()
app = FastAPI()

@app.get("/")
def read_root(x: Protean = Depends(injection)):
    return {"message": x.speak_word()}
