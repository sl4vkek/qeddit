# Web server config
Currently I only have documentation for running qeddit on Lighttpd, but it definitely could run on other web servers. More could be added in the future.
## Lighttpd
### Install web server
#### Arch/Manjaro
`sudo pacman -S lighttpd perl perl-cgi`
#### Ubuntu
`sudo apt-get install lighttpd perl perl-cgi`
### Configure Perl CGI
Replace `/etc/lighttpd/lighttpd.conf` with this one: 
<br/>`
curl https://raw.githubusercontent.com/sl4vkek/qeddit/master/web-config/lighttpd.conf -o /etc/lighttpd/lighttpd.conf`
<br/>
Configure it to your liking.
### Install qeddit
`cd /srv/http`<br/>
`git clone https://github.com/sl4vkek/qeddit.git`<br/>
`mv ./qeddit/src/* ./`<br/>
rm -rf ./qeddit
### Systemd stuff
`systemctl enable lighttpd`<br/>
`systemctl restart lighttpd`
### Thats it
You've done it, you've become a reddit proxy.