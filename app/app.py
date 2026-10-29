from fastapi import FastAPI ,HTTPException
from app.schema import posttype
from databasecofig import session 

app = FastAPI()
post={
    1:{"title": "Fun Fact", "content": "The Hogwarts motto 'Draco Dormiens Nunquam Titillandus' translates to 'Never tickle a sleeping dragon'."},
    2:{"title": "Update", "content": "Just got my hands on a new Firebolt! Excited for the next Quidditch match."},
    3:{"title": "Magic Insight", "content": "Mastering the Patronus Charm requires intense focus on your absolute happiest memory."},
    5:{"title": "Quote", "content": "\"Happiness can be found, even in the darkest of times, if one only remembers to turn on the light.\""},
    6:{"title": "Weekend Plans", "content": "Might finally brew that Polyjuice Potion... or just grab a Butterbeer at The Three Broomsticks."},
    7:{"title": "Question", "content": "What's the most underrated defensive spell you've ever used in a duel?"},
    8:{"title": "Mini Announcement", "content": "New Daily Prophet drops tomorrow—covering the weirdest creatures in the Forbidden Forest!"},
    9:{"title": "Reminder", "content": "Don't forget to get your Hogsmeade permission slips signed before the end of term."},
    10:{"title": "House Pride", "content": "Another 50 points to Gryffindor! The House Cup is looking within reach this year."},
    4:{"title": "Daily Motivation", "content": "\"It is our choices that show what we truly are, far more than our abilities.\""}
}


@app.get("/harry")
def harry(limit:int =None):
    db=session()
    db.query()
    if limit:
        return list(post.values())[:limit]
    return post

@app.get("/post/{id}")
def get_post(id:int):
    if id not in post:
        raise HTTPException(status_code=402, detail="Post not found")
    return post.get(id)
i=11
@app.post("/create_post")
def create_post(post:posttype) -> posttype:
    new_content={"title":post.title,"content":post.content}
    post[i+1]=new_content
    return new_content