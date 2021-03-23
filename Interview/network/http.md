[1 HTTP status](#HTTP status)<br/>
[2 nginx prox](#nginx prox)<br/>
[2 浏览器输入URL到网页完全呈现的过程](#http url)<br/>

###### HTTP status
    HTTP 500 – 内部服务器错误”，需要修改程序。
    HTTP 502 – 网关错误”，需要重启Web应用服务器。

###### nginx prox

    正向代理：一个局域网和客户端一个lan  好处 做验证 缓存
    反向代理：保证安全 负载均衡
    
 
###### #http url

###### 总体分为以下几个过程：

    
    DNS解析——解析域名，获取对应的ip地址
    TCP连接——TCP三次握手
    浏览器发送http请求
    服务器处理请求并返回http报文
    浏览器解析返回的数据并渲染页面
    断开连接：TCP四次挥手
