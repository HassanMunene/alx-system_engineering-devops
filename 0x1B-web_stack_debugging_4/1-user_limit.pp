# Fix the problem of large amount files opened at a time.

exec {'replace-1':

  provider => shell,

  command  => 'sudo sed -i "s/nofile 5/nofile 50000/" /etc/security/limits.conf',

  before   => Exec['replace-2'],

}

exec {'replace-2':

  provider => shell,

  command  => 'sudo sed -i "s/nofile 4/nofile 40000/" /etc/security/limits.conf',

}
