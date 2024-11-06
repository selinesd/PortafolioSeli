<?php
$conexion = mysqli_connect("localhost", "root", "", "nomina");
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Ingresar</title>

<body>

<div class="title">Nómina De Empleados</div>
<form method="POST">
        <div>
            <label for="nombre">Nombre:</label>
            <input type="text" id="nombre" name="nombre">
        </div>
        <div>
            <label for="apellidos">Apellidos:</label>
            <input type="text" id="apellidos" name="apellidos">
        </div>
        <div>
            <label for="cedula">Cédula:</label>
            <input type="text" id="cedula" name="cedula">
        </div>
        <div>
            <label for="posicion">Posición:</label>
            <input type="text" id="posicion" name="posicion">
        </div>
        <div>
            <label for="sueldo-bruto">Sueldo Bruto:</label>
            <input type="number" id="sueldo-bruto" name="sueldo-bruto">
        </div>
        <div id="Selecciona">
            <label for="incentivos">Elija su incentivo: </label>
            <select name="incentivos[]" id="incentivos">
                <option value ="0">No utlizo incentivos</option>
    <option value="1500">Incentivo por Formación Títulos Académicos</option>
    <option value="500">Incentivo por Evaluación de Desempeño</option>
    <option value="200">Incentivo por Experiencia Años en Servicio</option>
</select>
</div>

<div class="form-group" id="Odonto">
    <label>¿Utilizara Plan Odontologico?</label>
    <input type="radio" name="plan" value="Si" id="Si">
    <label for="Si">Si</label>
    <input type="radio" name="plan" value="No" id="No">
    <label for="No">No</label>
</div>

        <div id="enviar">
        <input type="submit" id="enviar" name="enviar">
</div>

<div id="tabla_2">
    <a href="tabla.php">
    <input type="button" value="Tabla" name="Tabla" id="Tabla">
</a>
</div>
    </form>

    <?php
    if (isset($_POST['enviar'])) {
        $nombre = trim($_POST['nombre']);
        $apellidos = trim($_POST['apellidos']);
        $cedula = trim($_POST['cedula']);
        $posicion = trim($_POST['posicion']);
        $sueldoBruto = trim($_POST['sueldo-bruto']);

        $incentivos = 0;
        if(isset($_POST['incentivos'])){
            foreach($_POST['incentivos'] as $incentivo){
                $incentivos += $incentivo;
            }
        }

        if (isset($_POST['plan'])) {
            $planSeleccionado = $_POST['plan'];
        
            if ($planSeleccionado == "Si") {
                $PlanOdontologico = (50 * 2) + (20 * 2); 
            } else {
                $PlanOdontologico = 0; 
            }
        }
        

        $sueldoAnual = $sueldoBruto * 12;
        if ($sueldoAnual <= 416220.00) {
            $impuestoRenta = 0;
        } elseif ($sueldoAnual <= 624329.00) {
            $impuestoRenta = ($sueldoAnual - 416220.01) * 0.15;
        } elseif ($sueldoAnual <= 867123.00) {
            $impuestoRenta = ($sueldoAnual - 624329.01) * 0.20 + 31216.00;
        } else {
            $impuestoRenta = ($sueldoAnual - 867123.01) * 0.25 + 79776.00;
        }

        $ImpSobreRenta = $impuestoRenta / 12;
        $SeguroDeVida = $sueldoBruto * 0.15;
        $SeguroPensiones = $sueldoBruto * 0.0997;
        $SeguroFamiliarSalud = (100 * 5) + (30 * 5); 
        $DescuentoFuneral = 200; 
        $planRetiro = 300; 

        $SueldoNeto = $sueldoBruto - ($ImpSobreRenta + $SeguroDeVida + $SeguroPensiones + $PlanOdontologico + $SeguroFamiliarSalud - $DescuentoFuneral + $planRetiro) + $incentivos;

        $consulta = "INSERT INTO tabla VALUES ('$nombre', '$apellidos','$cedula','$posicion','$sueldoBruto','$ImpSobreRenta','$SeguroDeVida','$SeguroPensiones','$PlanOdontologico','$SeguroFamiliarSalud','$DescuentoFuneral','$planRetiro','$incentivos','$SueldoNeto')";
        $resultado = mysqli_query($conexion, $consulta);

        if($resultado){
            echo "";
        } else {
            echo "Error al conectarse";
        }

    }
    mysqli_close($conexion);
?>

</head>
</body>
</html>