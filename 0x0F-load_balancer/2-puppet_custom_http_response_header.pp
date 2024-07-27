# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure the Nginx service is running and enabled
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'], # Restart if the configuration changes
}

# Create the directory for Nginx HTML files
file { '/etc/nginx/html':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}

# Create the index.html file
file { '/etc/nginx/html/index.html':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "Hello World!\n",
}

# Create the 404.html file
file { '/etc/nginx/html/404.html':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => "Ceci n'est pas une page\n",
}

# Configure Nginx to include the custom HTTP header
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => @("EOF")
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    add_header X-Served-By $hostname;

    root /etc/nginx/html;
    index index.html index.htm;
    
    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
    
    error_page 404 /404.html;
    location = /404.html {
        internal;
    }
}
EOF
  ",
  notify  => Service['nginx'], # Notify Nginx to restart if the configuration changes
}

# Ensure the configuration is linked from sites-enabled
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  notify => Service['nginx'], # Notify Nginx to restart if the link is created or updated
}
