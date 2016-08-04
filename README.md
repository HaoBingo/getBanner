# getBanner
First demo

## Usage：
Usage:   getBanner.py host
Example: getBanner.py 192.168.0.1

##  用途
在渗透过程中，常常需要扫描C段，利用C段来嗅探，为了方便，有时候需要过滤出Windows服务器。
快速扫描HOST主机并判断该主机是否为Windows操作系统。

## 说明
使用Python requests库
因有些网站不支持options、head等方式，故初版使用get请求获取服务器headers，通过headers返回的Server字段，来大致判断是否为wodows操作系统。

* 目前仅判断如下字段Server：*
1. IIS       Example:  Microft-IIS/6.0  Microft-IIS/IIS7.5
2. Win32     Example:  Apache/2.4.10(Win32) PHP/5.6.0
