<!DOCTYPE html>
<html lang="en">

<head>
    <title>.: Panel :.</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="main.css">
</head>

<body>
<div class="container-contact100">
    <div class="wrap-contact100">
        <a href="#" onclick="window.location.reload();">Clear</a>
        <form action="./../runTheBot.php" method="post">
            <input type="submit" id="a" value="Run" name="btn">
        </form>
        <form action="./write.php" method="post">
                <span class="contact100-form-title">Send Comment</span>
                <pre><textarea class="input100" name="comment" placeholder="Text"></textarea></pre>
                <input type="submit" id="a" name="submit" value="Submit">
                <script src="./btnClick.js"></script>
            </div>
        </div>
    </form>
</body>

</html>