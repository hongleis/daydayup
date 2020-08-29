# Redis
## 主从库数据如何实现一致
- 高性能的必然要求，服务尽量不要中断，因此要有主从库
- 第一次同步，从库调用`replicaof 主库IP 6379`
1. 从库给主库发送psync命令包含参数`runID=?, offset=-1`
2. 主库准备好，发送FULLRESYNC，包含参数自己的runID和offset
- 主库传送RDB文件，从库读RDB到内存
1. 主库执行bgsave命令，生产最新的RDB文件，把RDB文件传送从库
2. 从库把本地数据清空，把RDB文件读进内存
3. 在同步过程中，主库没有被阻塞，主库会把同步过程中产生的新的写命令存入`replication buffer`
- 主库把`replication buffer`中的命令传给从库
- 主从级联模式