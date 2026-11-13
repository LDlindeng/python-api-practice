from pathlib import Path

from src.data_loader import (
    DataLoadError,
    load_json_list,
    load_yaml,
    validate_cases,
)


ROOT_DIR = Path(__file__).resolve().parent


def main():
    try:
        config = load_yaml(ROOT_DIR / "config.yaml")
        cases = validate_cases(
            load_json_list(ROOT_DIR / "cases.json")
        )
    except DataLoadError as exc:
        print(f"数据加载失败: {exc}")
        return

    print("配置加载成功")
    print(f"测试环境: {config['base_url']}")
    print(f"超时时间: {config['timeout']} 秒")
    print(f"用例数量: {len(cases)}")
    print()

    for index, case in enumerate(cases, start=1):
        method = case["method"].upper()
        print(f"{index}. [{method}] {case['name']} -> {case['path']}")


if __name__ == "__main__":
    main()