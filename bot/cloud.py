import os
import boto3
from pathlib import Path
from bot.logger import logger

USE_S3 = os.getenv("USE_S3", "false").lower() == "true"
S3_BUCKET = os.getenv("S3_BUCKET")
S3_REGION = os.getenv("S3_REGION")
S3_ACCESS_KEY = os.getenv("S3_ACCESS_KEY")
S3_SECRET_KEY = os.getenv("S3_SECRET_KEY")

if USE_S3:
    s3 = boto3.client(
        's3',
        region_name=S3_REGION,
        aws_access_key_id=S3_ACCESS_KEY,
        aws_secret_access_key=S3_SECRET_KEY
    )
else:
    s3 = None

def upload_to_s3(local_path: Path, remote_path: str) -> bool:
    if not USE_S3 or not s3:
        logger.warning("S3 upload skipped (disabled)")
        return False
    try:
        s3.upload_file(str(local_path), S3_BUCKET, remote_path)
        logger.info(f"Uploaded to S3: {remote_path}")
        return True
    except Exception as e:
        logger.error(f"S3 Upload failed: {e}")
        return False
