import httpx
from fastapi import APIRouter
from typing import Optional,Any


router = APIRouter(prefix="/jobs")
@router.get("/")
def get_jobs(search: Optional[str] = None, category: Optional[str] = None):
    params: dict[str, Any] = {"limit": 20}
    if search: params["search"] = search
    if category: params["category"] = category
    response = httpx.get("https://remotive.com/api/remote-jobs", params=params)
    data = response.json()
    jobs = data["jobs"]
    return jobs
