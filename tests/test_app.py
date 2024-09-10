import sys
import os

# Add the root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import app, db

@pytest.fixture(scope='module')
def test_client():
    """Setup the test client and the test database."""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use an in-memory database for testing
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_create_task(test_client):
    """Test adding a new task."""
    response = test_client.post('/', data=dict(title="Test Task", desc="Test Description"))
    assert response.status_code == 200
    assert b"Test Task" in response.data

# def test_update_task(test_client):
#     """Test updating an existing task."""
#     # First, add a task
#     test_client.post('/', data=dict(title="Old Task", desc="Old Description"))

#     # Update the task
#     response = test_client.post('/update/1', data=dict(title="Updated Task", desc="Updated Description"))
#     print(response.data)
#     assert response.status_code == 302  # Redirect after POST

#     # Verify the update
#     response = test_client.get('/')
#     assert b"Updated Task" in response.data
#     assert b"Updated Description" in response.data

# def test_delete_task(test_client):
#     """Test deleting a task."""
#     # First, add a task
#     test_client.post('/', data=dict(title="Task to Delete", desc="Description"))

#     # Delete the task
#     response = test_client.get('/delete/1')
#     assert response.status_code == 302  # Redirect after DELETE

#     # Verify the deletion
#     response = test_client.get('/')
#     assert b"Task to Delete" not in response.data

# def test_show_tasks(test_client):
#     """Test the show all tasks endpoint."""
#     # Add some tasks
#     test_client.post('/', data=dict(title="Task 1", desc="Description 1"))
#     test_client.post('/', data=dict(title="Task 2", desc="Description 2"))

#     response = test_client.get('/show')
#     assert b"Task 1" in response.data
#     assert b"Task 2" in response.data

# #b"Task 1" is a byte string used to check if the task title "Task 1" appears in the response.
# #If you used a regular string ("Task 1"), it would cause a type mismatch because you can't compare a byte string (response.data) with a Unicode string ("Task 1").
