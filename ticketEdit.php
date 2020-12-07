<?php
    $id = $_GET['ID'];
    $name = $_GET['name'];
    $descrip = $_GET['descrip'];
    $category = $_GET['category'];
    $status = $_GET['status'];
    $lastUser = $_GET['lastUser'];

    $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.queryByID('".$id."')\"");
    $output = shell_exec($command);
    $output = trim($output);
    if($output == "False")
        die('Ticket with that ID does not exists. Please try again.');
    
    if(empty($lastUser))
        die('The current user to edit this ticket must be given.');    



    if($status == 'true'){
        $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.updateStatusOfTicket('".$id."')\"");
        $output = shell_exec($command);
    }
    if(!empty($lastUser)){
        $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.updateLastUser('".$id."','".$lastUser."')\"");
        $output = shell_exec($command);
    }    
    if(!empty($category)){
        $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.updateCategory('".$id."','".$category."')\"");
        $output = shell_exec($command);
    }
    if(!empty($descrip)){
        $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.updateDescription('".$id."','".$descrip."')\"");
        $output = shell_exec($command);
    }
    if(!empty($name)){
        $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.updateName('".$id."','".$name."')\"");
        $output = shell_exec($command);
    }


    die('Ticket has been updated. Please refer to Query page to view updated ticket.');
    
?>