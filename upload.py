import boto3
import os
import requests

BUCKET_NAME = os.environ.get("S3_BUCKET")
S3_LOCATION = f"https://{BUCKET_NAME}.s3.amazonaws.com/"

s3 = boto3.client(
    "s3",
    aws_access_key_id=os.environ.get("S3_KEY"),
    aws_secret_access_key=os.environ.get("S3_SECRET")
)


def upload_image_to_bucket(url, acl="public-read"):
    response = requests.get(url, stream=True)
    image_name = os.path.basename(url)
    try:
        s3.upload_fileobj(
            response.raw,
            BUCKET_NAME,
            image_name,
            ExtraArgs={
                "ACL": acl
            }
        )
    except Exception as e:
        # in case the our s3 upload fails
        return {"errors": str(e)}

    return f"{S3_LOCATION}{image_name}"
