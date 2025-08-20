

!!uninstall openai for general env.

[[2025-08-17]] [[voice to type - dumb v]] [[voice to type - smart v]]


#### for pdf147 read
```bash
# Ubuntu/Debian: 
sudo apt-get install libzbar0 

```

#### restart, refresh shell
- GNOME on Xorg: press Alt+F2, type r, Enter. This restarts the shell and refreshes icons.

## Fonts
```bash
sudo mkdir -p /usr/share/fonts/truetype/custom
sudo cp YourFont.ttf /usr/share/fonts/truetype/custom/
sudo fc-cache -fv
```

Font forge
```bash
sudo apt install fontforge
fontforge -lang=ff -c '
  Open("midi.ttf");
  # PSName, FamilyName, StyleName, FullName：PSName 必须 ASCII，Family/FullName 可以中英混合
  SetFontNames("MiDiShuFa", "misishufa-ziti", "Regular", "midishufaziti-Regular");
  Generate("mf-fixed.ttf");
  Close();
  Quit();
'


sudo cp ltjx-fixed.ttf /usr/share/fonts/truetype/custom/ltjx.ttf
sudo fc-cache -r -v


fc-list | grep -i YourFont
```
### libreoffice

Ubuntu 22.04 的 backports 仓库里也包含了更新版的 LibreOffice： (donesn't work)

```bash
sudo apt update sudo apt install -t jammy-backports libreoffice
```

- 这会直接从官方 backports 拉取更新，不需要额外添加 PPA


One that works: uninstall apt version install snap version
```bash
sudo apt remove --purge libreoffice*
sudo snap install libreoffice --classic
```
Above too slow:
### . Download and install the official LibreOffice tarball

1. Grab the latest Linux .tar.gz from https://www.libreoffice.org/download/
    
2. Extract and install the .deb files:

```bash
tar xf LibreOffice_*.tar.gz cd LibreOffice_*/DEBS sudo dpkg -i *.deb
```
Because you’re pulling straight from LibreOffice’s own mirror, you may get better throughput.

#### chmod
```bash
chmod +x ~/start_cursor_with_proxy.sh
```

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

sudo apt install fontforge
```

```bash
# cursor ide
curl https://cursor.com/install -fsS | bash

#1. Add ~/.local/bin to your PATH:
#   For bash:
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

#2. Start using Cursor Agent:
   cursor-agent
 
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


#### changed things
I've successfully fixed your icon setup! Here's what we accomplished:

Make icon to zotero and obesidian
```text
I've successfully fixed your icon setup! Here's what we accomplished:

### ✅ Zotero Icon - FIXED

- Icon installed: zotero-zotero.png (128x128) in your local icon directory

- Autostart file updated: Added Icon=zotero-zotero to ~/.config/autostart/zotero.desktop

- Status: Working properly

### ✅ Obsidian Icon - FIXED

- Icon set: Using Icon=text-editor (a generic text editor icon that should work with most icon themes)

- Autostart file updated: Added Icon=text-editor to ~/.config/autostart/obsidian.desktop

- Status: Working with generic icon

### 🔧 What Was Fixed

1. Path issues: Your original command had incorrect file paths

2. Icon installation: Properly installed Zotero icon using xdg-icon-resource

3. Desktop file updates: Added proper Icon= entries to both autostart files

4. Icon cache: Updated icon caches to ensure changes take effect

### 🎯 Current Status

Both applications should now display proper icons in your system tray, autostart manager, and other places where icons are shown.

### �� Optional: Better Obsidian Icon

If you want a more specific Obsidian icon, you have a few options:

1. Download an Obsidian icon: You can download an Obsidian icon from the internet and install it manually

2. Use a different generic icon: Change Icon=text-editor to something like Icon=document-edit or Icon=text-x-generic

3. Create a custom icon: Extract an icon from the Obsidian AppImage using a different method

The current setup should work well for most purposes. The icons will now appear properly in your system, and both applications should start with the correct icons when they autostart.

Would you like me to help you with any of the optional improvements, or are you satisfied with the current working setup?
```
