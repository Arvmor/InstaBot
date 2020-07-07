<?php
$command = escapeshellcmd('./main.py');
$output = shell_exec($command);
header("location:javascript://history.go(-1)");
?>