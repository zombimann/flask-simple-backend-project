## Flask Simple Backend Project

This is a simple Flask backend project that provides basic CRUD (Create, Read, Update, Delete) functionality for managing books. It includes a Flask API with endpoints to create, retrieve, update, and delete books.

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   ```

2. Navigate to the project directory:
   ```
   cd flask-simple-backend-project
   ```

3. (Optional) Create a virtual environment:
   ```
   python3 -m venv venv
   ```

4. Activate the virtual environment:
   - For Windows:
     ```
     venv\Scripts\activate
     ```
   - For Unix/macOS:
     ```
     source venv/bin/activate
     ```

5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

### Configuration

The project uses a configuration file `app/config.py` to manage settings. You can modify the configuration according to your needs. By default, it uses an SQLite database for testing purposes. If you want to use a different database, modify the `SQLALCHEMY_DATABASE_URI` setting in the configuration file.

### Usage

To start the Flask server, run the following command:
```
python api.py
```

This will start the server at `http://localhost:5000/`.

### API Endpoints

The following API endpoints are available:

- `POST /books` - Create a new book
- `GET /books` - Get all books
- `GET /books/<book_id>` - Get a specific book
- `PUT /books/<book_id>` - Update a specific book
- `DELETE /books/<book_id>` - Delete a specific book

### Example Usage

#### Create a new book

**Request:**
```
POST /books

{
  "title": "Book Title",
  "author": "Book Author"
}
```

**Response:**
```
HTTP/1.1 201 Created

{
  "id": 1,
  "title": "Book Title",
  "author": "Book Author"
}
```

#### Get all books

**Request:**
```
GET /books
```

**Response:**
```
HTTP/1.1 200 OK

[
  {
    "id": 1,
    "title": "Book Title",
    "author": "Book Author"
  },
  {
    "id": 2,
    "title": "Another Book",
    "author": "Another Author"
  }
]
```

#### Get a specific book

**Request:**
```
GET /books/1
```

**Response:**
```
HTTP/1.1 200 OK

{
  "id": 1,
  "title": "Book Title",
  "author": "Book Author"
}
```

#### Update a specific book

**Request:**
```
PUT /books/1

{
  "title": "Updated Title",
  "author": "Updated Author"
}
```

**Response:**
```
HTTP/1.1 200 OK

{
  "id": 1,
  "title": "Updated Title",
  "author": "Updated Author"
}
```

#### Delete a specific book

**Request:**
```
DELETE /books/1
```

**Response:**
```
HTTP/1.1 200 OK

{
  "message": "Book deleted"
}
```

### Testing

The project includes unit tests to ensure the functionality is working as expected. To run the tests, use the following command:
```
python -m unittest discover tests
```

Sure! Here's the updated README.md with the added deployment instructions:

```markdown
# Flask Backend Project

This is a simple Flask backend project that provides a RESTful API for managing books.

## Deployment to Google Cloud Platform (GCP)

To automate the deployment of the Flask backend project to Google Cloud Platform (GCP), you can use the Cloud Run service, which allows you to run stateless, containerized applications on a fully managed serverless platform. Below is an example YAML configuration for deploying the Flask backend project to Cloud Run:

```yaml
# cloudbuild.yaml

steps:
  # Build the container image
  - name: 'gcr.io/cloud-builders/docker'
    args: ['build', '-t', 'gcr.io/$PROJECT_ID/flask-backend', '.']

  # Push the container image to Google Container Registry
  - name: 'gcr.io/cloud-builders/docker'
    args: ['push', 'gcr.io/$PROJECT_ID/flask-backend']

  # Deploy the container image to Cloud Run
  - name: 'gcr.io/cloud-builders/gcloud'
    args:
      - 'run'
      - 'deploy'
      - 'flask-backend'
      - '--image'
      - 'gcr.io/$PROJECT_ID/flask-backend'
      - '--platform'
      - 'managed'
      - '--region'
      - 'us-central1'
      - '--allow-unauthenticated'

images:
  - 'gcr.io/$PROJECT_ID/flask-backend'
```

Make sure to replace `$PROJECT_ID` with your actual GCP project ID in the YAML file.

To deploy the Flask backend project to Cloud Run using the YAML configuration:

1. Ensure that you have the Cloud SDK (`gcloud`) installed and configured on your local machine.

2. Save the above YAML configuration as `cloudbuild.yaml` in the root directory of your project.

3. Open a terminal or command prompt and navigate to the project's root directory.

4. Run the following command to initiate the deployment using Cloud Build:
   ```shell
   gcloud builds submit --config cloudbuild.yaml .
   ```

   This command triggers a Cloud Build, which builds the container image, pushes it to Google Container Registry, and deploys it to Cloud Run.

5. After the build and deployment process completes, you will see the Cloud Run service URL in the output. You can access your Flask backend application using that URL.

Note: Before deploying, ensure that you have the necessary permissions and have enabled the Cloud Run and Container Registry APIs for your project.

## License

This project is licensed under the [MIT License](LICENSE).
