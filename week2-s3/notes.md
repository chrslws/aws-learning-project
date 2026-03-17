# Week 2 – S3 Static Website Hosting

## What I Did

Created an S3 bucket and configured it to host a static website. Uploaded an HTML file and enabled static website hosting.

## What I Learned

I learned how AWS S3 works as an object storage system where files are stored as objects inside buckets.

I also learned that making content publicly accessible requires both disabling block public access and configuring a bucket policy.

## Problems Encountered

I initially struggled to make the website publicly accessible. I attempted to modify object-level permissions, but this did not work due to AWS enforcing bucket-level access control.

After further investigation, I resolved the issue by updating the bucket policy and disabling block public access.

## Key Concepts

- Buckets vs objects  
- Public vs private access  
- Static website hosting  
- Bucket policies  

## Website Link

http://chris-aws-learning-progblack.s3-website.eu-north-1.amazonaws.com