"""RVC API客户端测试"""
import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from server.rvc_client import (
    check_rvc_status,
    upload_audio_to_rvc,
    start_training,
    get_training_status,
    list_models,
    delete_model,
    voice_change
)


@pytest.fixture
def mock_rvc_url():
    """模拟RVC WebUI URL"""
    return "http://localhost:7865"


@pytest.mark.asyncio
async def test_check_rvc_status_success(mock_rvc_url):
    """测试RVC状态检测成功"""
    with patch('httpx.AsyncClient.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        result = await check_rvc_status()
        assert result["status"] == "online"
        assert result["url"] == mock_rvc_url


@pytest.mark.asyncio
async def test_check_rvc_status_offline(mock_rvc_url):
    """测试RVC状态检测失败（离线）"""
    with patch('httpx.AsyncClient.get') as mock_get:
        mock_get.side_effect = Exception("Connection refused")
        
        result = await check_rvc_status()
        assert result["status"] == "offline"
        assert "error" in result


@pytest.mark.asyncio
async def test_upload_audio_to_rvc_success(mock_rvc_url, tmp_path):
    """测试上传音频到RVC成功"""
    audio_file = tmp_path / "test.wav"
    audio_file.write_bytes(b"fake audio data")
    
    with patch('httpx.AsyncClient.post') as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "success", "path": "/data/test.wav"}
        mock_post.return_value = mock_response
        
        result = await upload_audio_to_rvc(str(audio_file))
        assert result["status"] == "success"
        assert "path" in result


@pytest.mark.asyncio
async def test_upload_audio_to_rvc_failure(mock_rvc_url, tmp_path):
    """测试上传音频到RVC失败"""
    audio_file = tmp_path / "test.wav"
    audio_file.write_bytes(b"fake audio data")
    
    with patch('httpx.AsyncClient.post') as mock_post:
        mock_post.side_effect = Exception("Upload failed")
        
        result = await upload_audio_to_rvc(str(audio_file))
        assert result["status"] == "error"
        assert "error" in result


@pytest.mark.asyncio
async def test_start_training_success(mock_rvc_url):
    """测试启动训练成功"""
    with patch('httpx.AsyncClient.post') as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "training_started", "task_id": "123"}
        mock_post.return_value = mock_response
        
        result = await start_training("/data/test.wav", "test_model")
        assert result["status"] == "training_started"
        assert "task_id" in result


@pytest.mark.asyncio
async def test_start_training_failure(mock_rvc_url):
    """测试启动训练失败"""
    with patch('httpx.AsyncClient.post') as mock_post:
        mock_post.side_effect = Exception("Training failed")
        
        result = await start_training("/data/test.wav", "test_model")
        assert result["status"] == "error"
        assert "error" in result


@pytest.mark.asyncio
async def test_get_training_status_success(mock_rvc_url):
    """测试获取训练状态成功"""
    with patch('httpx.AsyncClient.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "training",
            "progress": 50,
            "epoch": 100,
            "total_epochs": 200
        }
        mock_get.return_value = mock_response
        
        result = await get_training_status()
        assert result["status"] == "training"
        assert result["progress"] == 50


@pytest.mark.asyncio
async def test_list_models_success(mock_rvc_url):
    """测试列出模型成功"""
    with patch('httpx.AsyncClient.get') as mock_get:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "models": [
                {"name": "model1.pth", "size": 1024},
                {"name": "model2.pth", "size": 2048}
            ]
        }
        mock_get.return_value = mock_response
        
        result = await list_models()
        assert len(result["models"]) == 2
        assert result["models"][0]["name"] == "model1.pth"


@pytest.mark.asyncio
async def test_delete_model_success(mock_rvc_url):
    """测试删除模型成功"""
    with patch('httpx.AsyncClient.delete') as mock_delete:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"status": "deleted"}
        mock_delete.return_value = mock_response
        
        result = await delete_model("model1.pth")
        assert result["status"] == "deleted"


@pytest.mark.asyncio
async def test_voice_change_success(mock_rvc_url, tmp_path):
    """测试翻唱生成成功"""
    audio_file = tmp_path / "song.wav"
    audio_file.write_bytes(b"fake song data")
    
    with patch('httpx.AsyncClient.post') as mock_post:
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.content = b"fake converted audio"
        mock_post.return_value = mock_response
        
        result = await voice_change(str(audio_file), "model1.pth", {"pitch": 0})
        assert result["status"] == "success"
        assert "audio_path" in result


@pytest.mark.asyncio
async def test_voice_change_failure(mock_rvc_url, tmp_path):
    """测试翻唱生成失败"""
    audio_file = tmp_path / "song.wav"
    audio_file.write_bytes(b"fake song data")
    
    with patch('httpx.AsyncClient.post') as mock_post:
        mock_post.side_effect = Exception("Voice change failed")
        
        result = await voice_change(str(audio_file), "model1.pth", {"pitch": 0})
        assert result["status"] == "error"
        assert "error" in result
