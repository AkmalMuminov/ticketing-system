<?php
    $id = $_GET['id'];
    $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.queryByID('".$id."')\"");
    $output = shell_exec($command);
    $output = trim($output);
    $output = trim($output,"[");
    $output = trim($output,"'");
    $output = rtrim($output,"]");
    $output = rtrim($output,"'");
    $output = explode(",",$output);
    
    echo "<table border = '1'>";
    echo "<tr>";
    $counter = 0;
    for($i=0; $i< sizeof($output); $i++){
            if($counter == 8 ){
               $counter = 0;
               echo "<tr>"; 
            }
            $counter++;
            echo "<td>".$output[$i]."</td>";
    }
?>