

!!uninstall openai for general env.

### R
```bash
#!/bin/bash
export R_X11_FONT_PATH="/usr/share/fonts/X11/75dpi"
export LD_LIBRARY_PATH="/opt/R/4.3.2/lib:/opt/R/4.3.2/lib/R/lib"
export R_HOME="/opt/R/4.3.2/lib/R"
exec /opt/R/4.3.2/bin/R "$@"
chmod +x ~/bin/R-4.3.2
R-4.3.2

/opt/R/4.3.2/lib/R/etc/Renviron.site, add
R_X11_FONT_PATH=/usr/share/fonts/X11/75dpi
LD_LIBRARY_PATH=/opt/R/4.3.2/lib:/opt/R/4.3.2/lib/R/lib
```


### Some must installed apckages
- curl # for getting insync
- FUSE #for run appiamges
- Clang complier for r (libssl-dev, libclang-dev)
- Flask-SocketIO for chatgpt and python3
- sudo install net-tools for remote connect(?)
-  sudo apt install libfuse2
- sudo apt-get install libxml2-dev
- sudo apt install netcat
- sudo ufw allow 22
- sudo apt install openssh-server corkscrew (for remote connection with ssh) 
- sudo apt-get install --reinstall gnome-control-center
- ClashVerge (- MUST! cash-verge)lv
- Rstudio + R
- julia 1.10.9
- python3
- openai
- Zoom (apt install)
- wine
	- wine Google Pinyin 2
	- wine through
	- wine wine WeChatSetup.exe

### sudo installed
```bash
sudo apt install fonts-wqy-zenhei fonts-wqy-microhei #(font)
sudo apt install redshift redshift-gtk; redshift -O 4000; redshift -x (to normal)
sudo apt install nodejs npm #install  render for backend 
npm install -g firebase-tools  #get firebase... another method
sudo apt install exfat-fuse exfat-utils #for connecting dji pocket
sudo apt install vlc
sudo apt-get install git-lfs #for github large push
sudo apt install feh
sudo apt install copyq
sudo apt install gh (for issue add in github)
sudo apt install gnome-shell-extension-appindicator gnome-tweaks chrome-gnome-shell #this and the follow is to show snipaste-dropdown sub menue.... but,   tweaks is a really good thing!
sudo apt install gnome-shell-extension-prefs gnome-shell-extension-appindicator
sudo apt install git-filter-repo

# for the zotero work with pdf arrange
sudo apt install pdfarranger

```

### Pip installed
```bash
pip install radian # this is for better R experience 
```
### snipaste:
use_appindicator = true #add this in:
nano /home/lea/.snipaste/config.ini
find config file in :nano /home/lea/.snipaste/config.ini


### back-end / middle-end / front-end
```bash

mkdir -p ~/.npm-global
chmod -R u+rw ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=$PATH:$HOME/.npm-global/bin' >> ~/.bashrc
source ~/.bashrc

sudo chmod +x /home/lea/.npm-global/bin/firebase

sudo npm uninstall -g firebase-tools
npm cache clean --force
npm install -g firebase-tools --max-old-space-size=4096 --verbose
npm install firebase-admin
npm install firebase-admin --save

pip install firebase-admin

```



### check ssd speed:
```bash
sudo dd if=/dev/nvme1n1 of=/dev/null bs=4M count=1000
```

###

	System R to 4.5.0; R in vscode and julia call of R being 4.3.2
	/opt/R/4.3.2
	free -h #REM use:
	
	lower version R:
	/opt/R/4.3.2/bin/R
	library in: ‘/home/lea/R/x86_64-pc-linux-gnu-library/4.3’
	
	add follow two lines in nano ~/.xprofile or nano ~/.xsessionrc as well
	bash:xset +fp /usr/share/fonts/X11/75dpi
	xset fp rehash
	check: xlsfonts | grep helvetica


```bash
# add follow two lines in 
nano ~/.xprofile
nano ~/.xsessionrc 
# add below:
	bash:xset +fp /usr/share/fonts/X11/75dpi
	xset fp rehash
	check: xlsfonts | grep helvetica

#add below:
nano ~/.Rprofile
Sys.setenv(R_X11_FONT_PATH = "/usr/share/fonts/X11/misc")
```

check in R: X11.options()

new solution: 
in bash (do this? to allow connection): xhost + 
```bash
nano ~/.bashrc

if [ "$DISPLAY" = "1" ]; then
    export DISPLAY=":1"
fi

export LD_LIBRARY_PATH=/opt/R/4.3.2/lib:/opt/R/4.3.2/lib/R/lib:$LD_LIBRARY_PATH	export R_HOME=/opt/R/4.3.2/lib/R
	
```

##### vscode setting
```json
    "terminal.integrated.env.linux": {
        "LD_LIBRARY_PATH": "/opt/R/4.3.2/lib:/opt/R/4.3.2/lib/R/lib",
        "DISPLAY": ":1",
        "XDG_RUNTIME_DIR": "/run/user/1000",
        "FONTCONFIG_PATH": "/etc/fonts",
        "R_X11_FONT_PATH": "/usr/share/fonts/X11/75dpi",
        "LIBGL_ALWAYS_INDIRECT": "1",
        "XAUTHORITY": "/home/Lea/.Xauthority"
    }
    
```
 check by echo $DISPLAY


higher version R:
the other R: /usr/bin/R
library in: ‘/home/lea/R/x86_64-pc-linux-gnu-library/4.5’

```bash
export LD_LIBRARY_PATH=/opt/R/4.3.2/lib:$LD_LIBRARY_PATH

LD_LIBRARY_PATH=/opt/R/4.3.2/lib:/opt/R/4.3.2/lib/R/lib julia
```

```julia
ENV["R_HOME"] = "/opt/R/4.3.2/lib/R"
using Pkg
Pkg.build("RCall")
```



```bash
sudo apt update
sudo apt install --no-install-recommends software-properties-common dirmngr
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
sudo add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"
```

##### Radiant:
```bash
sudo apt update
sudo apt install libcurl4-openssl-dev libxml2-dev libssl-dev libharfbuzz-dev libfribidi-dev libglpk-dev libudunits2-dev libgdal-dev libgeos-dev libproj-dev libfontconfig1-dev libfreetype6-dev libcairo2-dev
```
	
	

	
```bash
# FOLLOWING FROM R official website of install r
sudo apt update -qq
# install two helper packages we need
sudo apt install --no-install-recommends software-properties-common dirmngr
# add the signing key (by Michael Rutter) for these repos
# To verify key, run gpg --show-keys /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc 
# Fingerprint: E298A3A825C0D65DFD57CBB651716619E084DAB9
wget -qO- https://cloud.r-project.org/bin/linux/ubuntu/marutter_pubkey.asc | sudo tee -a /etc/apt/trusted.gpg.d/cran_ubuntu_key.asc
# add the repo from CRAN -- lsb_release adjusts to 'noble' or 'jammy' or ... as needed
sudo add-apt-repository "deb https://cloud.r-project.org/bin/linux/ubuntu $(lsb_release -cs)-cran40/"
# install R itself
sudo apt install --no-install-recommends r-base
```

##### for installilng tidyverse
```bash
#build-essential
#==============================================

sudo nano /etc/ssh/sshd_config
	PermitRootLogin yes
	PasswordAuthentication yes
	AllowTcpForwarding yes

nano ~/.ssh/config

	Host your-server
	  HostName your-server-ip
	  User your-username
	  Port 22
	  ProxyCommand corkscrew your-proxy-ip your-proxy-port %h %p
	  IdentityFile ~/.ssh/your-private-key


python3.10-venv #sudo apt install python3.10-venv
 #source lea/bin/activate

nano ~/.bashrc
export HTTP_PROXY="http://127.0.0.1:7897"
export HTTPS_PROXY="http://127.0.0.1:7897"

source ~/.bashrc 
echo $http_proxy
echo $https_proxy
env | grep -i proxy


```

### pinyin
- pinyin through cfitx (fcitx)
- fcitx5
- pinyin-fcitx
- ibux-pinyin
```bash
sudo apt install ibus ibus-libpinyin
ibus restart
ibus-setup
im-config -n ibus
sudo apt install ibus-gtk ibus-gtk3 ibus-qt4 ibus-qt5
export GTK_IM_MODULE=ibus
export QT_IM_MODULE=ibus
export XMODIFIERS=@im=ibus
nano ~/.bashrc
~/.profile
```


```bash


sudo sed -i.bak 's/Exec=\/usr\/bin\/google-chrome-stable/Exec=\/usr\/bin\/google-chrome-stable --gtk-version=4/' /usr/share/applications/google-chrome.desktop
sudo apt-get install ibus-gtk ibus-gtk3 ibus-qt4
sudo apt install ibus-typing-booster


```


### NEW FILES:
- Insync
- snipaste:  ./Downloads/Snipaste-2.10.6-x86_64.AppImage 
```bash
chmod +x ~/Downloads/snipaste.AppImage
```



### softlinks:
```bash
mkdir -p ~/.config/autostart
nano ~/.config/autostart/clashverge.desktop
nano ~/.config/autostart/snipaste.desktop
nano ~/.config/autostart/copyq.desktop

chmod +x ~/.config/autostart/*.desktop
```


### for julia
for VScode/julia
```bash
nano ~/.bashrc  
# add below
	export JULIA_NUM_THREADS=22;
	
	export JULIA_NUM_THREADS=4 
```
