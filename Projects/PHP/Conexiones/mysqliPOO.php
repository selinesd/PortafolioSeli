<?php
    $mysqli = new mysqli ("localhost", "root", "", "ConexionesPracticando");

    if($mysqli === false){
        die("ERROR al conectarse ".$mysqli->Connect_error);
    }

    echo "Conexión exitosa desde MySQL con POO. Información del Host: ".$mysqli->host_info;
?>