# ip-rpi
Python script to display local IP address of Raspberry Pi

Read this in other languages: [简体中文](https://github.com/kopikaki/ip-rpi/blob/master/README.zh-cn.md).

## Installation

Download to project folder /home/pi/projects/ip-rpi.

```bash
$ cd /home/pi/projects/
$ git clone https://github.com/kopikaki/ip-rpi.git
```

## Usage

Add the cron script to start at boot and run for every 1 min.

```bash
$ crontab -e
```

```
@reboot sudo python /home/pi/projects/ip-rpi/ip.py > /home/pi/docker/node-red-exp/data/ip.txt &
* * * * * sudo python /home/pi/projects/ip-rpi/ip.py > /home/pi/docker/node-red-exp/data/ip.txt
@reboot sudo iwgetid -r > /home/pi/docker/node-red-exp/data/ssid.txt &
* * * * * sudo iwgetid -r > /home/pi/docker/node-red-exp/data/ssid.txt
```

Check the cron script.

```bash
$ crontab -l
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
