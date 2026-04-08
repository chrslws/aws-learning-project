# Week 5 – DynamoDB Integration

## What I Did

This week I extended my AWS Lambda function to interact with a DynamoDB database.

I created a table and modified my API to allow storing and retrieving messages.

## What I Learned

I learned how DynamoDB works as a NoSQL database and how it integrates with AWS services.

I also learned how permissions must be explicitly configured using IAM roles.

## Problems Encountered

I encountered an internal server error when first testing the API. By checking CloudWatch logs, I identified that the issue was related to missing permissions and configuration errors.

After resolving these, I successfully connected Lambda to DynamoDB.

## Key Concepts

- DynamoDB tables and items  
- NoSQL databases  
- IAM roles and permissions  
- Persistent data storage  

## Example Usage

?action=add&text=hello  
?action=get  

## Example Output

["hello","world"]