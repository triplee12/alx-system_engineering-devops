# Web stack debugging 3
exec { 'debug wordpress':
    environment => ['Dir=/var/www/html/wp-settings.php',
        'OLD_PHPP=phpp', 'NEW_PHP=php'],
    command     => 'sudo sed -i "s/$OLD_PHPP/$NEW_PHP/" $DIR',
    path        => ['/usr/bin', '/bin'],
    returns     => [0, 1]
}
