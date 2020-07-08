<?php
$command = escapeshellcmd('./main.py');
$output = shell_exec($command);
$myfile = fopen("./userInputs/status.txt", "w");
fwrite($myfile, $output);
header("location:javascript://history.go(-1)");
?>