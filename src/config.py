from pydantic import BaseSettings


class Settings(BaseSettings):
    DEFAULT_ENV = "OK"
    NAMESPACE:str
    APPLICATION:str
    TEST_ENV: str	

    class Config:
        env_file = "/etc/config/.env"
        #env_file = "../.env"
    


