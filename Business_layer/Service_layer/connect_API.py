import requests
from tabulate import tabulate

# My API key and ID
api_key = "172efa229f7dfce6a99b4bf26b538ed7"
api_id = "37f68c4e"

# Define variable for country, endpoint and page number
page_number = 1
country = "gb"

# Set the base URL and endpoint : Adzuna API - Job Search
base_url = "https://api.adzuna.com/v1/api/"
endpoint = f"jobs/{country}/search/{page_number}"

# Definition of variables for the query
# TO DO

# Define your query parameters
params = {
    "app_id": api_id,
    "app_key": api_key,
    "results_per_page": 20,
    "what": "python dev",
    # "where": "london",
    # Add additional parameters as needed
    # "sort_direction": "up",
    # "sort_by": "relevance",
    # "category": "IT Jobs",
    # "distance": 10,
    # "salary_min": 50000,
    # "salary_max": 100000,
    # "permanent": "1",
    # "part_time": "0",
    # "full_time": "1",
    # "contract": "0",
}


# Make the API request
response = requests.get(f"{base_url}{endpoint}", params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    # Extract the relevant job data from the JSON response
    jobs = data.get("results", [])

    # Create a list of dictionaries to represent the table data
    table_data = [
        {
            "id": i + 1,
            "Title": job.get("title", ""),
            "Company": job.get("company", {}).get("display_name", ""),
            "Location": job.get("location", {}).get("display_name", ""),
            "Minimum salary": job.get("salary_min", ""),
            "Maximum salary": job.get("salary_max", ""),
            "Category": job.get("category", {}).get("label", ""),
            # "description": job.get("description", ""),
            # "created": job.get("created", ""),
            "redirect_url": job.get("redirect_url", ""),
        }
        for i, job in enumerate(jobs)
    ]

    # Display the data in a pretty table
    print(tabulate(table_data, headers="keys", tablefmt="pretty"))
else:
    print(f"Request failed with status code {response.status_code}: {response.text}")
