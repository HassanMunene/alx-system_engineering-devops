# This manifest is used to configure nginx web server during installation
package { 'nginx':
    ensure => 'installed',
}

exec {'install':
    command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
    provider => shell,
}
service { 'nginx':
    ensure  => 'running',
    enable  => true,
    require => Package['nginx'],
}

file {'/etc/nginx/sites-available/default':
    ensure  => 'file',
    content => '
       server {
           listen 80;
           listen [::]:80 default_server;
           root /etc/nginx/html;
           index.html index.htm;
       
            location /redirect_me {
                return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
            }
        }
    ',
    require => Package['nginx'],
    notify  => Service['nginx']
}
file {'/etc/nginx/html/index.html':
    ensure  => 'file',
    content => 'Hello World',
}

exec {'run':
    command  => 'sudo service nginx restart',
    provider => shell,
}
