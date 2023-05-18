import pytest

from src.tests.base_test import BaseTest
from src.tests.API.base_api_test import BaseAPITest

from src.api.models.menu.departments.menu_departments_model import MenuDepartmentsResponseSchema


@pytest.fixture
def base_api():
    base_api = BaseAPITest()
    yield base_api


@pytest.mark.api
@pytest.mark.usefixtures("base_api")
class TestDepartmentsEndpoint(BaseTest):

    def test_GET_menu_departments(self, base_api):
        response = base_api.send_request(
            method="GET",
            path="menu/departments",
            entity_schema=MenuDepartmentsResponseSchema()
        )

        assert response.status_code == 200
        assert len(response.body.departments) > 0
