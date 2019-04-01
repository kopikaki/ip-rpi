# ip-rpi
Python 程序显示树莓派网路地址 。

Read this in other languages: [English](https://github.com/kopikaki/ip-rpi/README.md).

## 安装

下载去目录 /home/pi/projects/ip-rpi.

```bash
$ cd /home/pi/projects/
$ git clone https://github.com/kopikaki/ip-rpi.git
```

## 使用

加入定时程序，系统启动时执行，然后每分钟执行.

```bash
$ crontab -e
```

```
@reboot sudo python /home/pi/projects/ip-rpi/ip.py > /home/pi/docker/node-red-exp/data/ip.txt &
* * * * * sudo python /home/pi/projects/ip-rpi/ip.py > /home/pi/docker/node-red-exp/data/ip.txt
@reboot sudo iwgetid -r > /home/pi/docker/node-red-exp/data/ssid.txt &
* * * * * sudo iwgetid -r > /home/pi/docker/node-red-exp/data/ssid.txt
```

检查代码：

```bash
$ crontab -l
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
