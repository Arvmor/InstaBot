<?php
$myfile = fopen("./../userInputs/accountNumber.txt", "w");
$txt = $_POST['accountNumber'];
fwrite($myfile, $txt);
header("location:javascript://history.go(-1)");
?>