# getBanner
扫描网段，查找开放web(80)服务并且是windows的主机。

2016/8/4  二版，支持网段扫描，获取80端口Banner，使用head请求，扫描C段大概耗时4min</br>
2016/8/4  初版 仅能判断单个主机

## Usage：
Usage:   getBanner.py host </br>
Example: getBanner.py 192.168.0.1 or 192.168.0.1/24

##  用途
在渗透过程中，常常需要扫描C段，利用C段来嗅探，为了方便，有时候需要过滤出Windows服务器。</br>
快速扫描HOST主机并判断该主机是否为Windows操作系统。

## 说明
需要库：
1. requests 
2. netaddr

使用head请求获取服务器headers，通过headers返回的Server字段，来大致判断是否为wodows操作系统。

目前仅判断如下字段Server：

1. IIS       Example:  Microft-IIS/6.0  Microft-IIS/IIS7.5
2. Win32     Example:  Apache/2.4.10(Win32) PHP/5.6.0
