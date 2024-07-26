# Create process called killmenow
  
    exec { 'pkill killmenow':
    path    => '/bin/',
    
    }
