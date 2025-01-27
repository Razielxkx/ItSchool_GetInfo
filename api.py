from fastapi import FastAPI
from src.models import ItSchoolDb

app = FastAPI()

@app.get("/courses")
def get_courses(title: str | None = None):
    if title:
        return ItSchoolDb.get_course(title)
    return ItSchoolDb.get_all_courses()

@app.get("/trainers")
def get_trainers(name: str | None = None):
    if name:
        return ItSchoolDb.get_trainer(name)
    return ItSchoolDb.get_all_trainers()



# @app.post("/movies")
# def add_movie(movie: MovieInput, db: Session = Depends(get_db)):
#     if db.query(Movie).filter(Movie.id == movie.id).first():
#         raise HTTPException(status_code=400, detail="Movie with this ID already exists.")
#     new_movie = Movie(**movie.model_dump())
#     print(new_movie)
#     db.add(new_movie)
#     db.commit()
#     db.refresh(new_movie)
#     return {"message": "Movie added successfully", "movie": new_movie}