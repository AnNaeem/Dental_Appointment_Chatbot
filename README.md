# Dental Clinic Appointment Booking Assistant

## Overview

This project is a Streamlit-based AI assistant that simulates booking dental appointments. It utilizes LangChain and the Ollama model to handle natural language understanding and provide a conversational interface for scheduling appointments.

## Features

- **Natural Language Processing**: Uses LangChain with the Ollama model to understand and process user input.
- **Interactive UI**: Built with Streamlit to provide an easy-to-use interface for booking appointments.
- **Appointment Simulation**: Simulates booking an appointment by collecting user details and providing confirmation.

## Requirements

- Python 3.7 or higher
- Streamlit
- LangChain
- DateTime

## Setup and Installation

### 1. Install Python Packages

First, ensure you have Python 3.7 or higher installed on your system. Then, install the required packages using pip:

```
pip install streamlit Langchain
```
# Dental Clinic Appointment Booking Assistant

## Overview

This project is a Streamlit-based AI assistant that simulates booking dental appointments. It utilizes LangChain and the Ollama model to handle natural language understanding and provide a conversational interface for scheduling appointments.

## Features

- **Natural Language Processing**: Uses LangChain with the Ollama model to understand and process user input.
- **Interactive UI**: Built with Streamlit to provide an easy-to-use interface for booking appointments.
- **Appointment Simulation**: Simulates booking an appointment by collecting user details and providing confirmation.

## Requirements

- Python 3.7 or higher
- Streamlit
- LangChain
- DateTime

## Setup and Installation

### 1. Install Python Packages

First, ensure you have Python 3.7 or higher installed on your system. Then, install the required packages using pip:

```
pip install streamlit langchain
```
2. Install Additional Required Packages

```
pip install datetime
```
3. Install LangChain Specific Models
Ensure you have access to the coderindajungle/llama-3b-8b model for the Ollama class. This might require additional configuration depending on the model's availability.

4. Clone the Repository
Clone this repository to your local machine:
```
git clone https://github.com/your-username/dental-appointment-assistant.git
cd dental-appointment-assistant
```
5. Save the Code
Save the provided Python code into a file named app.py.

6. Run the Streamlit App
Navigate to the directory containing app.py and run the Streamlit app using:
```
streamlit run app.py
```
Usage
  1.	Open the App: Once you run the app, it will open in your default web browser.
  2.	Enter Your Name: Provide your name when prompted.
  3.	Book an Appointment: Enter the details for the appointment including date and time.
  4.	Confirm: Review the appointment details and confirm the booking.

Conversation Flow
  1.	Greeting: The assistant greets the user and asks for their name.
  2.	Collecting Details: The user provides their name, and the assistant asks for the date and time of the appointment.
  3.	Confirmation: The user selects the date and time, and the assistant confirms the appointment with a message.

Code Structure
* app.py: Main Python script that sets up the LangChain conversational model, Streamlit UI, and handles appointment booking.
* streamlit: Provides the interactive web interface.
* langchain: Handles natural language understanding and response generation.
* datetime: Manages date and time for appointments.

Code Quality
* Structured Code: Well-organized code with separate functions and classes for readability and maintenance.
* Best Practices: Followed best practices for Python development and Streamlit usage.
* Documentation: Clear and concise documentation explaining setup, functionality, and code structure.

# Contributing 
* Feel free to submit issues or pull requests to improve the project. Please follow the standard GitHub contribution guidelines.
* License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or feedback, please contact ansarinaeem236@gmail.com

