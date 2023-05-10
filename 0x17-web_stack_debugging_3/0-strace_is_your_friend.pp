# Create index.html file
file {'/var/www/html/index.html':
    ensure  => file,
    mode    => '0644',
    content => '<html><head><title>Web Stack Debugging 3</title></head><body><h1>Hello, World!</h1></body></html>'
}

# Apache restart
exec {'Apache restart':
    command => 'sudo service apache2 restart',
    path    => ['/usr/bin', '/usr/sbin',]
}
