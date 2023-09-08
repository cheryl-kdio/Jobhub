import requests
from tabulate import tabulate


class AdzunaJobSearch:
    def __init__(self, api_key, api_id, country="gb", page_number=1):
        self.api_key = api_key
        self.api_id = api_id
        self.country = country
        self.page_number = page_number
        self.base_url = "https://api.adzuna.com/v1/api/"
        self.endpoint = f"jobs/{country}/search/{page_number}"

    def make_request(self, query_params):
        params = {"app_id": self.api_id, "app_key": self.api_key, **query_params}

        response = requests.get(f"{self.base_url}{self.endpoint}", params=params)

        if response.status_code == 200:
            data = response.json()
            return data.get("results", [])
        else:
            print(
                f"Request failed with status code {response.status_code}: {response.text}"
            )
            return []

    def search_jobs(self, query_params):
        jobs = self.make_request(query_params)

        table_data = [
            {
                "id": i + 1,
                "Title": job.get("title", ""),
                "Company": job.get("company", {}).get("display_name", ""),
                "Location": job.get("location", {}).get("display_name", ""),
                "Minimum salary": job.get("salary_min", ""),
                "Maximum salary": job.get("salary_max", ""),
                "Category": job.get("category", {}).get("label", ""),
                "redirect_url": job.get("redirect_url", ""),
            }
            for i, job in enumerate(jobs)
        ]

        print(tabulate(table_data, headers="keys", tablefmt="pretty"))


# Example usage:
if __name__ == "__main__":
    api_key = "172efa229f7dfce6a99b4bf26b538ed7"
    api_id = "37f68c4e"

    job_search = AdzunaJobSearch(api_key, api_id)

    query_params = {
        "results_per_page": 20,
        "what": "python dev",
        # Add additional parameters as needed
        # "where": "london",
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

    job_search.search_jobs(query_params)
