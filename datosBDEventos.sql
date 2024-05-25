insert into eventos.PAISES (codigo,nombre) values (57, 'COLOMBIA'); 
insert into eventos.DEPARTAMENTOS (codigo,nombre, cod_pais) values (76, 'VALLE DEL CAUCA', 57); 
insert into eventos.DEPARTAMENTOS (codigo,nombre, cod_pais) values (19, 'CAUCA', 57); 

insert into eventos.ciudades (codigo,nombre, cod_dpto) values (76001, 'CALI', 76); 
insert into eventos.ciudades (codigo,nombre, cod_dpto) values (76364, 'JAMUNDI', 76); 
insert into eventos.ciudades (codigo,nombre, cod_dpto) values (19001, 'POPAYAN', 76); 


insert into eventos.facultades (codigo,nombre,ubicacion,nro_telefono) values (1,'INGENIERIA', 'P38-203','3197906');

insert into eventos.sedes (codigo,nombre,cod_ciudad) values (1, 'PANCE', 76001);

insert into eventos.tipos_contratacion (nombre) values ('PRESTACION DE SERVICIOS');
insert into eventos.tipos_contratacion (nombre) values ('CONTRATO A TERMINO INDEFINIDO');
insert into eventos.tipos_contratacion (nombre) values ('CONTRATO A TERMINO DEFINIDO');

insert into eventos.tipos_empleado (nombre) values ('ADMINISTRATIVO');
insert into eventos.tipos_empleado (nombre) values ('DOCENTE');

insert into eventos.empleados (identificacion,nombres,apellidos,email,tipo_contratacion,tipo_empleado,cod_facultad,codigo_sede,lugar_nacimiento) values (10,'ROCIO','LOPEZ','RLOPEZ@U.EDU.CO','CONTRATO A TERMINO INDEFINIDO','ADMINISTRATIVO', 1,1,76364);
insert into eventos.empleados (identificacion,nombres,apellidos,email,tipo_contratacion,tipo_empleado,cod_facultad,codigo_sede,lugar_nacimiento) values (11,'JOSE','JURADO','JJURADO@U.EDU.CO','CONTRATO A TERMINO INDEFINIDO','DOCENTE', 1,1,19001);

insert into eventos.areas (codigo,nombre,codigo_facultad, id_coordinador) values (1, 'CSI', 1, 10); 

insert into eventos.PROGRAMAS (codigo,nombre,codigo_area) values (15,'INGENIERIA DE SISTEMAS', 1);
