<html>
<head>
<title>Challenge 9</title>
<body>
It's a gift exchange! If you can send Santa a special gift in your header, he will give you one, too. He likes cookies: gingerbread. </br></br>Here are the headers you sent:</br></br>
<?php
$headers = apache_request_headers();

foreach ($headers as $header => $value) {
   echo "$header: $value <br />\n";
   if ($value == "clause") {
    echo "<br><br><h1>You've done it!</h1></br>Visit xDaGFsbGVuZ2U to get info on the final challenge!";
} else {
    echo "";
}
}
?>
</body>
</html>
