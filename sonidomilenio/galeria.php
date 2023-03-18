<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">

    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css">
    <link rel="stylesheet" href="css/carrusel.css">
    <title>Sonido Milenio</title>
</head>

<body>


    <?php
    include "source/menu.html";
    include "source/carousel.html"; ?>

    <main>
        <div class="container-fluid">
            <div class="text-center">
                <img src="media/logo.png" class="img-fluid" alt="...">
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
                    Pellentesque et dolor dignissim, sodales arcu non, scelerisque magna. 
                    Nam sollicitudin libero eu laoreet faucibus. Curabitur auctor purus mi, 
                    vitae tincidunt mi consequat sed. Suspendisse egestas, elit ultricies hendrerit 
                    lacinia, leo tellus vehicula urna, nec facilisis leo sapien sed est. 
                    Sed sed facilisis nibh, in sagittis erat. Vestibulum cursus gravida risus 
                    sit amet euismod. Fusce at aliquet nibh. Quisque ullamcorper malesuada orci 
                    quis semper. Aliquam vitae finibus purus. Praesent eu felis vel augue commodo 
                    accumsan id vel est. Curabitur posuere id nunc rutrum egestas. Donec quis turpis
                    eget massa scelerisque ornare. Proin luctus neque at enim imperdiet, at 
                    scelerisque tortor ornare. Fusce aliquet enim vel mollis fringilla.</p>
            </div>
            <?php include "source/galery.html"?>
        </div>



        <?php include "source/footer.html" ?>
    </main>

</body>

</html>