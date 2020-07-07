<?php
$myfile = fopen("commentText.txt", "w");
$txt = $_POST['comment'];
fwrite($myfile, $txt);
?>