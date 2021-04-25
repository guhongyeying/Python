##### redis 五种数据结构详解
    （string，list，set，zset，hash HyperLogLog、Geo、Pub/Sub）
##### 如果你说还玩过Redis Module，像BloomFilter，RedisSearch，Redis-ML，面试官得眼睛就开始发亮了

#####https://baijiahao.baidu.com/s?id=1594341157941741587&wfr=spider&for=pc


###滑动窗口设置用户访问次数
    # coding: utf8
    import time
    import redis
    client = redis.StrictRedis()
    def is_action_allowed(user_id, action_key, period, max_count):
         key = 'hist:%s:%s' % (user_id, action_key)
         now_ts = int(time.time() * 1000) # 毫秒时间戳
         with client.pipeline() as pipe: # client 是 StrictRedis 实例
             # 记录行为
             pipe.zadd(key, now_ts, now_ts) # value 和 score 都使用毫秒时间戳
             # 移除时间窗口之前的行为记录，剩下的都是时间窗口内的
             pipe.zremrangebyscore(key, 0, now_ts - period * 1000)
             # 获取窗口内的行为数量
             pipe.zcard(key)
             # 设置 zset 过期时间，避免冷用户持续占用内存
             # 过期时间应该等于时间窗口的长度，再多宽限 1s
             pipe.expire(key, period + 1)
             # 批量执行
             _, _, current_count, _ = pipe.execute()
         print(client.zrange(key,0,now_ts))
         return current_count <= max_count
    for i in range(20):
        time.sleep(6)
        print (is_action_allowed("laoqian", "reply5", 6, 5))
        
 ##### redis击穿，穿透，雪崩以及解决方案
 
1. 击穿：单个key并发造车db压力
        
        1) 通过synchronized+双重检查机制：某个key只让一个线程查询，阻塞其它线程 缺点: 会阻塞其它线程
        2) 设置value永不过期

2. 穿透：为恶意频繁查询才会对系统造成很大的问题: key缓存并且数据库不存在
        1） 布隆过滤器（bloom filter）
3. 雪崩：突然大量失效
        做二级缓存
        不同过期时间
        
        
 #### 锁 互斥锁，mutex key setex
 
 #### 单机 主从，集群