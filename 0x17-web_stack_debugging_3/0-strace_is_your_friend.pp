file {'var/www/html/index.html';
  ensure  => file,
  mode    => '0666',
  content => '<html><head><title>Web Debugging #3</title></head><body><h1>Hello, World!</h1></body></html>'
}
