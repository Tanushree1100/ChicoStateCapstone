# LitList : Beyond the cover

LitList is a simple web application that allows users to log and track the books they have read. Users can add new books, mark books as completed, and write reviews for the books they finish. The application provides a convenient way to organize and reflect on your reading experiences.

## Features

- **Book Tracking:** Log details of the books you are currently reading or have completed.
- **Review Writing:** Write and save reviews for the books you finish, including ratings and additional comments.
- **Genre Classification:** Categorize books into different genres for better organization.
- **Search Functionality:** Easily search and filter books based on title, author, or genre.
- **Mark as Completed:** Indicate when you have finished reading a book and move it to the completed books section.

## Getting Started

### Prerequisites

Make sure you have the following installed on your system:

- [Python](https://www.python.org/) (version 3.x)
- [Django](https://www.djangoproject.com/)
- [Git](https://git-scm.com/)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/book-logger.git
    ```

2. Navigate to the project directory:

    ```bash
    cd book-logger
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Apply migrations:

    ```bash
    python manage.py migrate
    ```

7. Create a superuser account:

    ```bash
    python manage.py createsuperuser
    ```

8. Start the development server:

    ```bash
    python manage.py runserver
    ```

9. Open your web browser and go to [http://localhost:8000/admin/](http://localhost:8000/admin/). Log in with the superuser credentials created earlier.

10. Start logging your books!

## Contributing

Contributions are welcome! If you have any suggestions, feature requests, or find any issues, please open an [issue](https://github.com/yourusername/book-logger/issues) or submit a [pull request](https://github.com/yourusername/book-logger/pulls).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
