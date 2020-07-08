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
            <span class="contact100-form-title">Status</span>
                <pre><textarea class="input100" name="" disabled>Current Status: <?php include('./../userInputs/status.txt'); ?>                
Account: <?php include('./../userInputs/accountNumber.txt'); ?>                
comment Text: <?php include('./../userInputs/commentText.txt'); ?>                
Post URL: <?php include('./../userInputs/postURLText.txt'); ?></textarea></pre>
        </form>
        <form action="./writeAccountNumber.php" method="post">
                <span class="contact100-form-title">Account Number</span>
                <pre><textarea class="input100" name="accountNumber" placeholder="Ex. 1"></textarea></pre>
                <input type="submit" id="a" name="submit" value="Submit">
        </form>
        <form action="./writePostURL.php" method="post">
                <span class="contact100-form-title">Target Post</span>
                <pre><textarea class="input100" name="posturl" placeholder="Ex. https://www.instagram.com/p/ABCDEFGHIJHK/"></textarea></pre>
                <input type="submit" id="a" name="submit" value="Submit">
        </form>
        <form action="./writeComment.php" method="post">
                <span class="contact100-form-title">Send Comment</span>
                <pre><textarea class="input100" name="comment" placeholder="Ex. Great Post 👍"></textarea></pre>
                <input type="submit" id="a" name="submit" value="Submit">
                <script src="./btnClick.js"></script>
            </div>
        </div>
    </form>
</body>

</html>