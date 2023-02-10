<?php

$Presidente = [
  "nombres" => "Guillermo",
  "apellidos" => "Lasso",
  "fecha_nacimiento" => "16-11-1995",
  "edad" => 67,
  "pais_nacimiento" => "Ecuador",
  "ciudad" => "Guayaquil",
  "Profesiones" => "Banquero y Politico",
  "Partido" => "Movimiento Creo",
  "Cargo" => "Movimiento Creo",
  "nacionalidad" => "Ecuatoriano"
];

$Presidente_json = json_encode($Presidente);

$data = json_decode($Presidente_json);

echo "Nombre: " . $data->nombres . " " . $data->apellidos . "\n";
echo "Fecha de Nacimiento: " . $data->fecha_nacimiento . "\n";
echo "Edad: " . $data->edad . "\n";
echo "País de Nacimiento: " . $data->pais_nacimiento . "\n";
echo "Ciudad: " . $data->ciudad . "\n";
echo "Profesiones: " . $data->Profesiones . "\n";
echo "Partido: " . $data->Partido . "\n";
echo "Cargo: " . $data->Cargo . "\n";
echo "Nacionalidad: " . $data->nacionalidad . "\n";

?>