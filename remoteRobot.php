<?php
session_start();
include "remoteRobot.html";
$action = $_GET['GO'];
switch ($action)
{
	case "ON":
		system('sudo python /var/www/init.sh');
		break;
	case "FORWARD":
                system('sudo python /var/www/forward.py');
		break;
	case "BACKWARD":
		system('sudo python /var/www/backward.py');
		break;
	case "LEFT":
		system('sudo python /var/www/left.py');
		break;
	case "RIGHT":
		system('sudo python /var/www/right.py');
		break;
        case "STOP":
		system('sudo python /var/www/stop.py');
		break;
}
?>
