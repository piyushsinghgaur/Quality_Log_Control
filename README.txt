# Log Query Interface

## Overview

The Log Query Interface is a web application designed to ingest and query logs stored in different log files. It provides users with a user-friendly interface to search for logs based on various criteria such as log level, log string, timestamp range, and source. The application consists of a backend built with Python Flask for log ingestion and querying, and a frontend developed with HTML, CSS, and JavaScript for the user interface.

## How to Run the Project

### Prerequisites
- Python 3.x installed on your system
- Flask library installed (`pip install Flask`)

### Steps
1. **Clone the Repository:**
   ```
   git clone https://github.com/your-username/log-query-interface.git
   cd log-query-interface
   ```

2. **Run the Backend:**
   ```
   python app.py
   ```
   The Flask server will start running on `http://localhost:5000`.

3. **Open the Frontend:**
   - Open `index.html` in a web browser.
   - The frontend will be displayed, allowing you to interact with the log query interface.

## System Design

The system consists of two main components:

1. **Backend (Python Flask):**
   - Handles log ingestion and querying.
   - Provides RESTful API endpoints for logging data (`/log`) and searching logs (`/search`).
   - Utilizes Python's `logging` module for writing logs to files.

2. **Frontend (HTML, CSS, JavaScript):**
   - Provides a user-friendly interface for querying logs.
   - Allows users to specify search criteria such as level, log string, timestamp range, and source.
   - Uses JavaScript to send AJAX requests to the backend API and display search results.

## Features Implemented

- Log ingestion API to accept POST requests and write logs to designated log files.
- Log querying API to search for logs based on various criteria.
- User interface with input fields for specifying search criteria and a button to trigger the search.
- Support for searching logs based on level, log string, timestamp range, and source.

## Identified Issues

- As of now, the application does not include authentication or authorization mechanisms.
- Error handling could be improved to provide more descriptive error messages to users.
- The frontend interface could be enhanced with additional features such as pagination and sorting of search results.

## Future Enhancements

- Implement real-time log ingestion and searching capabilities.
- Add support for role-based access control to restrict access to certain features based on user roles.
- Enhance error handling and validation to ensure robustness of the application.

---