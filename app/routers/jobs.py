import httpx
import time
from fastapi import APIRouter
from typing import Optional

router = APIRouter(prefix="/jobs")

_cache = {"data": None, "timestamp": 0}
CACHE_TTL = 600  # 10 minutes

@router.get("/")
async def get_jobs(search: Optional[str] = None, category: Optional[str] = None):
    current_time = time.time()
    if _cache["data"] is None or (current_time - _cache["timestamp"]) > CACHE_TTL:
        print("Fetching fresh data from Remotive...")
        async with httpx.AsyncClient() as client:
            response = await client.get("https://remotive.com/api/remote-jobs")
        _cache["data"] = response.json()["jobs"]
        _cache["timestamp"] = current_time
    
    jobs = _cache["data"]
    if search:
        jobs = [job for job in jobs if search.lower() in job["title"].lower()]
    if category:
        jobs = [job for job in jobs if any(category.lower() in tag.lower() for tag in job["tags"])]
    return jobs