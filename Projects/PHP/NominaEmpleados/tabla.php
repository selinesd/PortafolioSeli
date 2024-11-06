<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel ="stylesheet" href="style.css">
    <title>Tabla</title>
</head>
<body>
    <div class="titulo">Tabla De Datos</div>
    
    <?php
    $connection = mysqli_connect ("localhost", "root", "", "nomina");

    if($connection->connect_error){
        die("ERROR Su conexión ha fallado. " . $connection->connect_error);
    }else{

        $sql = "SELECT * FROM tabla";
    $answer = mysqli_query($connection,$sql);

    if($answer->num_rows>0){
        echo"<table border = '1' class = 'container'>
            <tr>
            <th>Nombre</th>
            <th>Apellidos</th>
            <th>Cédula</th>
            <th>Posición</th>
            <th>Sueldo Bruto</th>
            <th>Imp. Sobre Renta</th>
            <th>Seguro De Vida</th>
            <th>Seguro De Pensiones</th>
            <th>Plan Odonto.</th>
            <th>Seguro De Salud Fam.</th>
            <th>Descuento Funerario</th>
            <th>Plan Retiro</th>
            <th>Incentivos</th>
            <th>Sueldo Neto</th>
        </tr>";
        while($ingresa = $answer->fetch_assoc()){
            echo"<tr>
            <td>{$ingresa['Nombre']}</td>
            <td>{$ingresa['Apellidos']}</td>
            <td>{$ingresa['Cedula']}</td>
            <td>{$ingresa['Posicion']}</td>
            <td>{$ingresa['SueldoBruto']}</td>
            <td>{$ingresa['ImpSobreRenta']}</td>
            <td>{$ingresa['SeguroDeVida']}</td>
            <td>{$ingresa['SeguroPensiones']}</td>
            <td>{$ingresa['PlanOdontologico']}</td>
            <td>{$ingresa['SeguroFamiliarSalud']}</td>
            <td>{$ingresa['DescuentoFuneral']}</td>
            <td>{$ingresa['PlanRetiro']}</td>
            <td>{$ingresa['Incentivos']}</td>
            <td>{$ingresa['SueldoNeto']}</td>
            </tr>";
        }
        echo"</table>";
    }else{
        echo"No se encontraron los resultados";
    }

    $answer->free();
}

mysqli_close($connection);
    ?>

<div id="volver">
    <a href="Index.php">
    <input type="button" value="Volver" name="Volver" id="Volver">
</a>
</div>

</body>
</html>