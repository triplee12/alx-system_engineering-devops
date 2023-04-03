# Install a new brand ubuntu server with custom http header
exec {'update_system':
    command => '/usr/bin/env apt-get update'
}
Exec['update_system'] -> package {'nginx':
    ensure   => installed,
    provider => apt,
}
file {[
        '/var/www/ebukaejie',
        '/var/www/ebukaejie/html'
    ]:
    ensure => 'directory'
}
file {'/var/www/ebukaejie/html/index.html':
    ensure  => 'present',
    content => 'Hello World!'
}
file {'/var/www/ebukaejie/html/custom_404.html':
    ensure  => 'present',
    content => "Ceci n'est pas une page"
}
$cnt = "server {
	listen 80;
	listen [::]:80 default_server;
	root /var/www/ebukaejie/html;
	index index.html;
	
	server_name ebukaejie.tech www.ebukaejie.tech;
	rewrite '^/redirect_me$' http://example.com permanent;
	error_page 404 /custom_404.html;
	location / {
		add_header X-Served-By $hostname;
	}
}"
exec {'clean_up_available_site':
    command => '/usr/bin/env rm -rf /etc/nginx/sites-available/*'
}
exec {'clean_up_enabled_site':
    command => '/usr/bin/env rm -rf /etc/nginx/sites-enabled/*'
}
Exec ['clean_up_available_site'] -> file {'/etc/nginx/sites-available/ebukaejie.config':
    content => $cnt,
}
Exec ['clean_up_enabled_site'] -> file {'/etc/nginx/sites-enabled/ebukaejie.config':
    ensure => 'link',
    target => '/etc/nginx/sites-available/ebukaejie.config'
}
service {'nginx':
    ensure  => 'running',
    restart => true
}
