import pytest
from authenticator import Authenticator
from unittest.mock import MagicMock

@pytest.fixture
def authenticator():
    auth = Authenticator()
    yield auth
    auth.users.clear()

def test_register(authenticator):
    authenticator.register("user1", "password1")
    assert "user1" in authenticator.users
    assert authenticator.users["user1"] == "password1"

    with pytest.raises(ValueError, match="エラー: ユーザーは既に存在します。"):
        authenticator.register("user1", "password2")

def test_login(authenticator):
    authenticator.register("user1", "password1")
    
    assert authenticator.login("user1", "password1") == "ログイン成功"

    with pytest.raises(ValueError, match="エラー: ユーザー名またはパスワードが正しくありません。"):
        authenticator.login("user1", "wrongpassword")
