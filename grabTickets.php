<?php
    $command = escapeshellcmd("py -c \"import connectionToSql; connectionToSql.queryDefault()\"");
    $output = shell_exec($command);
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
    
    #$table = $output;
		
	#	echo"<table border = '1'>";
	#	foreach($table as $row){ 
	#	echo "<tr>";
	#	foreach($row as $value){
	#		echo "<td>$value</td>";
	#	}
	#	echo "</tr>";
	#	}
?>