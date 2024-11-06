<?php
// Verifica que la extensión PHP-GTK esté cargada
if (!class_exists('Gtk')) {
    die("PHP-GTK no está instalado.\n");
}

// Crear una ventana
$window = new GtkWindow();
$window->set_title("Mi Aplicación de Escritorio");
$window->set_default_size(400, 300);

// Añadir un botón
$button = new GtkButton("Presiona aquí");
$window->add($button);

// Conectar el botón a un evento
$button->connect_simple('clicked', function() {
    echo "Botón presionado!\n";
});

// Mostrar todo
$window->show_all();
Gtk::main();
?>