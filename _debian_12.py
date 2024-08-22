Заменить репозитории в sources.list 
su
apt update
apt install sudo

sudo nano /etc/apt/sources.list
В открывшемся каталоге с правами root редактируем sources.list в любом текстовом редакторе, 
можо от туда удалить всё, вставив следующие репозитории:

#---------------------------------------------------------------
#            Официальные репозитории
deb http://ftp.ru.debian.org/debian/ bookworm main non-free-firmware
deb-src http://ftp.ru.debian.org/debian/ bookworm main non-free-firmware

deb http://security.debian.org/debian-security bookworm-security main non-free-firmware
deb-src http://security.debian.org/debian-security bookworm-security main non-free-firmware

deb http://security.debian.org/ bookworm-security main
deb-src http://security.debian.org/ bookworm-security main
#---------------------------------------------------------------

apt update

для 64х битных дистрибутивов подключаем дополнительно 32х битную архитектуру:
sudo dpkg --add-architecture i386

Настраиваем автоматический вход при запуске системы. Необходимо отредактировать конфиг lightdm.conf
sudo mousepad /etc/lightdm/lightdm.conf
#вместо mousepad можно написать любой установленный текстовой редактор.
в открывшемся конфиге, после параметра [Seat:*] находим строки
autologin-user=sav7eyes
autologin-user-timeout=0
Нужно их раскоментировать и прописать свое имя пользователя, при котором и запланирован автовход.

Добавляем пользователя в группу sudo (активация sudo) командами:
su -      #(знак - после su обязателен)
adduser sav7eyes sudo 

reboot

обновляем систему уже с использованием sudo и подключенной ранее 32х битной архитектуры:
sudo apt update
sudo apt upgrade

Одной командой ставим необходимые утилиты
sudo apt install gdebi thunar-gtkhash gedit nautilus gnome-disk-utility gnome-system-tools synaptic gnome-mpv qbittorrent vlc gnome-calculator

Русифицируем libreoffice:
sudo apt install libreoffice libreoffice-l10n-ru libreoffice-help-ru 

Если нужно, ставим Wine:
sudo apt install wine fonts-wine 
Желательно будет поставить к Wine следующие пакеты: playonlinux и winetricks
Однако их пока в репозиториях Debian 12 нет.

По необходимости (не на всех компах он есть) пакеты для Блютуз:
sudo apt install blueman blueman bluez pulseaudio-module-bluetooth

Драйвера для принтеров (тоже, если нужно):
sudo apt-get install printer-driver-all
sudo apt-get install cups hplip

устанавливаем заголовки и модули ядра
sudo apt install linux-headers-$(uname -r|sed 's,[^-]*-[^-]*-,,')

Устанавливаем дополнительные бинарники
sudo apt install firmware-linux-nonfree

И менеджер сети gnome (в Xfce уже установлен)
sudo apt install network-manager-gnome

Далее по необходимости:
# звук в терминале
sudo apt install sox libsox-fmt-all
# превью mp3 в файловом менеджере
sudo apt install mpg321 vorbis-tools
# для сохранения своих настроек thunar из под root
sudo apt install dbus-x11
# утилита информация о системе
sudo apt install neofetch

Уменьшаем зависание выключения (включения) проблеммных процессов с 1.5 минуты на 10 сек.
Редактируем конфиг с правами root /etc/systemd/system.conf
sudo mousepad /etc/systemd/system.conf
Находим, раскоментируем и исправляем строки:
DefaultTimeoutStartSec=10s
DefaultTimeoutStopSec=10s

Можно удалить архиватор и браузер (на их место ставлю другие), но это по желанию:
sudo apt remove --purge xarchiver firefox-esr
sudo apt autoremove

Перевод интерфейса среды debian на en
su
locale -a
cat /etc/locale.gen | grep en
nano /etc/locale.gen 
/sbin/locale-gen
localectl set-locale LANG=en_US.UTF-8