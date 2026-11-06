# Python API Practice

一个用于学习和实践 Python 接口自动化测试的练手项目。

项目目标是逐步实现一个结构清晰、可配置、可复用的接口测试工具，并最终迁移到 Pytest 接口自动化框架。

## 项目目标

- 使用 Python 调用 HTTP 接口
- 从配置文件读取测试环境信息
- 从 JSON 文件读取测试用例
- 支持 GET、POST 等请求
- 统一处理请求头和鉴权
- 记录请求日志和响应结果
- 输出结构化测试报告
- 后续迁移到 Pytest 自动化框架

## 当前进度

- [x] 创建 Python 虚拟环境
- [x] 创建项目目录结构
- [x] 添加配置文件 `config.yaml`
- [x] 使用 `PyYAML` 读取配置
- [x] 搭建最小运行入口 `run.py`
- [ ] 封装 `ApiClient`
- [ ] 支持批量执行测试用例
- [ ] 增加日志和测试报告
- [ ] 迁移到 Pytest
- [ ] 增加 Selenium 核心流程自动化
- [ ] 增加 JMeter 性能测试示例

## 技术栈

- Python 3.12
- Requests
- PyYAML
- Pytest，后续引入
- Selenium，后续引入

## 目录结构

python-api-practice/
├── config.yaml          # 环境配置：基础地址、超时时间、公共请求头
├── cases.json           # 接口测试用例
├── run.py               # 批量执行入口
├── src/                 # Python 代码
│   ├── api_client.py    # 接口请求封装
│   ├── data_loader.py   # 读取配置文件
│   └── logger.py        # 日志
├── reports/
│   └── result.json      # 执行结果
└── README.md            # 运行说明