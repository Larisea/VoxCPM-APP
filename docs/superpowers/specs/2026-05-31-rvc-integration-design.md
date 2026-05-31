# RVC翻唱功能集成设计文档

## 目标

将RVC（Retrieval-based Voice Conversion）完整集成到VoxCPM Web界面，实现从录制、训练到翻唱的完整流程。

## 架构设计

```
VoxCPM Web Server (port 8868)
├── /api/rvc/status → 检测RVC WebUI是否运行
├── /api/rvc/upload_audio → 上传音频到RVC训练目录
├── /api/rvc/train → 启动RVC训练任务
├── /api/rvc/training_status → 查询训练状态
├── /api/rvc/models → 列出已训练模型
├── /api/rvc/delete_model → 删除模型
├── /api/rvc/voice_change → 翻唱生成
└── 前端向导界面 (4步流程)

RVC WebUI (port 7865)
├── POST /api/train → 训练API
├── POST /api/voice_change → 推理API
└── GET /api/models → 模型列表
```

## 核心模块

### 1. RVC API客户端 (`server/rvc_client.py`)
- `check_rvc_status()` → 检测RVC WebUI运行状态
- `upload_audio_to_rvc(audio_path)` → 上传音频到RVC
- `start_training(audio_path, model_name)` → 启动训练
- `get_training_status()` → 获取训练状态
- `list_models()` → 列出可用模型
- `delete_model(model_name)` → 删除模型
- `voice_change(audio_path, model_name, params)` → 翻唱生成

### 2. API路由 (`server/routes.py`)
新增路由：
- `GET /api/rvc/status` → RVC状态检测
- `POST /api/rvc/upload_audio` → 上传音频
- `POST /api/rvc/train` → 启动训练
- `GET /api/rvc/training_status` → 训练状态
- `GET /api/rvc/models` → 模型列表
- `DELETE /api/rvc/models/{name}` → 删除模型
- `POST /api/rvc/voice_change` → 翻唱生成

### 3. 前端向导界面
4步向导流程：
1. **录制** → 上传/录制干声音频
2. **训练** → 选择音频、输入模型名、开始训练
3. **模型** → 查看训练状态、选择模型
4. **翻唱** → 上传歌曲、选择模型、生成翻唱

## 数据流

```
录制音频 → 上传到RVC → 启动训练 → 监控训练 → 选择模型 → 上传歌曲 → 翻唱生成 → 下载结果
```

## 测试策略

### 单元测试
- RVC API客户端测试（模拟RVC响应）
- 路由处理函数测试
- 前端JavaScript函数测试

### 集成测试
- 完整流程测试（需要RVC WebUI运行）
- 错误处理测试（RVC未运行时）

## 实现计划

1. 先写测试
2. 实现RVC API客户端
3. 添加API路由
4. 实现前端向导界面
5. 集成测试
