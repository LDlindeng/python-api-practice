from pathlib import Path
import json
import yaml


BASE_DIR = Path(__file__).resolve().parent.parent


class DataLoadError(Exception):
    """配置或测试数据加载异常"""


def resolve_path(file_path):
    path = Path(file_path)
    if path.is_absolute():
        return path
    return BASE_DIR / path


def load_yaml(file_path):
    path = resolve_path(file_path)

    try:
        with path.open("r", encoding="utf-8") as file:
            data = yaml.safe_load(file)
    except FileNotFoundError as exc:
        raise DataLoadError(f"YAML 文件不存在: {path}") from exc
    except yaml.YAMLError as exc:
        raise DataLoadError(f"YAML 格式错误: {path}\n{exc}") from exc

    if not isinstance(data, dict):
        raise DataLoadError(f"YAML 内容必须是字典: {path}")

    return data


def load_json_list(file_path):
    path = resolve_path(file_path)

    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as exc:
        raise DataLoadError(f"JSON 文件不存在: {path}") from exc
    except json.JSONDecodeError as exc:
        raise DataLoadError(
            f"JSON 格式错误: {path}\n"
            f"第 {exc.lineno} 行，第 {exc.colno} 列，{exc.msg}"
        ) from exc

    if not isinstance(data, list):
        raise DataLoadError(f"JSON 内容必须是列表: {path}")

    return data


def validate_cases(cases):
    required_fields = {"name", "method", "path", "expected_status"}
    allowed_methods = {"GET", "POST", "PUT", "PATCH", "DELETE"}

    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            raise DataLoadError(f"第 {index} 条用例必须是对象")

        missing_fields = required_fields - case.keys()
        if missing_fields:
            raise DataLoadError(
                f"第 {index} 条用例缺少字段: {sorted(missing_fields)}"
            )

        method = str(case["method"]).upper()
        if method not in allowed_methods:
            raise DataLoadError(
                f"第 {index} 条用例的请求方法不支持: {case['method']}"
            )

        if not isinstance(case["expected_status"], int):
            raise DataLoadError(
                f"第 {index} 条用例的 expected_status 必须是整数"
            )

    return cases