<?php
$myfile = fopen("./../userInputs/commentText.txt", "w");
$txt = $_POST['comment'];
fwrite($myfile, $txt);
header("location:javascript://history.go(-1)");
?>