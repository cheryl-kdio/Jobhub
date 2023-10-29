# Packages used: tkinter, tkinter.ttk, requests
import tkinter as tk
from tkinter import ttk
import requests

# Create the main application window
app = tk.Tk()
app.title("JobHub")

# My API key and ID
api_key = "6beb9a3e95cede40d2a6a7c58bb22764"
api_id = "9b48e28e"

# Create and pack a frame for search parameters
search_frame = ttk.LabelFrame(app, text="Search Parameters")
search_frame.grid(row=1, column=0, padx=10, pady=10, sticky="w")

# Define variable for country, endpoint, and page number
page_number = 1
country_var = tk.StringVar()  # Variable to store selected country
country_var.set("gb")  # Set the default country

# What and Where labels and entry fields
what_label = ttk.Label(search_frame, text="Job Title/Keyword:")
what_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
what_entry = ttk.Entry(search_frame, width=40)
what_entry.grid(row=0, column=1, padx=5, pady=5)

where_label = ttk.Label(search_frame, text="Location:")
where_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
where_entry = ttk.Entry(search_frame, width=40)
where_entry.grid(row=1, column=1, padx=5, pady=5)

# Country label and Combobox
country_label = ttk.Label(search_frame, text="Country:")
country_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
country_combobox = ttk.Combobox(
    search_frame,
    textvariable=country_var,
    values=[
        "gb",
        "us",
        "fr",
        "at",
        "au",
        "br",
        "be",
        "ca",
        "ch",
        "de",
        "es",
        "in",
        "it",
        "nl",
        "nz",
        "pl",
        "ru",
        "sg",
        "za",
        "mx",
    ],
)  # Add more countries as needed
country_combobox.grid(row=2, column=1, padx=5, pady=5)

# Create a Treeview widget to display the results
results_tree = ttk.Treeview(
    app,
    columns=(
        "Title",
        "Company",
        "Location",
        "Min Salary",
        "Max Salary",
        "Category",
        "Created",
    ),
)
results_tree.heading("#1", text="Title")
results_tree.heading("#2", text="Company")
results_tree.heading("#3", text="Location")
results_tree.heading("#4", text="Min Salary")
results_tree.heading("#5", text="Max Salary")
results_tree.heading("#6", text="Category")
results_tree.heading("#7", text="Created")
results_tree.grid(row=2, column=0, padx=10, pady=10, sticky="w")


# Create a function to make the API request and populate the Treeview widget
def make_api_request():
    # Clear previous results
    for item in results_tree.get_children():
        results_tree.delete(item)

    # Get API credentials and search parameters from the entry fields
    search_what = what_entry.get()
    search_where = where_entry.get()
    selected_country = country_var.get()

    # Set the base URL and endpoint
    base_url = "https://api.adzuna.com/v1/api/"
    endpoint = f"jobs/{selected_country}/search/{page_number}"

    # Define your query parameters
    params = {
        "app_id": api_id,
        "app_key": api_key,
        "results_per_page": 10,
        "what": search_what,
        "where": search_where,
    }

    # Make the API request
    response = requests.get(f"{base_url}{endpoint}", params=params)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()

        # Extract the relevant job data from the JSON response and populate the Treeview
        jobs = data.get("results", [])
        for job in jobs:
            results_tree.insert(
                "",
                "end",
                values=(
                    job.get("title", ""),
                    job.get("company", {}).get("display_name", ""),
                    job.get("location", {}).get("display_name", ""),
                    job.get("salary_min", ""),
                    job.get("salary_max", ""),
                    job.get("category", {}).get("label", ""),
                    job.get("created", ""),
                ),
            )

    else:
        error_message = (
            f"Request failed with status code {response.status_code}: {response.text}"
        )
        print(error_message)


# Create and pack a button to trigger the API request
search_button = ttk.Button(search_frame, text="Search", command=make_api_request)
search_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10)

# Start the GUI main loop
app.mainloop()
