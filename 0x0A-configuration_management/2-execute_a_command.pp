# Task 3
  exec { 'pkill':
    command  => 'pkill killmenow',
    provider => 'shell',
}
