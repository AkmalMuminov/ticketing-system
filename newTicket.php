<?php
    $name = $_GET['name'];
    $descrip = $_GET['descrip'];
    $category = $_GET['category'];
    if(empty($name) or empty($descrip) or empty($category))
        die('Ticket could not be created. Please complete all fields before submitting.');
    else{
        $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.addTicket('".$name."','".$descrip."','".'Open'."','".'N/A'."','".$category."')\"");
        
        $output = shell_exec($command);
        echo 'Ticket has been created successfully';
    }

?>