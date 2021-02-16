# check if micropython firmware exists in currect dir. if not, download it.
if(!(Test-Path -path esp8266-20210202-v1.14.bin))
{
    Invoke-WebRequest -Uri "https://micropython.org/resources/firmware/esp8266-20210202-v1.14.bin" -OutFile "esp8266-20210202-v1.14.bin"
}

py -m esptool --port COM5 erase_flash
py -m esptool --port COM5 --baud 460800 write_flash --flash_size=4MB 0 "esp8266-20210202-v1.14.bin"
Start-Sleep -s 5
ampy --port COM5 --baud 115200 put micropython/boot.py
ampy --port COM5 --baud 115200 put micropython/main.py
ampy --port COM5 --baud 115200 put micropython/lib
ampy --port COM5 --baud 115200 put micropython/read_temperature.py