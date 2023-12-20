import pytest
import allure
from app import get_json

@pytest.mark.asyncio
async def test_get_json_successful():
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = await get_json(url)
    assert "userId" in response

@allure.feature("Get JSON Feature")
@allure.story("Error Handling")
@pytest.mark.asyncio
async def test_get_json_with_invalid_url():
    url = "https://jsonplaceholder.typicode.com/invalid"
    with pytest.raises(aiohttp.ClientResponseError):
        await get_json(url)