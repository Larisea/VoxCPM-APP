"""RVC API路由测试"""
import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from fastapi.testclient import TestClient
from server.routes import create_app


@pytest.fixture
def client():
    """创建测试客户端"""
    app = create_app()
    return TestClient(app)


def test_rvc_status_endpoint(client):
    """测试RVC状态检测端点"""
    with patch('server.rvc_client.check_rvc_status') as mock_check:
        mock_check.return_value = {"status": "online", "url": "http://localhost:7865"}
        
        response = client.get("/api/rvc/status")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "online"
        assert "url" in data


def test_rvc_status_endpoint_offline(client):
    """测试RVC状态检测端点（离线）"""
    with patch('server.rvc_client.check_rvc_status') as mock_check:
        mock_check.return_value = {"status": "offline", "error": "Connection refused"}
        
        response = client.get("/api/rvc/status")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "offline"
        assert "error" in data


def test_rvc_upload_audio_endpoint(client, tmp_path):
    """测试上传音频端点"""
    audio_file = tmp_path / "test.wav"
    audio_file.write_bytes(b"fake audio data")
    
    with patch('server.rvc_client.upload_audio_to_rvc') as mock_upload:
        mock_upload.return_value = {"status": "success", "path": "/data/test.wav"}
        
        with open(audio_file, "rb") as f:
            response = client.post(
                "/api/rvc/upload_audio",
                files={"audio": ("test.wav", f, "audio/wav")}
            )
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "path" in data


def test_rvc_train_endpoint(client):
    """测试训练端点"""
    with patch('server.rvc_client.start_training') as mock_train:
        mock_train.return_value = {"status": "training_started", "task_id": "123"}
        
        response = client.post(
            "/api/rvc/train",
            json={
                "audio_path": "/data/test.wav",
                "model_name": "test_model"
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "training_started"
        assert "task_id" in data


def test_rvc_training_status_endpoint(client):
    """测试训练状态端点"""
    with patch('server.rvc_client.get_training_status') as mock_status:
        mock_status.return_value = {
            "status": "training",
            "progress": 50,
            "epoch": 100,
            "total_epochs": 200
        }
        
        response = client.get("/api/rvc/training_status")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "training"
        assert data["progress"] == 50


def test_rvc_models_endpoint(client):
    """测试模型列表端点"""
    with patch('server.rvc_client.list_models') as mock_list:
        mock_list.return_value = {
            "models": [
                {"name": "model1.pth", "size": 1024},
                {"name": "model2.pth", "size": 2048}
            ]
        }
        
        response = client.get("/api/rvc/models")
        assert response.status_code == 200
        data = response.json()
        assert len(data["models"]) == 2
        assert data["models"][0]["name"] == "model1.pth"


def test_rvc_delete_model_endpoint(client):
    """测试删除模型端点"""
    with patch('server.rvc_client.delete_model') as mock_delete:
        mock_delete.return_value = {"status": "deleted"}
        
        response = client.delete("/api/rvc/models/model1.pth")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "deleted"


def test_rvc_voice_change_endpoint(client, tmp_path):
    """测试翻唱生成端点"""
    audio_file = tmp_path / "song.wav"
    audio_file.write_bytes(b"fake song data")
    
    with patch('server.rvc_client.voice_change') as mock_change:
        mock_change.return_value = {"status": "success", "audio_path": "output/cover_song_model1.wav"}
        
        with open(audio_file, "rb") as f:
            response = client.post(
                "/api/rvc/voice_change",
                files={"audio": ("song.wav", f, "audio/wav")},
                data={"model_name": "model1.pth", "pitch": 0}
            )
        
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "success"
        assert "audio_path" in data
