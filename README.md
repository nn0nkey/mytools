# mytools
一些写的漏洞利用工具

## CVE-2024-23334

python start.py [启动脚本] -i [检测目标ip] -t [检测的目录]
用法可以查看 -h

python start.py -i 192.168.177.146 -t static

## CVE-2024-39027

和上面差不多

## CVE-2025-24813 tomcat-rce

同上

## CVE-2025-30208

vite前台任意文件读取漏洞

## 哥斯拉二开

参考https://github.com/kong030813/Z-Godzilla_ekp
https://github.com/xiaogang000/XG_NTAI/
https://tttang.com/archive/1840/#toc__4
https://yzddmr6.com/

### 流量规避

修改了cookie的强特征，以及ua，accept 弱特征，达成随机化

修改了请求包固定格式加入了随机请求，伪造为请求jpg和js资源规避

修改了响应包，伪造waf界面

### php免杀

参考小刚师傅的工具集成了目前还有免杀作用的php，一键生成免杀木马
![20250307121313](https://github.com/user-attachments/assets/206171fe-9cc2-4e7b-a3a1-c2076d852897)

![20250306181350](https://github.com/user-attachments/assets/69604813-faa4-47aa-bcb4-d435ae7fa0f2)


集成jsp免杀

采用编码的免杀方法
![20250307150512](https://github.com/user-attachments/assets/08c07849-2062-4c7b-a822-2413b2fdfba7)
![20250307150835](https://github.com/user-attachments/assets/976b5c96-b125-4f39-8634-6a41757dd639)

![20250307150844](https://github.com/user-attachments/assets/2c2e58bb-6127-45c2-9a52-6e641cb4488a)
