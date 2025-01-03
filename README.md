****Basic Flask Application with GitHub Actions & Docker Integration****

Overview

This repository contains the code for a basic Flask application that demonstrates the usage of classes and objects in Python. Additionally, the repository showcases how to create a GitHub Actions workflow to build and publish a Docker image. The Flask app provides APIs for currency exchange and weather data using external services.

Features

	•	Flask Web Application: A simple Flask application showcasing the use of classes and objects.
	•	Currency Exchange API: Fetches currency conversion rates from an external API.
	•	Weather API: Fetches weather data from an external API.
	•	GitHub Actions Workflow: Automatically builds and publishes a Docker image for the Flask app.
	•	Docker Integration: The project is containerized using Docker for easier deployment and scalability.

Requirements

Before running the application, make sure you have the following tools installed on your local machine:
	•	Python 3.x
	•	Flask
	•	Docker (for building the container image)
	•	GitHub account (for setting up workflows)
	•	Virtual environment tool (like venv or virtualenv)

Setup & Installation

Clone the Repository
git clone https://github.com/yourusername/repo-name.git
cd repo-name
Install Dependencies

Make sure to install the required dependencies for the Flask app:
pip install -r requirements.txt

Create secret.json File

For security reasons, the repository uses a secret.json file to store tokens for external services. Create this file with the following format:
{
    "currency_api_token": "YOUR_CURRENCY_API_TOKEN",
    "weather_api_token": "YOUR_WEATHER_API_TOKEN"
}
Replace "YOUR_CURRENCY_API_TOKEN" and "YOUR_WEATHER_API_TOKEN" with your actual API tokens from the services.


Running the Application

Once all dependencies are installed and the secret.json file is created, you can run the application using:
python app.py

The application will start running locally on http://127.0.0.1:5000.


API Endpoints

Currency Check API

The API for checking currency conversion rates can be accessed via the following URL:

http://127.0.0.1:5001/forex/<from_currency>/<to_currency>

	•	from_currency: The currency you are converting from (e.g., USD, EUR).
	•	to_currency: The currency or currencies you are converting to. Multiple currencies can be provided by separating them with commas (e.g., USD,EUR,JPY).
Example:

To convert from USD to EUR and JPY: 
http://127.0.0.1:5001/forex/USD/EUR,JPY

GitHub Actions Workflow

This repository contains a GitHub Actions workflow that automates the process of building and publishing a Docker image. Once set up, every time code is pushed to the repository, the workflow will automatically trigger and:
	1.	Build the Docker image.
	2.	Publish the Docker image to a container registry (e.g., Docker Hub).

To view and configure the workflow, navigate to .github/workflows directory in the repository.



Documentation for External APIs

The following external APIs are used in the application:
	1.	Currency Data API: Provides currency conversion rates.
Documentation: Currency Data API
	2.	WeatherStack API: Provides weather data for different locations.
Documentation: WeatherStack API

Make sure you sign up for these services and obtain your API tokens to integrate them into the application.

Conclusion

This repository provides a simple but powerful example of how to integrate Flask with external APIs, use GitHub Actions for CI/CD, and containerize an application with Docker.
