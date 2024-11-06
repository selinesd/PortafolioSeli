<?php
$connect = mysqli_connect("localhost", "root", "", "signinpracticaformtwo");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css"> 
    <title>Formulario para Registrarse</title>
</head>
<body>

<div class="Baner"></div>
<div class="square"></div>
<img src="logo.png" id="imagen">
        <div class="Principal">Para Registrarse</div>
        <div class="Princi">Formulario </div>
        <div class="linea"></div>
        <div class="name">Sporer</div>
        <div class="nombre">Mega Banco</div>

        <form method="POST">
        <div class="container">
            <div class="form-group">
                <label for="Nombre">Nombre Completo</label>
                <input type="text" name="Nombre" id="Nombre" placeholder="Nombre" required>
                <label></label>
                <input type="text" name="Apellidos" id="Apellidos" placeholder="Apellidos" required>
            </div>

            <div class="form-group">
                <label for="email">E-mail</label>
                <input type="email" name="email" id="email" placeholder="minombre@ejemplo.com" required>
            </div>
            <div class="form-group">
                <label for="telefono">Número de Télefono</label>
                <input type="text" name="telefono" id="telefono" placeholder="(000) 000-000" required>
            </div>

            <div class="form-group">
                <label for="Direccion">Dirección</label>
                <input type="text" name="Direccion" id="Direccion" placeholder="Dirección" required>
                <label></label>
                <input type="text" name="Direccion2" id="Direccion2" placeholder="Dirección 2">
                <label></label>
                <input type="text" name="ciudad" id="ciudad" placeholder="Ciudad" required>
                <label></label>
                <input type="text" name="Estado" id="Estado" placeholder="Estado / Provincia" required>
                <label></label>
                <input type="text" name="zip" id="zip" placeholder="Postal / Código ZIP" required>
            </div>

            <div class="form-group">
                <label>¿Vende o renta un hogar?</label>
                <input type="radio" name="ownership" value="Venta" id="Venta">
                <label for="Venta">Venta</label>
                <input type="radio" name="ownership" value="Renta" id="Renta">
                <label for="Renta">Renta</label>
</div>

            <div class="form-group">
                <label>¿Necesita vender su casa para comprar una nueva?</label>
                <input type="radio" name="sell_home" value="SI" id="SI">
                <label for="SI">Si</label>
                <input type="radio" name="sell_home" value="NO" id="NO">
                <label for="NO">No</label>
</div>

            <div class="form-group">
                <label for="Comentarios">Comentarios o Preguntas:</label>
                <textarea name="Comentarios" id="Comentarios" placeholder="Escriba aqui:"></textarea>
            </div>

            <div class="form-group">
                <input type="submit" name="Submit" value="Submit">
            </div>
            </div>
        </form>

<?php
if(isset($_POST['Submit'])){
    $nombre = trim($_POST['Nombre']);
    $apellidos = trim($_POST['Apellidos']);
    $correo = trim($_POST['email']);
    $telefono = trim($_POST['telefono']);
    $direccion = trim($_POST['Direccion']);
    $direcciondos = trim($_POST['Direccion2']);
    $ciudad = trim($_POST['ciudad']);
    $estado = trim($_POST['Estado']);
    $zip = trim($_POST['zip']);
    $opcionuna = trim($_POST['ownership']);
    $opciondos = trim($_POST['sell_home']);
    $comentarios = trim($_POST['Comentarios']);

    $consulta="INSERT INTO formulario VALUES ('$nombre','$apellidos','$correo','$telefono','$direccion','$direcciondos','$ciudad','$estado','$zip','$opcionuna','$opciondos','$comentarios')";
    $resultado = mysqli_query($connect, $consulta);

    if($resultado){
        echo "Datos guardados con exito";
    }else{
        echo "No se ha guardado correctamente";
    }
}

mysqli_close($connect);
?>

</body>
</html>
