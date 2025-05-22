import pytest
from types import SimpleNamespace
from bot.handlers import language_selected, echo_handler

class MockMessage:
    def __init__(self, text=None, document=None, user_id=1):
        self.text = text
        self.document = document
        self.from_user = SimpleNamespace(id=user_id)
        self.responses = []
        self.bot = SimpleNamespace(
            get_file=self.mock_get_file,
            download_file=self.mock_download_file
        )

    async def answer(self, text, reply_markup=None):
        self.responses.append(text)

    async def mock_get_file(self, file_id):
        return SimpleNamespace(file_path="dummy/path")

    async def mock_download_file(self, file_path, destination):
        destination.write(b"test content")

@pytest.mark.asyncio
async def test_language_selection():
    msg = MockMessage(text="English")
    await language_selected(msg)
    assert any("choose" in resp.lower() or "welcome" in resp.lower() for resp in msg.responses)

@pytest.mark.asyncio
async def test_file_upload():
    mock_doc = SimpleNamespace(file_name="test.txt", file_id="fake123")
    msg = MockMessage(document=mock_doc)
    await echo_handler(msg)
    assert any("saved" in resp.lower() or "backup" in resp.lower() for resp in msg.responses)
