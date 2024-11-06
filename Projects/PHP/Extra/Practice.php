<?php
    $conexion=mysqli_connect("localhost", "root", "", "ejemplo");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Registrarse</h1>

    <form method="post">
        <div class="container">
    <input type="text" name="Nombre" class="Nombre" placeholder="Nombre">
    <input type="text" name="Apellidos" class="Apellidos" placeholder="Apellidos">
    <input type="submit" name ="Enviar" value="Enviar">
</div>
</form>

<?php
if(isset($_POST['Enviar'])){
    $nombre = trim($_POST['Nombre']);
    $apellidos = trim($_POST['Apellidos']);

    $consulta = "INSERT INTO tabla VALUES ('$nombre', '$apellidos')";
    $resultado = mysqli_query($conexion, $consulta);

    if($resultado){
        echo "Datos enviados";
    }else{
        echo "Hubo un error";
    }
}

mysqli_close($conexion);

?>
</body>
</html>
