INSERT INTO public.backend_colegio(
	nombre, codigo)
	VALUES ('San Agustín El Paraíso', 1),
	('Santa Rosa de Lima', 2),
	('La Concepción', 3);

INSERT INTO public.backend_carrera(
	nombre, codigo, "estaEnUCAB")
	VALUES ('Letras', 1, true),
	('Psicología', 2, true),
	('Derecho', 3, true),
	('Comunicación Social', 4, true),
	('Contaduría', 5, true),
	('Administración', 6, true),
	('Economía', 7, true)

INSERT INTO public.backend_sede(
	nombre)
	VALUES ('Caracas'),
	('Guayana');

INSERT INTO public.backend_listacodigo(
	nombre, descripcion, "fechaCreacion", "fechaUltimaModificacion")
	VALUES ('Colegios', 'Opciones de colegio', '1-1-2022', '1-1-2022'),
	('Empresas', 'Empresa ideal para trabajar', '1-1-2022', '1-1-2022'),
	('Vivienda', 'Tipo de vivienda', '1-1-2022', '1-1-2022'),
	('Universidades', 'Opciones de universidades', '1-1-2022', '1-1-2022');

INSERT INTO public.backend_categoria(
	codigo, descripcion, "fechaCreacion", "fechaUltimaModificacion", "listaCodigo_id")
	VALUES (1, 'Academia Merici', '1-1-2022', '1-1-2022', 1),
	(2, 'Agustín Codazzi', '1-1-2022', '1-1-2022', 1),
	(3, 'Academia Washington', '1-1-2022', '1-1-2022', 1),
	(4, 'CFI 12 de febrero', '1-1-2022', '1-1-2022', 1),
	(5, 'Cristo Rey', '1-1-2022', '1-1-2022', 1),
	(1, 'Empresas agropecuarias', '1-1-2022', '1-1-2022', 2),
	(2, 'Empresas mineras', '1-1-2022', '1-1-2022', 2),
	(3, 'Empresas comerciales', '1-1-2022', '1-1-2022', 2),
	(4, 'Empresas servicios', '1-1-2022', '1-1-2022', 2),
	(1, 'Rancho', '1-1-2022', '1-1-2022', 3),
	(2, 'Casa', '1-1-2022', '1-1-2022', 3),
	(3, 'Apartamento', '1-1-2022', '1-1-2022', 3),
	(4, 'Quinta', '1-1-2022', '1-1-2022', 3),
	(1, 'UCAB', '1-1-2022', '1-1-2022', 4),
	(2, 'UCV', '1-1-2022', '1-1-2022', 4),
	(3, 'USB', '1-1-2022', '1-1-2022', 4),
	(4, 'UNIMET', '1-1-2022', '1-1-2022', 4),
	(5, 'USM', '1-1-2022', '1-1-2022', 4)

ALTER SEQUENCE backend_lugar_id_seq RESTART WITH 1

INSERT INTO backend_lugar(
	nombre, tipo, fk_lugar_id)
	VALUES
	('Amazonas', 'ESTADO',null),
	('Anzoátegui', 'ESTADO',null),
	('Apure', 'ESTADO',null),
	('Aragua', 'ESTADO',null),
	('Barinas', 'ESTADO',null),
	('Bolívar', 'ESTADO',null),
	('Carabobo', 'ESTADO',null),
	('Cojedes', 'ESTADO',null),
	('Delta Amacuro', 'ESTADO',null),
	('Falcón', 'ESTADO',null),
	('Guárico', 'ESTADO',null),
	('Lara', 'ESTADO',null),
	('Mérida', 'ESTADO',null),
	('Miranda', 'ESTADO',null),
	('Monagas', 'ESTADO',null),
	('Nueva Esparta', 'ESTADO',null),
	('Portuguesa', 'ESTADO',null),
	('Sucre', 'ESTADO',null),
	('Táchira', 'ESTADO',null),
	('Trujillo', 'ESTADO',null),
	('Vargas', 'ESTADO',null),
	('Yaracuy', 'ESTADO',null),
	('Zulia', 'ESTADO',null),
	('Distrito Capital', 'ESTADO',null),

('Alto Orinoco','MUNICIPIO',1),
	('Atabapo','MUNICIPIO',1),
	('Atures','MUNICIPIO',1),
	('Autana','MUNICIPIO',1),
	('Manapiare','MUNICIPIO',1),
	('Maroa','MUNICIPIO',1),
	('Río Negro','MUNICIPIO',1),
	('Anaco','MUNICIPIO',2),
	('Aragua','MUNICIPIO',2),
	('Manuel Ezequiel Bruzual','MUNICIPIO',2),
	('Diego Bautista Urbaneja','MUNICIPIO',2),
	('Fernando Peñalver','MUNICIPIO',2),
	('Francisco Del Carmen Carvajal','MUNICIPIO',2),
	('General Sir Arthur McGregor','MUNICIPIO',2),
	('Guanta','MUNICIPIO',2),
	('Independencia','MUNICIPIO',2),
	('José Gregorio Monagas','MUNICIPIO',2),
	('Juan Antonio Sotillo','MUNICIPIO',2),
	('Juan Manuel Cajigal','MUNICIPIO',2),
	('Libertad','MUNICIPIO',2),
	('Francisco de Miranda','MUNICIPIO',2),
	('Pedro María Freites','MUNICIPIO',2),
	('Píritu','MUNICIPIO',2),
	('San José de Guanipa','MUNICIPIO',2),
	('San Juan de Capistrano','MUNICIPIO',2),
	('Santa Ana','MUNICIPIO',2),
	('Simón Bolívar','MUNICIPIO',2),
	('Simón Rodríguez','MUNICIPIO',2),
	('Achaguas','MUNICIPIO',3),
	('Biruaca','MUNICIPIO',3),
	('Muñóz','MUNICIPIO',3),
	('Páez','MUNICIPIO',3),
	('Pedro Camejo','MUNICIPIO',3),
	('Rómulo Gallegos','MUNICIPIO',3),
	('San Fernando','MUNICIPIO',3),
	('Atanasio Girardot','MUNICIPIO',4),
	('Bolívar','MUNICIPIO',4),
	('Camatagua','MUNICIPIO',4),
	('Francisco Linares Alcántara','MUNICIPIO',4),
	('José Ángel Lamas','MUNICIPIO',4),
	('José Félix Ribas','MUNICIPIO',4),
	('José Rafael Revenga','MUNICIPIO',4),
	('Libertador','MUNICIPIO',4),
	('Mario Briceño Iragorry','MUNICIPIO',4),
	('Ocumare de la Costa de Oro','MUNICIPIO',4),
	('San Casimiro','MUNICIPIO',4),
	('San Sebastián','MUNICIPIO',4),
	('Santiago Mariño','MUNICIPIO',4),
	('Santos Michelena','MUNICIPIO',4),
	('Sucre','MUNICIPIO',4),
	('Tovar','MUNICIPIO',4),
	('Urdaneta','MUNICIPIO',4),
	('Zamora','MUNICIPIO',4),
	('Alberto Arvelo Torrealba','MUNICIPIO',5),
	('Andrés Eloy Blanco','MUNICIPIO',5),
	('Antonio José de Sucre','MUNICIPIO',5),
	('Arismendi','MUNICIPIO',5),
	('Barinas','MUNICIPIO',5),
	('Bolívar','MUNICIPIO',5),
	('Cruz Paredes','MUNICIPIO',5),
	('Ezequiel Zamora','MUNICIPIO',5),
	('Obispos','MUNICIPIO',5),
	('Pedraza','MUNICIPIO',5),
	('Rojas','MUNICIPIO',5),
	('Sosa','MUNICIPIO',5),
	('Caroní','MUNICIPIO',6),
	('Cedeño','MUNICIPIO',6),
	('El Callao','MUNICIPIO',6),
	('Gran Sabana','MUNICIPIO',6),
	('Heres','MUNICIPIO',6),
	('Piar','MUNICIPIO',6),
	('Angostura (Raúl Leoni)','MUNICIPIO',6),
	('Roscio','MUNICIPIO',6),
	('Sifontes','MUNICIPIO',6),
	('Sucre','MUNICIPIO',6),
	('Padre Pedro Chien','MUNICIPIO',6),
	('Bejuma','MUNICIPIO',7),
	('Carlos Arvelo','MUNICIPIO',7),
	('Diego Ibarra','MUNICIPIO',7),
	('Guacara','MUNICIPIO',7),
	('Juan José Mora','MUNICIPIO',7),
	('Libertador','MUNICIPIO',7),
	('Los Guayos','MUNICIPIO',7),
	('Miranda','MUNICIPIO',7),
	('Montalbán','MUNICIPIO',7),
	('Naguanagua','MUNICIPIO',7),
	('Puerto Cabello','MUNICIPIO',7),
	('San Diego','MUNICIPIO',7),
	('San Joaquín','MUNICIPIO',7),
	('Valencia','MUNICIPIO',7),
	('Anzoátegui','MUNICIPIO',8),
	('Tinaquillo','MUNICIPIO',8),
	('Girardot','MUNICIPIO',8),
	('Lima Blanco','MUNICIPIO',8),
	('Pao de San Juan Bautista','MUNICIPIO',8),
	('Ricaurte','MUNICIPIO',8),
	('Rómulo Gallegos','MUNICIPIO',8),
	('San Carlos','MUNICIPIO',8),
	('Tinaco','MUNICIPIO',8),
	('Antonio Díaz','MUNICIPIO',9),
	('Casacoima','MUNICIPIO',9),
	('Pedernales','MUNICIPIO',9),
	('Tucupita','MUNICIPIO',9),
	('Acosta','MUNICIPIO',10),
	('Bolívar','MUNICIPIO',10),
	('Buchivacoa','MUNICIPIO',10),
	('Cacique Manaure','MUNICIPIO',10),
	('Carirubana','MUNICIPIO',10),
	('Colina','MUNICIPIO',10),
	('Dabajuro','MUNICIPIO',10),
	('Democracia','MUNICIPIO',10),
	('Falcón','MUNICIPIO',10),
	('Federación','MUNICIPIO',10),
	('Jacura','MUNICIPIO',10),
	('José Laurencio Silva','MUNICIPIO',10),
	('Los Taques','MUNICIPIO',10),
	('Mauroa','MUNICIPIO',10),
	('Miranda','MUNICIPIO',10),
	('Monseñor Iturriza','MUNICIPIO',10),
	('Palmasola','MUNICIPIO',10),
	('Petit','MUNICIPIO',10),
	('Píritu','MUNICIPIO',10),
	('San Francisco','MUNICIPIO',10),
	('Sucre','MUNICIPIO',10),
	('Tocópero','MUNICIPIO',10),
	('Unión','MUNICIPIO',10),
	('Urumaco','MUNICIPIO',10),
	('Zamora','MUNICIPIO',10),
	('Camaguán','MUNICIPIO',11),
	('Chaguaramas','MUNICIPIO',11),
	('El Socorro','MUNICIPIO',11),
	('José Félix Ribas','MUNICIPIO',11),
	('José Tadeo Monagas','MUNICIPIO',11),
	('Juan Germán Roscio','MUNICIPIO',11),
	('Julián Mellado','MUNICIPIO',11),
	('Las Mercedes','MUNICIPIO',11),
	('Leonardo Infante','MUNICIPIO',11),
	('Pedro Zaraza','MUNICIPIO',11),
	('Ortíz','MUNICIPIO',11),
	('San Gerónimo de Guayabal','MUNICIPIO',11),
	('San José de Guaribe','MUNICIPIO',11),
	('Santa María de Ipire','MUNICIPIO',11),
	('Sebastián Francisco de Miranda','MUNICIPIO',11),
	('Andrés Eloy Blanco','MUNICIPIO',12),
	('Crespo','MUNICIPIO',12),
	('Iribarren','MUNICIPIO',12),
	('Jiménez','MUNICIPIO',12),
	('Morán','MUNICIPIO',12),
	('Palavecino','MUNICIPIO',12),
	('Simón Planas','MUNICIPIO',12),
	('Torres','MUNICIPIO',12),
	('Urdaneta','MUNICIPIO',12),
	('Alberto Adriani','MUNICIPIO',13),
	('Andrés Bello','MUNICIPIO',13),
	('Antonio Pinto Salinas','MUNICIPIO',13),
	('Aricagua','MUNICIPIO',13),
	('Arzobispo Chacón','MUNICIPIO',13),
	('Campo Elías','MUNICIPIO',13),
	('Caracciolo Parra Olmedo','MUNICIPIO',13),
	('Cardenal Quintero','MUNICIPIO',13),
	('Guaraque','MUNICIPIO',13),
	('Julio César Salas','MUNICIPIO',13),
	('Justo Briceño','MUNICIPIO',13),
	('Libertador','MUNICIPIO',13),
	('Miranda','MUNICIPIO',13),
	('Obispo Ramos de Lora','MUNICIPIO',13),
	('Padre Noguera','MUNICIPIO',13),
	('Pueblo Llano','MUNICIPIO',13),
	('Rangel','MUNICIPIO',13),
	('Rivas Dávila','MUNICIPIO',13),
	('Santos Marquina','MUNICIPIO',13),
	('Sucre','MUNICIPIO',13),
	('Tovar','MUNICIPIO',13),
	('Tulio Febres Cordero','MUNICIPIO',13),
	('Zea','MUNICIPIO',13),
	('Acevedo','MUNICIPIO',14),
	('Andrés Bello','MUNICIPIO',14),
	('Baruta','MUNICIPIO',14),
	('Brión','MUNICIPIO',14),
	('Buroz','MUNICIPIO',14),
	('Carrizal','MUNICIPIO',14),
	('Chacao','MUNICIPIO',14),
	('Cristóbal Rojas','MUNICIPIO',14),
	('El Hatillo','MUNICIPIO',14),
	('Guaicaipuro','MUNICIPIO',14),
	('Independencia','MUNICIPIO',14),
	('Lander','MUNICIPIO',14),
	('Los Salias','MUNICIPIO',14),
	('Páez','MUNICIPIO',14),
	('Paz Castillo','MUNICIPIO',14),
	('Pedro Gual','MUNICIPIO',14),
	('Plaza','MUNICIPIO',14),
	('Simón Bolívar','MUNICIPIO',14),
	('Sucre','MUNICIPIO',14),
	('Urdaneta','MUNICIPIO',14),
	('Zamora','MUNICIPIO',14),
	('Acosta','MUNICIPIO',15),
	('Aguasay','MUNICIPIO',15),
	('Bolívar','MUNICIPIO',15),
	('Caripe','MUNICIPIO',15),
	('Cedeño','MUNICIPIO',15),
	('Ezequiel Zamora','MUNICIPIO',15),
	('Libertador','MUNICIPIO',15),
	('Maturín','MUNICIPIO',15),
	('Piar','MUNICIPIO',15),
	('Punceres','MUNICIPIO',15),
	('Santa Bárbara','MUNICIPIO',15),
	('Sotillo','MUNICIPIO',15),
	('Uracoa','MUNICIPIO',15),
	('Antolín del Campo','MUNICIPIO',16),
	('Arismendi','MUNICIPIO',16),
	('García','MUNICIPIO',16),
	('Gómez','MUNICIPIO',16),
	('Maneiro','MUNICIPIO',16),
	('Marcano','MUNICIPIO',16),
	('Mariño','MUNICIPIO',16),
	('Península de Macanao','MUNICIPIO',16),
	('Tubores','MUNICIPIO',16),
	('Villalba','MUNICIPIO',16),
	('Díaz','MUNICIPIO',16),
	('Agua Blanca','MUNICIPIO',17),
	('Araure','MUNICIPIO',17),
	('Esteller','MUNICIPIO',17),
	('Guanare','MUNICIPIO',17),
	('Guanarito','MUNICIPIO',17),
	('Monseñor José Vicente de Unda','MUNICIPIO',17),
	('Ospino','MUNICIPIO',17),
	('Páez','MUNICIPIO',17),
	('Papelón','MUNICIPIO',17),
	('San Genaro de Boconoíto','MUNICIPIO',17),
	('San Rafael de Onoto','MUNICIPIO',17),
	('Santa Rosalía','MUNICIPIO',17),
	('Sucre','MUNICIPIO',17),
	('Turén','MUNICIPIO',17),
	('Andrés Eloy Blanco','MUNICIPIO',18),
	('Andrés Mata','MUNICIPIO',18),
	('Arismendi','MUNICIPIO',18),
	('Benítez','MUNICIPIO',18),
	('Bermúdez','MUNICIPIO',18),
	('Bolívar','MUNICIPIO',18),
	('Cajigal','MUNICIPIO',18),
	('Cruz Salmerón Acosta','MUNICIPIO',18),
	('Libertador','MUNICIPIO',18),
	('Mariño','MUNICIPIO',18),
	('Mejía','MUNICIPIO',18),
	('Montes','MUNICIPIO',18),
	('Ribero','MUNICIPIO',18),
	('Sucre','MUNICIPIO',18),
	('Valdéz','MUNICIPIO',18),
	('Andrés Bello','MUNICIPIO',19),
	('Antonio Rómulo Costa','MUNICIPIO',19),
	('Ayacucho','MUNICIPIO',19),
	('Bolívar','MUNICIPIO',19),
	('Cárdenas','MUNICIPIO',19),
	('Córdoba','MUNICIPIO',19),
	('Fernández Feo','MUNICIPIO',19),
	('Francisco de Miranda','MUNICIPIO',19),
	('García de Hevia','MUNICIPIO',19),
	('Guásimos','MUNICIPIO',19),
	('Independencia','MUNICIPIO',19),
	('Jáuregui','MUNICIPIO',19),
	('José María Vargas','MUNICIPIO',19),
	('Junín','MUNICIPIO',19),
	('Libertad','MUNICIPIO',19),
	('Libertador','MUNICIPIO',19),
	('Lobatera','MUNICIPIO',19),
	('Michelena','MUNICIPIO',19),
	('Panamericano','MUNICIPIO',19),
	('Pedro María Ureña','MUNICIPIO',19),
	('Rafael Urdaneta','MUNICIPIO',19),
	('Samuel Darío Maldonado','MUNICIPIO',19),
	('San Cristóbal','MUNICIPIO',19),
	('Seboruco','MUNICIPIO',19),
	('Simón Rodríguez','MUNICIPIO',19),
	('Sucre','MUNICIPIO',19),
	('Torbes','MUNICIPIO',19),
	('Uribante','MUNICIPIO',19),
	('San Judas Tadeo','MUNICIPIO',19),
	('Andrés Bello','MUNICIPIO',20),
	('Boconó','MUNICIPIO',20),
	('Bolívar','MUNICIPIO',20),
	('Candelaria','MUNICIPIO',20),
	('Carache','MUNICIPIO',20),
	('Escuque','MUNICIPIO',20),
	('José Felipe Márquez Cañizalez','MUNICIPIO',20),
	('Juan Vicente Campos Elías','MUNICIPIO',20),
	('La Ceiba','MUNICIPIO',20),
	('Miranda','MUNICIPIO',20),
	('Monte Carmelo','MUNICIPIO',20),
	('Motatán','MUNICIPIO',20),
	('Pampán','MUNICIPIO',20),
	('Pampanito','MUNICIPIO',20),
	('Rafael Rangel','MUNICIPIO',20),
	('San Rafael de Carvajal','MUNICIPIO',20),
	('Sucre','MUNICIPIO',20),
	('Trujillo','MUNICIPIO',20),
	('Urdaneta','MUNICIPIO',20),
	('Valera','MUNICIPIO',20),
	('Vargas','MUNICIPIO',21),
	('Arístides Bastidas','MUNICIPIO',22),
	('Bolívar','MUNICIPIO',22),
	('Bruzual','MUNICIPIO',22),
	('Cocorote','MUNICIPIO',22),
	('Independencia','MUNICIPIO',22),
	('José Antonio Páez','MUNICIPIO',22),
	('La Trinidad','MUNICIPIO',22),
	('Manuel Monge','MUNICIPIO',22),
	('Nirgua','MUNICIPIO',22),
	('Peña','MUNICIPIO',22),
	('San Felipe','MUNICIPIO',22),
	('Sucre','MUNICIPIO',22),
	('Urachiche','MUNICIPIO',22),
	('José Joaquín Veroes','MUNICIPIO',22),
	('Almirante Padilla','MUNICIPIO', 23),
	('Baralt','MUNICIPIO', 23),
	('Cabimas','MUNICIPIO', 23),
	('Catatumbo','MUNICIPIO', 23),
	('Colón','MUNICIPIO', 23),
	('Francisco Javier Pulgar','MUNICIPIO', 23),
	('Guajira','MUNICIPIO', 23),
	('Jesús Enrique Losada','MUNICIPIO', 23),
	('Jesús María Semprún','MUNICIPIO', 23),
	('La Cañada de Urdaneta','MUNICIPIO', 23),
	('Lagunillas','MUNICIPIO', 23),
	('Machiques de Perijá','MUNICIPIO', 23),
	('Mara','MUNICIPIO', 23),
	('Maracaibo','MUNICIPIO', 23),
	('Miranda','MUNICIPIO', 23),
	('Rosario de Perijá','MUNICIPIO', 23),
	('San Francisco','MUNICIPIO', 23),
	('Santa Rita','MUNICIPIO', 23),
	('Simón Bolívar','MUNICIPIO', 23),
	('Sucre','MUNICIPIO', 23),
	('Valmore Rodríguez','MUNICIPIO', 23),
	('Libertador', 'MUNICIPIO',24)
