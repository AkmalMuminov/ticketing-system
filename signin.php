<?php
    $username = $_GET['userName'];
    $password = $_GET['passWord'];
    $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.userLogin('".$username."','".$password."')\"");
    $output = shell_exec($command); 
    echo($output);
    if(strcmp($output,"True") !== 0){
        header('Location: query.html');
        echo('here');
    }
?>