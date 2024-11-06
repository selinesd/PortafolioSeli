<?php
    $connection = mysqli_connect("localhost", "root", "", "SigninPracticaFormOne");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Frontend.css">
    <title>Registrarse</title>
</head>
<body>

    <div class="container">
    <div class="box form-box">
        <header>Registrar</header>
        <form method="post">

    <div class="field1">
        <label for="Nombre">Nombre: </label>
        <input type="text" name="Nombre" id="Nombre" required>
    </div>

    <div class="field2">
        <label for="Apellidos">Apellidos: </label>
        <input type="text" name="Apellidos" id="Apellidos" required>
    </div>

    <div class="field1">
        <label for="Correo">Correo: </label>
        <input type="email" name="Correo" id="Correo" required>
    </div>

    <div class="field2">
        <label for="Civil">Estado Civil: </label>
        <input type="text" name="Civil" id="Civil" required>
    </div>

    <div class="field1">
        <label for="Telefono">Teléfono: </label>
        <input type="text" name="Telefono" id="Telefono" required>
    </div>

    <div class="field2">
        <label for="Direccion">Dirección: </label>
        <input type="text" name="Direccion" id="Direccion" required>
    </div>

    <div class="field3">
        <label for="Sexo">Sexo: </label>
        <input type="text" name="Sexo" id="Sexo" required>
    </div>

    <div class="field4">
        <label for="FechaNacimiento">Fecha De Nacimiento: </label>
        <input type="date" name="FechaNacimiento" id="FechaNacimiento" required>
    </div>

    <div class="field3">
        <label for="Edad">Edad: </label>
        <input type="number" name="Edad" id="Edad" required>
    </div>

    <div class="Enviar">
        <input type="submit" name="Enviar" class ="Enviar" value="Enviar">
    </div>

        </form>
    </div>
    </div>

    <?php
        if (isset($_POST['Enviar'])){
            $nombre = trim($_POST['Nombre']);
            $apellidos = trim($_POST['Apellidos']);
            $sexo = trim($_POST['Sexo']);
            $correo = trim($_POST['Correo']);
            $estadocivil = trim($_POST['Civil']);
            $edad = trim($_POST['Edad']);
            $telefono = trim($_POST['Telefono']);
            $direccion = trim($_POST['Direccion']);
            $fechanacimiento = trim($_POST['FechaNacimiento']);

            $consulta = "INSERT INTO registrarse VALUES ('$nombre','$apellidos','$sexo','$correo','$estadocivil','$edad','$telefono','$direccion','$fechanacimiento')";
            $result = mysqli_query($connection, $consulta);

    if($result){
        echo "Datos enviados con exito";
}else{
    echo "Ha fallado la conexión";
}
        }
        mysqli_close($result);

    ?>
    
</body>
</html>