#!/usr/bin/env python3
# @author wuzhixuan
# @date 2025-01-27
import socket
import json
import time
from datetime import datetime

def send_log(message, level="INFO", service="test-service"):
    log_data = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "level": level,
        "message": message,
        "service": service
    }
    
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('192.168.61.65', 50000))
        sock.sendall((json.dumps(log_data) + '\n').encode('utf-8'))
        sock.close()
        print(f"✓ 发送成功: {message}")
    except Exception as e:
        print(f"✗ 发送失败: {e}")

# 发送测试日志
for i in range(10):
    send_log(f"测试日志 #{i+1}", "INFO", "python-test")
    time.sleep(0.5)