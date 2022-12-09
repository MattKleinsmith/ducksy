import boto3
import os
import requests
from dotenv import load_dotenv
load_dotenv()

BUCKET_NAME = os.environ.get("S3_BUCKET")
S3_LOCATION = f"https://{BUCKET_NAME}.s3.amazonaws.com/"

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET")
)


def upload_image_to_bucket(url, acl="public-read"):
    image_name = os.path.basename(url)
    bucket_url = f"{S3_LOCATION}{image_name}"

    # Don't bother the third party if we already have the image
    try:
        s3.head_object(Bucket=BUCKET_NAME, Key=image_name)
    except Exception:
        print("Downloading", url)
        response = requests.get(url, stream=True)
        try:
            s3.upload_fileobj(
                response.raw,
                BUCKET_NAME,
                image_name,
                ExtraArgs={
                    "ACL": acl,
                }
            )
        except Exception as e:
            # in case the our s3 upload fails
            return {"errors": str(e)}

    return bucket_url
