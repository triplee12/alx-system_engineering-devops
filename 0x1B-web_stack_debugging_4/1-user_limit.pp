# Increase number of hard limits

exec { 'Increase hard limit':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 500000/" /etc/security/limits.conf',
  onlyif  => 'test -e /etc/security/limits.conf',
  path    => ['/usr/bin', '/bin',],
  returns => [0, 1]
}

# Increase number of soft limit

exec { 'Increase soft limit':
  command => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 400000/" /etc/security/limits.conf',
  onlyif  => 'test -e /etc/security/limits.conf',
  path    => ['/usr/bin', '/bin',],
  returns => [0, 1],
}
