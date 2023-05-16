# Increase limit

exec { 'Increase limit':
  command => 'sed -i "s/15/1000000/" /etc/default/nginx',
  path    => ['/usr/bin', '/bin',],
  returns => [0,1]
}

# Start nginx
service { 'Nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  restart    => '/usr/sbin/service nginx restart',
  subscribe  => Exec[ 'Increase limit']
}