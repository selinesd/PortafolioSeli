<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <title>Practice</title>
</head>
<body>

    <div class="input">
    <input type="password" name="password" id="password" placeholder="Password">
    <p id="message">Password is <span id="strength"></p>
</div>

<script>
    var pass = document.getElementById("password");
    var msg = document.getElementById("message");
    var str = document.getElementById("strength");

    pass.addEventListener('input', () => {
        if(pass.value.length > 0){
            msg.style.display = "block";
        }else{
            msg.style.display = "none";
        }
        if(pass.value.length < 4){
            str.innerHTML = "weak";
            pass.style.borderColor = "red";
            msg.style.color = "red";
        }else if(pass.value.length >= 4 && pass.value.length < 8){
            str.innerHTML = "medium";
            pass.style.borderColor = "yellow";
            msg.style.color = "yellow";
        }else if(pass.value.length >= 8 && pass.value.length < 12){
            str.innerHTML = "strong";
            pass.style.borderColor = "green";
            msg.style.color = "green";
        }
    })

</script>
</body>
</html>