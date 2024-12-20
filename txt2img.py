from PIL.Image import Image
from fastapi import HTTPException
import schemas as _schemas
from services import *

async def txt2img(imgPrompt: _schemas.ImageCreate) -> str:
    # 비동기 이미지 생성
    
    image,seed = connect_txt2img(imgPrompt=imgPrompt)
    # 비동기로 S3에 업로드 및 URL 반환
    s3_url = await upload_to_s3(image, BUCKET_NAME, s3_client,seed)
    return s3_url
