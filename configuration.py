
import yaml
from pathlib import Path

def read_config():
    fpath = Path().cwd() / "config.yaml"

    with open(fpath) as f:
        config = yaml.load(f, yaml.Loader)
    return config

if __name__ == "__main__":
    read_config()
    config = read_config()
    print(config["mail"])
