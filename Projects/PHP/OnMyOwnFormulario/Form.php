<?php
$conexion = mysqli_connect("localhost", "root", "", "conexiones");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Design.css">
    <title>Formulario</title>
</head>
<body>

<div class="Fondo"></div>
<div class="Titulo">Registrarse:</div>

<form method="post" id="formulario">
<div class="Fila">
    <label for="Nombre">Nombre: </label>
    <input type="text" name ="Nombre" class="Nombre" placeholder="Nombre aqui:">
</div>

<div class="Fila">
    <label for="Apellidos">Apellidos: </label>
    <input type="text" name ="Apellidos" class="Apellidos" placeholder="Apellidos">
</div>

<div class="Fila">
    <label>Contraseña</label>
    <input type="password" class ="password"name="password" id="password">
</div>

<div class="Fila">
    <label>Confirmar Contraseña:</label>
    <input type="password" class="confirm" name="confirm" id="confirm">
    <p id="message">Contraseña <span></a</p>
</div>

<div class="Fila">
    <input type="submit" name ="Enviar" class="Enviar" >
</div>
</form>

<script>
document.querySelector('.Enviar').onclick = function(){

var password = document.querySelector('.password').value,
    confirmar = document.querySelector('.confirm').value;

if(password == ""){
    alert("El campo no puede estar vacio.");
}else if(password != confirmar){
    alert("Sus contraseñas son distintas.");
    return false
}else if(password == confirmar){
    alert("¡Perfecto!");
}
return true
}

    </script>
</body>
</html>

<?php
if(isset($_POST['Enviar'])){
        $nombre = trim($_POST['Nombre']);
        $apellidos = trim($_POST['Apellidos']);
        $password = trim($_POST['password']);

        $consulta = "INSERT INTO aver VALUES ('$nombre', '$apellidos', '$password')";
        $result = mysqli_query($conexion, $consulta);

        if($result){
            //te mandara a la otra pagina
            header("Location: login.php");
            exit();
        }else{
            echo "Conexión fallida";
    }
}

mysqli_close($conexion);
?>
