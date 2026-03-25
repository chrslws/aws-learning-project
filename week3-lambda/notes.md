# Week 3 – AWS Lambda

## What I Did

Created an AWS Lambda function using Python. Configured and deployed the function through the AWS console.
Tested the function using custom events and verified the output.

## What I Learned

I learned that AWS Lambda allows code to run without managing servers, which is known as serverless computing.
I also learned how Lambda functions take input via events and return structured responses.

## Problems Encountered

Initially I found the concept of event input confusing, particularly how to access values from the event object.
After experimenting, I learned to use event.get() to safely retrieve values.

## Key Concepts

- Serverless computing  
- Event-driven execution  
- Lambda handler function  
- Input/output structure  

## Example Input

{
  "name": "Chris"
}

## Example Output

Hello Chris, welcome to AWS Lambda