import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from django_testing import settings
from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def url():
    return '/api/v1/courses/'