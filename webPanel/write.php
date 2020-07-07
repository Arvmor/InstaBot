<?php
$myfile = fopen("./../commentText.txt", "w");
$txt = $_POST['comment'];
fwrite($myfile, $txt);
header("location:javascript://history.go(-1)");
?>