from typing import Any, Dict
from interfaz.models import User
from interfaz.utils.enctyption_utils import decrypt_password


def auth_user(credentials: Dict[str, Any]):

    user = User.objects.get(
        username=credentials["username"]
    )

    assert credentials["password"] == decrypt_password(user.password)

