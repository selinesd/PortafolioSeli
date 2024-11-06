<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Trabajo Jhoan</title>
</head>
<body>

<?php
$Servidor = "localhost";
$Contraseña = "";
$BaseDatos = "datos";
$Usuario = "root1";

$mysqli = new mysqli ($Servidor, $Usuario, $Contraseña, $BaseDatos);

if($mysqli->connect_error){
    die("ERROR Su conexión ha fallado. " . $mysqli->connect_error);
}else{

     $consulta = "SELECT Nombres, Apellidos, Sexo, Fecha_nacimiento, Correo, Estado_Civil, Edad, Teléfono, Dirección, Fecha_Ingreso FROM datos2";
     $resultado = $mysqli->query($consulta);
 
     if ($resultado->num_rows > 0) {
         echo "<table border='1'>
                 <tr>
                     <th>Nombres</th>
                     <th>Apellidos</th>
                     <th>Sexo</th>
                     <th>Fecha de Nacimiento</th>
                     <th>Correo</th>
                     <th>Estado Civil</th>
                     <th>Edad</th>
                     <th>Teléfono</th>
                     <th>Dirección</th>
                     <th>Fecha de Ingreso</th>
                 </tr>";
 
         while($fila = $resultado->fetch_assoc()) {
             echo "<tr>
                     <td>{$fila['Nombres']}</td>
                     <td>{$fila['Apellidos']}</td>
                     <td>{$fila['Sexo']}</td>
                     <td>{$fila['Fecha_nacimiento']}</td>
                     <td>{$fila['Correo']}</td>
                     <td>{$fila['Estado_Civil']}</td>
                     <td>{$fila['Edad']}</td>
                     <td>{$fila['Teléfono']}</td>
                     <td>{$fila['Dirección']}</td>
                     <td>{$fila['Fecha_Ingreso']}</td>
                   </tr>";
         }
         echo "</table>";
    } else {
        echo "No se encontraron resultados en la tabla.";
    }

    $resultado->free();
        } 
        
    $mysqli->close();
?>
    
</body>
</html>