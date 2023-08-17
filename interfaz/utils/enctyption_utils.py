from puntodeventa.settings import ENCRYPTION_KEY

from cryptography.fernet import Fernet

CYPHER = Fernet(bytes(ENCRYPTION_KEY, "utf-8"))


def encrypt_password(password: str) -> str:
    return CYPHER.encrypt(bytes(password, "utf-8")).decode("utf-8")


def decrypt_password(encp_password: str) -> str:
    return CYPHER.decrypt(bytes(encp_password, "utf-8")).decode("utf-8")