<?php
    try{
        $pdo = new PDO ("mysql: host=localhost; dbname=ConexionesPracticando", "root", "", );

        $pdo -> setAttibute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
        echo "Conexión exitosa. Información del host: ".$pdo->getAttibute(constant("PDO:: ATTR_CONNECTION_STATUS"));
    }catch(PDOException $e){
        die("ERROR al conectarse ".$e->getMessage());
    }
?>