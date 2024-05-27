INSERT INTO paises (codigo, nombre) VALUES (57, 'COLOMBIA');

INSERT INTO departamentos (codigo, nombre, cod_pais_id) VALUES (76, 'VALLE DEL CAUCA', 57);
INSERT INTO departamentos (codigo, nombre, cod_pais_id) VALUES (19, 'CAUCA', 57);

INSERT INTO ciudades (codigo, nombre, cod_dpto_id) VALUES (76001, 'CALI', 76);
INSERT INTO ciudades (codigo, nombre, cod_dpto_id) VALUES (76364, 'JAMUNDI', 76);
INSERT INTO ciudades (codigo, nombre, cod_dpto_id) VALUES (19001, 'POPAYAN', 19);

INSERT INTO facultades (codigo, nombre, ubicacion, nro_telefono) VALUES (1, 'INGENIERIA', 'P38-203', '3197906');

INSERT INTO sedes (codigo, nombre, cod_ciudad_id) VALUES (1, 'PANCE', 76001);

INSERT INTO tipos_contratacion (nombre) VALUES ('PRESTACION DE SERVICIOS');
INSERT INTO tipos_contratacion (nombre) VALUES ('CONTRATO A TERMINO INDEFINIDO');
INSERT INTO tipos_contratacion (nombre) VALUES ('CONTRATO A TERMINO DEFINIDO');

INSERT INTO tipos_empleado (nombre) VALUES ('ADMINISTRATIVO');
INSERT INTO tipos_empleado (nombre) VALUES ('DOCENTE');

INSERT INTO empleados (identificacion, nombres, apellidos, email, tipo_contratacion_id, tipo_empleado_id, cod_facultad_id, codigo_sede_id, lugar_nacimiento_id) 
VALUES ('10', 'ROCIO', 'LOPEZ', 'RLOPEZ@U.EDU.CO', 'CONTRATO A TERMINO INDEFINIDO', 'ADMINISTRATIVO', 1, 1, 76364);

INSERT INTO empleados (identificacion, nombres, apellidos, email, tipo_contratacion_id, tipo_empleado_id, cod_facultad_id, codigo_sede_id, lugar_nacimiento_id) 
VALUES ('11', 'JOSE', 'JURADO', 'JJURADO@U.EDU.CO', 'CONTRATO A TERMINO INDEFINIDO', 'DOCENTE', 1, 1, 19001);

INSERT INTO areas (codigo, nombre, codigo_facultad_id, id_coordinador_id) VALUES (1, 'CSI', 1, '10');

INSERT INTO programas (codigo, nombre, codigo_area_id) VALUES (15, 'INGENIERIA DE SISTEMAS', 1);

-- Insertar datos en la tabla "lugares"
INSERT INTO lugares (nombre, direccion, ciudad_id) VALUES ('Auditorio Principal', 'Calle 123', 76001);
INSERT INTO lugares (nombre, direccion, ciudad_id) VALUES ('Sala de Conferencias', 'Avenida 456', 19001);

-- Insertar datos en la tabla "usuarios"
INSERT INTO usuarios (identificacion, nombre_usuario, nombre_completo, tipo_relacion, email, ciudad_id) VALUES ('1001', 'juanperez', 'Juan Perez', 'Estudiante', 'juan.perez@example.com', 76001);
INSERT INTO usuarios (identificacion, nombre_usuario, nombre_completo, tipo_relacion, email, ciudad_id) VALUES ('1002', 'mariagomez', 'Maria Gomez', 'Docente', 'maria.gomez@example.com', 76364);

-- Insertar el primer evento
INSERT INTO eventos (titulo, descripcion, categorias, fecha, lugar_id, programa_organizador_id) 
VALUES ('Congreso Internacional de Ingeniería', 'Un evento para discutir los avances en ingeniería.', 'Congreso, Ingeniería', '2024-06-01 09:00:00', 
(SELECT id FROM lugares WHERE nombre='Auditorio Principal'), 15);

-- Relacionar usuarios como asistentes y conferencistas para el primer evento
INSERT INTO eventos_asistentes (evento_id, usuario_id) VALUES 
((SELECT id FROM eventos WHERE titulo='Congreso Internacional de Ingeniería'), '1001'),
((SELECT id FROM eventos WHERE titulo='Congreso Internacional de Ingeniería'), '1002');

INSERT INTO eventos_conferencistas (evento_id, usuario_id) VALUES 
((SELECT id FROM eventos WHERE titulo='Congreso Internacional de Ingeniería'), '1002');

-- Relacionar facultades organizadoras para el primer evento
INSERT INTO eventos_facultades_organizadoras (evento_id, facultad_id) VALUES 
((SELECT id FROM eventos WHERE titulo='Congreso Internacional de Ingeniería'), 1);

-- Insertar el segundo evento
INSERT INTO eventos (titulo, descripcion, categorias, fecha, lugar_id, programa_organizador_id) 
VALUES ('Seminario de Artes', 'Un seminario sobre técnicas modernas en artes visuales.', 'Seminario, Artes', '2024-07-15 14:00:00', 
(SELECT id FROM lugares WHERE nombre='Sala de Conferencias'), 15);

-- Relacionar usuarios como asistentes y conferencistas para el segundo evento
INSERT INTO eventos_asistentes (evento_id, usuario_id) VALUES 
((SELECT id FROM eventos WHERE titulo='Seminario de Artes'), '1001'),
((SELECT id FROM eventos WHERE titulo='Seminario de Artes'), '1002');

INSERT INTO eventos_conferencistas (evento_id, usuario_id) VALUES 
((SELECT id FROM eventos WHERE titulo='Seminario de Artes'), '1002');

-- Relacionar facultades organizadoras para el segundo evento
INSERT INTO eventos_facultades_organizadoras (evento_id, facultad_id) VALUES 
((SELECT id FROM eventos WHERE titulo='Seminario de Artes'), 1);

