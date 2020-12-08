<?php
    $queryType = $_GET['typeToQuery'];
    $queryInfo = $_GET['queryInfo'];

    if($queryType == 1){
        $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.queryByID('".$queryInfo."')\"");
    }
    else if($queryType == 2){
        $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.queryByKeyword('".$queryInfo."')\"");
    }
    else if($queryType == 3){
        $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.queryByLastUser('".$queryInfo."')\"");
    }
    else if($queryType == 4){
        $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.queryByStatus('".$queryInfo."')\"");
    }
    else{
        $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.queryByDate('".$queryInfo."')\"");
    }
    #$command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.queryByID('".$queryInfo."')\"");
    #$command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.queryByKeyword('".$queryInfo."')\"");
    #$command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.queryByID('".$queryInfo."')\"");
    #$command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.queryByDate('".$queryInfo."')\"");
    #$command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.queryByStatus('".$queryInfo."')\"");
    

    $output = shell_exec($command);
    #$output .= shell_exec($command2);
    #$output .= shell_exec($command3);
    #$output .= shell_exec($command4);
    #$output .= shell_exec($command5);

    $output = explode(",",$output);
    $output = str_replace("'","",$output);
    $output = str_replace("[","",$output);
    $output = str_replace("]","",$output);
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