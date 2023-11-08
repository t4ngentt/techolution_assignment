
# Resume Parsing Application

This is a Python application for matching job descriptions with resumes using NLP. Here are the steps to set it up:

## Installation

1. Clone this repository to your local machine.

2. Open a terminal in the cloned folder and run the following command to install the required Python packages:

```shell
pip install -r requirements.txt
```

3. Download the necessary spaCy NLP models by running the following commands in your terminal:

```shell
python -m spacy download en_core_web_lg
python -m spacy download en_core_web_sm
```

4. Start the FastAPI server by running the following command in the terminal:

```shell
uvicorn main:app --reload
```

The first run of the application may take a while because it downloads all required NLP models.

## Database Operations

- To add resumes to the database, visit `index.html`.
- To remove all resumes from the current database, visit `delete.html`.

Note: These commands can also be accessed via the FastAPI documentation.

## Using the API

1. Go to [http://localhost:8000/docs/](http://localhost:8000/docs/) in your web browser.

2. Navigate to the 'initiatequery api' section.

3. Click 'Try it out' and add the desired job description. Execute the request.

Alternatively, you can use URL encoding to send API requests. For example:

```shell
http://127.0.0.1:8000/initiatequery?job_desc=okay%20123%20test
```

That's it! You now have the Resume Matching Application up and running locally.
```

Feel free to customize this README to include any additional information or details specific to your project.
