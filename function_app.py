import azure.functions as func
import logging
import json
import requests

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION) #sets up a new function app with HTTP security that requires a specific key to access its functions.

# app = app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS) --> sets up a new function app where anyone can access its functions without needing a key or any special permissions.

# app = func.FunctionApp(http_auth_level=func.AuthLevel.ADMIN) --> sets up a new function app where only users with an administrative key can access its functions, ensuring a high level of security.

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst

def binary_search(array, target):
    
    start = 0
    end = len(array) - 1

    while start <= end:
        middle = (start + end) // 2
        #print(f"Checking middle index {middle}, value {array[middle]}")

        if array[middle] == target:
            #print(f"Found target {target} at index {middle}")
            return middle
        elif array[middle] < target:
            #print(f"Target {target} is greater than {array[middle]}")
            start = middle + 1
        else:
            #print(f"Target {target} is less than {array[middle]}")
            end = middle - 1

    #print("Target not found")
    return -1

@app.route(route="bubble")
def bubble(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        list_items = req.params.get('arr') # retrieves a parameter named 'arr' from the query parameters of the HTTP request.
        list_items = json.loads(list_items) # converts the retrieved parameter (which is a JSON string) into a Python list using the json.loads function.
        
        if list_items is None:
            return func.HttpResponse("Please pass a list of integers in the request body.",
                                     status_code=400 # Bad Request: The request was invalid due to malformed syntax or incorrect parameters, and the server could not process it.
                                     )
        
        sorted_list = bubble_sort(list_items)

        return func.HttpResponse(
            str(sorted_list),
            # json.dumps(sorted_list) --> Converts the sorted Python list back to a JSON string for proper JSON formatting in the response.
            status_code=200, # OK: The request was successful and the server returned the requested resource.
            mimetype="application/json" #used to specify the media type of the content being sent or received in an HTTP request or response. In this case, it indicates that the content is in JSON (JavaScript Object Notation) format.
        )
    
    except ValueError:
        return func.HttpResponse("Invalid input. Please pass a JSON object with a 'list' field containing integers.",
            status_code=400
        )
    
@app.route(route="binarysearch")
def binarysearch(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    try:
        inputArray = req.params.get('arr')
        
        searchItem = req.params.get('target')
        searchItem = int(searchItem)

        url = 'https://bubble-sort.azurewebsites.net/api/bubble?code=qqzircSy5xrgH3Fo5-MxFU2FLWsrQXK-yQ74-xD2DlgFAzFulpUI4A%3D%3D&arr=' + inputArray
        response = requests.get(url)
        response = json.loads(response.content)
        
        result = binary_search(response, searchItem)
        if result > -1:
            return func.HttpResponse(f" Searched item {searchItem} found at index {result}",status_code=200)
        else:
            return func.HttpResponse(f" Searched item {searchItem} not found!",status_code=200)
        
    except ValueError:
        return func.HttpResponse("Invalid input. Please pass a JSON object with a 'list' field containing integers.",
            status_code=400
        )
    

