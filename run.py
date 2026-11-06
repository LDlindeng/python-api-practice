from pathlib import Path
import yaml


ROOT_DIR = Path(__file__).resolve().parent


def load_config():
    config_path = ROOT_DIR / "config.yaml"
    with config_path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main():
    config = load_config()
    print("配置文件读取成功")
    print(f"base_url: {config['base_url']}")
    print(f"timeout: {config['timeout']}")
    print(f"headers: {config['headers']}")


if __name__ == "__main__":
    main()