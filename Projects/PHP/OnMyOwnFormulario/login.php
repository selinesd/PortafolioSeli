<?php
$connect = mysqli_connect("localhost", "root", "", "conexiones");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Design.css">
    <title>Log-In</title>
</head>
<body>

<div class="Fondo"></div>
<div class="Titulo">Iniciar Sesión</div>

<form method="POST" id="loginform" onsubmit="return validateLoginForm()">
    <div class="Fila">
        <label for="Nombre">Nombre:</label>
        <input type="text" name="Nombre" id="loginNombre" class="Nombre" placeholder="Ingrese aqui:" required>
    </div>

    <div class="Fila">
        <label>Contraseña:</label>
        <input type="password" name="password" class="password" id="loginPassword" placeholder="Ingrese aqui:" required>
    </div>

    <div class="Fila">
        <input type="submit" name="Login" value="Login" class="Enviar">
    </div>
</form>

<script>
// JavaScript form validation
function validateLoginForm() {
    const username = document.getElementById("loginNombre").value.trim();
    const password = document.getElementById("loginPassword").value.trim();

    if (username === "" || username.length < 3) {
        alert("Nombre debe tener al menos 3 caracteres.");
        return false;
    }

    if (password === "" || password.length < 6) {
        alert("Contraseña debe tener al menos 6 caracteres.");
        return false;
    }

    return true;
}
</script>

<?php
if(isset($_POST['Login'])){
    $nombre = trim($_POST['Nombre']);
    $password = trim($_POST['password']);

    // Query to verify the user exists
    $consulta = "SELECT * FROM aver WHERE Nombre = '$nombre'";
    $result = mysqli_query($connect, $consulta);
    // Handle the result here (e.g., checking password match)

    if($result){
        header("Location: principal.php");
        exit();
    } else{
        alert("Error");
    }
}
?>

</body>
</html>
