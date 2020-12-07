<?php
    $username = $_GET['username'];
    $password = $_GET['password'];
    $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.userLogin('".$username."','".$password."')\"");
    $output = shell_exec($command); 
    $output = trim($output);
    if($output == "True"){
        echo 'editTickets.html';
    }
    else
        echo 'Invalid Log in. Please Try Again.';
?>