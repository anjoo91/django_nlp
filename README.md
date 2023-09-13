# WebNLP
# Live Link: 
https://django-nlp-fdc565844cf0.herokuapp.com

## Overview

This project integrates Natural Language Processing (NLP) with web development using Django. It provides a web interface to perform various NLP tasks such as Regular Expressions, Lemmatization, Part of Speech Tagging, and Named Entity Recognition.

## Features

- **Home Page**: Provides an introduction to NLP and the tasks you can perform.
- **Regular Expressions**: Extracts US phone numbers from the text.
- **Lemmatization**: Reduces words to their base or root form.
- **Part of Speech Tagging**: Tags each word in the text with its corresponding part of speech.
- **Named Entity Recognition**: Identifies entities like names, organizations, locations, etc., in the text.

## Technologies Used

- Django
- Python
- Bootstrap
- HTML, CSS, JavaScript
- spaCy
- Natural Language Processing
- MVT Framework (Django)
- Heroku

## Setup

1. Clone the repository:
   ```bash
   git clone <repository_url>
   ```
2. Navigate to the project directory:
   ```bash
   cd django_nlp
   ```
3. Install dependencies using Poetry:
   ```bash
   poetry install
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the development server:
   ```bash
   python manage.py runserver
   ```

## Deployment

The project is deployed on Heroku. Follow the Heroku deployment guide for Django applications to deploy your own version.

## Contributing

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them.
4. Push to your fork.
5. Create a pull request.


## Author

- anjoo91