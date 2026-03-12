#!/bin/bash
# 测试 Docker data-root 配置脚本
# 用于验证 /mnt/docker 配置是否正确

set -e

echo "=========================================="
echo "Testing Docker data-root configuration"
echo "=========================================="
echo

# 1. 检查当前磁盘空间
echo "1. Current disk space:"
df -h | grep -E "Filesystem|/|/mnt"
echo

# 2. 停止 Docker
echo "2. Stopping Docker..."
sudo systemctl stop docker
echo "   ✓ Docker stopped"
echo

# 3. 创建 /mnt/docker 目录
echo "3. Creating /mnt/docker directory..."
sudo mkdir -p /mnt/docker
ls -ld /mnt/docker
echo "   ✓ Directory created"
echo

# 4. 配置 daemon.json
echo "4. Configuring daemon.json..."
if [ -f /etc/docker/daemon.json ]; then
    echo "   Current daemon.json:"
    sudo cat /etc/docker/daemon.json
    echo
    sudo jq '. + {"data-root": "/mnt/docker"}' /etc/docker/daemon.json > /tmp/daemon.json
else
    echo "   No existing daemon.json, creating new one"
    echo '{"data-root": "/mnt/docker"}' > /tmp/daemon.json
fi

sudo mv /tmp/daemon.json /etc/docker/daemon.json
echo "   New daemon.json:"
sudo cat /etc/docker/daemon.json
echo "   ✓ daemon.json configured"
echo

# 5. 启动 Docker
echo "5. Starting Docker..."
sudo systemctl start docker
sleep 3
echo "   ✓ Docker started"
echo

# 6. 验证配置
echo "6. Verifying configuration..."
echo "   Docker info:"
sudo docker info | grep -E "Docker Root Dir|Storage Driver"
echo

# 7. 测试构建
echo "7. Testing with a simple build..."
cat > /tmp/Dockerfile.test <<EOF
FROM alpine:3.19
RUN echo "Test successful"
EOF

docker build -t test:latest -f /tmp/Dockerfile.test /tmp
docker rmi test:latest
rm /tmp/Dockerfile.test
echo "   ✓ Test build successful"
echo

# 8. 最终磁盘空间检查
echo "8. Final disk space:"
df -h | grep -E "Filesystem|/|/mnt"
echo

echo "=========================================="
echo "✅ All tests passed!"
echo "Docker is now using /mnt/docker for storage"
echo "=========================================="
