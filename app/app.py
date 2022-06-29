from datetime import datetime
from msilib.schema import Error
from typing import Dict, List
from fastapi import FastAPI, HTTPException
from models import Post, UpdatePostPayload

app = FastAPI()

posts_db: Dict[str, Post] = {}


@app.get('/')
def get_posts() -> List[Post]:
    return list(posts_db.values())


@app.post('/posts')
def create_post(post: Post):
    created_post = post.dict()
    posts_db[created_post['id']] = created_post
    return created_post


@app.get('/posts/{post_id}')
def get_post(post_id: str):
    try:
        post = posts_db[post_id]
        return post
    except KeyError:
        raise HTTPException(status_code=404, detail="Post not found")


@app.delete('/posts/{post_id}')
def delete_post(post_id: str):
    try:
        del posts_db[post_id]
        return {"status": "Success"}
    except KeyError:
        raise HTTPException(status_code=404, detail="Post not found")


@app.put('/posts/{post_id}')
def update_post(post_id: str, update_payload: UpdatePostPayload):
    try:
        assert posts_db[post_id]
        previous_content = posts_db[post_id]
        posts_db[post_id] = {**previous_content, **update_payload.dict()}
        return posts_db[post_id]

    except KeyError:
        raise HTTPException(status_code=404, detail="Post not found")


@app.post('/posts/{post_id}/publish')
def publish_post(post_id: str):
    try:
        if posts_db[post_id]['published']:
            raise Error("The post is already published")

        posts_db[post_id]['published'] = True
        posts_db[post_id]['published_at'] = datetime.now()
        return posts_db[post_id]

    except KeyError:
        raise HTTPException(status_code=404, detail="Post not found")
