# Week 4 – API Gateway

## What I Did

This week I connected my AWS Lambda function to API Gateway in order to create a public HTTP endpoint.

I configured a GET route (/hello) and linked it to my Lambda function. I then tested the API through a browser using query parameters.

## What I Learned

I learned how API Gateway allows external users to interact with backend services via HTTP requests.

I also learned that Lambda functions must return responses in a specific format for APIs to work correctly.

## Problems Encountered

Initially, accessing the base API URL returned a "Not Found" message. I discovered that this was because routes must be explicitly defined, and the correct path (/hello) must be included.

I also encountered issues with response formatting, which caused errors until I structured the output correctly.

## Key Concepts

- API Gateway  
- HTTP routes  
- Query parameters  
- Integration with Lambda  

## Example Usage

/hello?name=Chris

## Example Output

Hello Chris, your API works!