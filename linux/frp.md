# frp内网穿透

## 前期准备
### 1. vps服务器
### 2. 域名（可有可无）
### 3. frp github文件

## 开始部署

### 1. 服务器端部署

#### 1.1 开放服务器端口
#### 1.2 部署服务器端frps
#### 1.3 编写配置文件frps.ini

#### 1.4 启动服务器端服务 ./frps -c frps.ini


### 2. 客户端配置

#### 2.1 部署客户端fprc
#### 2.2 编写配置文件frpc.ini
#### 2.3 启动客户端服务 ./frpc -c frpc.ini


frps.ini{
[common]
bind_port = 7000
}


frpc.ini{
[common]
server_addr =  xxx #your_custom_domain or the real public ip
server_port = 7000

[ssh]
type = tcp
local_ip = 127.0.0.1
local_port = 22
remote_port = xxx #custom_port  
}



## 常见问题

> [E] [proxy.go:793] [01a44f5ed94ac458] [dell_docker_ssh] connect to local service [127.0.0.1:22] error: dial tcp 127.0.0.1:22: connect: connection refused

没有打开ssh 服务



