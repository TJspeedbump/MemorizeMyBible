from pydantic import BaseSettings

class Settings(BaseSettings):
    Database_Hostname: str
    Database_Port: int
    Database_Password: str
    Database_Username: str
    NLT_Database_Name: str
    NIV_Database_Name: str
    Users_Database_Name: str
    Secret_Key: str
    Algorithm: str
    Token_Access_Minutes: int


