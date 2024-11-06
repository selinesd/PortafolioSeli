<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Principal</title>
</head>
<body>

    <h1>¡Bienvenidos!</h1>

    <div>
    <a href="?logout=true"><button>Cerrar Sesion</button></a>
    <?php
    if (isset($_GET['logout'])) {
    session_destroy();
    header("Location: login.php");
    exit();
    }
    ?>
</body>
</html>