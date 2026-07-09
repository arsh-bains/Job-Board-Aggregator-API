import httpx
from fastapi import APIRouter
from typing import Optional


router = APIRouter(prefix="/jobs")
@router.get("/")
def get_jobs(search: Optional[str] = None, category: Optional[str] = None):
    response = httpx.get("https://remotive.com/api/remote-jobs")
    data = response.json()
    jobs = data["jobs"]
    if search:
        jobs = [job for job in jobs if search.lower() in job["title"].lower()]
    if category:
        jobs = [job for job in jobs if any(category.lower() in tag.lower() for tag in job["tags"])]
    return jobs



