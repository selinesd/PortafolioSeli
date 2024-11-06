<?php
    $mysqli = mysqli_connect ("localhost", "root", "", "ConexionesPracticando");

    if($mysqli === false){
        die("ERROR al conectarse".mysqli_connect_error());
    }

    echo "Conexión exitosa. Información del Host: ".mysqli_get_host_info($mysqli);
?>