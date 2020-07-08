<?php
$myfile = fopen("./../userInputs/postURLText.txt", "w");
$txt = $_POST['posturl'];
fwrite($myfile, $txt);
header("location:javascript://history.go(-1)");
?>