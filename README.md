# Azure-Function-App-for-Sorting-and-Searching-Operations

## Project Overview
The Azure Function App for Sorting and Searching Operations provides a cloud-based solution for performing sorting and searching algorithms. This project leverages Azure Functions to handle serverless, scalable sorting and searching operations, enabling quick deployment and efficient resource usage in the cloud environment. This app is designed for developers or businesses that need to process data efficiently without managing underlying server infrastructure.

## Features

Sorting: Supports bubble sorting algorithm.

Searching: Provides searching algorithms such as binary search.

Scalable: Uses Azure Functions for serverless execution, automatically scaling based on demand.

Efficient: Optimized code for handling large datasets with minimal latency.

## Technologies Used

Azure Functions: For creating and deploying serverless function apps.

Python: The core language for implementing sorting and searching algorithms.

Azure Portal: For managing and deploying the function app.

Visual Studio Code (with Azure Functions extension): For local development and testing.

## Setup Instructions

Azure Account: Create an Azure account if you don't have one here.

Python 3.x: Ensure Python is installed on your machine.

### Steps to Deploy the Azure Function App
Clone the Repository:

git clone https://github.com/your-username/Azure-Function-App-for-Sorting-and-Searching.git

cd Azure-Function-App-for-Sorting-and-Searching

Install the Azure Functions Core Tools: Follow the instructions from the Azure documentation to set up your development environment locally.

Install Python Dependencies: In the project directory, run:

pip install -r requirements.txt

Run Locally: Use the following command to run the function locally:

func start

Deploy to Azure: After testing locally, deploy the function to Azure:

func azure functionapp publish <YOUR_FUNCTION_APP_NAME>

### Usage
Once the Function App is deployed, it can handle HTTP requests for sorting and searching operations. The user can send a dataset along with a specified operation to be performed (e.g., sort or search).

Example Request:

curl -X POST https://<YOUR_FUNCTION_APP_NAME>.azurewebsites.net/api/sort \
-H "Content-Type: application/json" \
-d '{
    "data": [3, 1, 4, 1, 5, 9, 2],
    "algorithm": "quicksort"
}'

Example Response:

{
    "sorted_data": [1, 1, 2, 3, 4, 5, 9],
    "algorithm": "quicksort",
    "time_taken": "0.002s"
}

### API Endpoints

POST /sort: Accepts a dataset and sorting algorithm, returning the sorted data.

POST /search: Accepts a dataset and search key, returning the index or result of the search.

### Request Format
Both endpoints accept JSON requests with the following structure:

{
    "data": [Array of numbers],
    "algorithm": "Algorithm name"
}

### Testing
To test the function locally or via Azure, you can use tools like:

Postman: Send HTTP requests and check the responses.

curl: Use curl commands to interact with the API endpoints.

Example Postman setup:

1. Select POST request.

2. Enter the URL for the function.

3. In the body, choose raw format and input JSON data.

4. Send the request and review the response.

## Conclusion

The Azure Function App for Sorting and Searching Operations offers a scalable, efficient solution for performing complex data processing tasks in a serverless environment. By leveraging Azure Functions, users can handle large datasets with minimal infrastructure management, making it an ideal tool for cloud-based applications. Whether you need to sort massive lists or perform quick searches, this app provides flexibility and power, all within a streamlined, easy-to-deploy setup. We welcome contributions to enhance this project further and encourage developers to explore its potential for real-world applications.
