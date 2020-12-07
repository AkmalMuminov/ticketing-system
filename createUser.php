<?php
    $username = $_GET['name'];
    $password = $_GET['password'];

    if(empty($username) or empty($password))
        die('User cannot be created. Please enter both fields.');
    else{
        $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.addUser('".$username."','".$password."')\"");
        echo $command;
        $output = shell_exec($command);
        die('New User Created successfully.');
    }

?>