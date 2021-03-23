
https://blog.csdn.net/DrewLee/article/details/114647876?spm=1001.2014.3001.5501
<https://blog.csdn.net/DrewLee/article/details/114799010#:~:text=%E6%89%80%E8%B0%93OSI%E4%B8%83%E5%B1%82%E6%A8%A1,%E6%A8%A1%E5%9E%8B%E6%88%96%E4%B8%83%E5%B1%82%E6%A8%A1%E5%9E%8B%E3%80%82>
 
[1 osi](#osi)<br/>
[2 TCP连接的建立与释放](#tcp)<br/>


###### osi
| Tables | Are |
| ------------- |:-------------:| 
| 物理层 | 负责比特流和电信号的转换，界定连接器钰网线的规格，使上层数据链路层不用管具体的传输介质 |
| 链路层 | 负责识别数据帧 ，将有差别的物理通道变为无差别的| 
| 网路层 | 负责地质管理路由选择，arp,ip, icmp, 为链路层和传输层转发，从一个设备到另外一个设备| 
| 传输层 | 连接两个设备的可靠传输 ，面向连接，屋面向无连接，tcp，udp| 
| 会话层 |,是用户应用程序和网络之间的接口例如：如果80端口要用，所以系统内数据通信，将接收端口数据送至需求端口 | 
| 表示层 | 设备固有数据和网络数据转换 比如语音和视频,解决各应用程序之间在数据格式表示上的差异。 | 
| 应用层 | 具体应用协议 ：FTP（文件传送协议）、Telnet（远程登录协议）、DNS（域名解析协议）、SMTP（邮件传送协议），POP3协议（邮局协议），HTTP协议（Hyper Text Transfer Protocol）| 



###### tcp
###### 三次
        第一次握手：SYN同步序列 + seq==x 结果：客户端syn-send
        第二次握手：SYN同步序列 + ack==x+1 ACK +seq=y 结果：服务端syn-send
        第三次握手：ACK  seq=y+1 ack= y+1 都就绪状态
        
###### 为什么不是两次握手：
        第一次握手保证客户端发送是ok的，服务端接受也是半ok的
        第二次握手保证服务端发送和接受是ok的
        第三次发送保证客户端接受是ok的
        
###### 为什么不是四次次握手：
        可以但是没必要，无非是服务端发一个ACK确认报文和syn同步报文
        
###### 四次
        第一次客户端发送FIN=1 seq=u  结果 客户端出去FIN-wait1 状态  
        第二次服务端发送 ACK ack = u+1 FIN=1 结果服务端处于close-wait tcpc处于半关闭状态 服务端处于FIN-wait2 此时服务端发送完ACK后可以继续发送未发完的数据
        第三次 服务端发送FIN=1 ack=u+1 ACK=1 seq=w   结果:服务端处于last-wati 客户端time-wait 2msl
        第四次 seq=u+1 ACK ack=w+1 结果 服务端 close  客户端 2mls后 close 
##### 2MSL设计的原因

        1.防止上一次连接中的包，迷路后重新出现，影响新连接（经过2MSL，上一次连接中所有的重复包都会消失）
        2.可靠的关闭TCP连接。在主动关闭方发送的最后一个 ack(fin) ，有可能丢失，这时被动方会重新发fin,
         如果这时主动方处于 CLOSED 状态 ，就会响应 rst 而不是 ack。所以主动方要处于 TIME_WAIT 状态，
         而不能是 CLOSED 。另外这么设计TIME_WAIT 会定时的回收资源，并不会占用很大资源的，除非短时间内接受大量请求或者受到攻击。
##### TCP 与 UDP 的区别

####  TCP 如何保证可靠传输
###   TCP 超时重传的原理
https://blog.csdn.net/cbjcry/article/details/84925028












































### <span id="jump1">1. 目录1</span>







 <span id = "anchor">锚点</span>
