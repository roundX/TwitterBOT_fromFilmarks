<?php
$data = array();
exec("/virtual/roundx/public_html/FilmarksBOT.sh 2>&1", $data);
echo("<html><body><pre>");
var_dump($data);
echo("</pre></body></html>");
