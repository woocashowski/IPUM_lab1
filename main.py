import os
import argparse
import yaml
import subprocess
from dotenv import load_dotenv
from settings import Settings


def export_envs(environment: str = "dev") -> None:
    env_file = f"config/.env.{environment}"
    if os.path.exists(env_file):
        load_dotenv(env_file)
    else:
        raise FileNotFoundError(f"Brak pliku {env_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--environment", type=str, default="dev")
    args = parser.parse_args()

    export_envs(args.environment)

    # DEKRYPTUJ I ŁADUJ SECRETS
    if os.path.exists("secrets.yaml"):
        subprocess.run(
            ["sops", "--decrypt", "--in-place", "secrets.yaml"], capture_output=True
        )
        with open("secrets.yaml") as f:
            data = yaml.safe_load(f)
        for k, v in data.items():
            os.environ[k] = v

    settings = Settings()
    print("APP_NAME:", settings.APP_NAME)
    print("ENVIRONMENT:", settings.ENVIRONMENT)
    print("API_KEY:", settings.API_KEY)
    print("DATABASE_PASSWORD:", settings.DATABASE_PASSWORD)
