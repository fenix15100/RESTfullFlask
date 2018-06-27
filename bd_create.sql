
CREATE TABLE "productos" (
        "id_fab" character(3) NOT NULL,
        "id_producto" character(5) NOT NULL,
        "descripcion" character varying(20) NOT NULL,
        "precio" numeric(7,2) NOT NULL,
        "existencias" int4 NOT NULL,
	constraint cp_productos primary key (id_fab,id_producto),
	constraint chk_productos_precio check (precio>0),
	constraint chk_productos_existencias check (existencias>=0)
);

CREATE TABLE "oficinas" (
        "oficina" int2 NOT NULL,
        "ciudad" character varying(15) NOT NULL,
        "region" character varying(10) NOT NULL,
        "dir" int2,
        "objetivo" numeric(9,2),
        "ventas" numeric(9,2) NOT NULL,
	constraint cp_oficinas primary key (oficina),
	constraint chk_oficina_ventas check (ventas>=0), 
	constraint chk_oficina_objetivo check (objetivo>=0)

	

);


CREATE TABLE "repventas" (
        "num_empl" int2 NOT NULL,
        "nombre" character varying(15) NOT NULL,
        "edad" int2,
        "oficina_rep" int2,
        "titulo" character varying(10),
        "contrato" date NOT NULL,
        "director" int2,
        "cuota" numeric(8,2),
        "ventas" numeric(8,2) NOT NULL,
	constraint cp_repventas primary key (num_empl),
	constraint ca_dir foreign key(director) references repventas on delete restrict on update cascade,
	constraint ca_ofi_rep foreign key(oficina_rep) references oficinas on delete set null on update cascade,
	constraint chk_repventas_edad check (edad>18),
	constraint chk_repventas_ventas check (ventas>=0), 
	constraint chk_repventas_cuota check (cuota>=0),
	constraint chk_repventas_contrato check (contrato< current_date)
	
	
);

create table clientes
	(num_clie int2 not null,
	empresa varchar(20) not null,
	rep_clie int2 not null,
	limite_credito numeric(8,2),
	constraint cp_clientes primary key(num_clie),
	constraint  ca_rep_clie foreign key(rep_clie) references repventas on delete restrict on update cascade,
	constraint chk_clientes_limite_credito check (limite_credito>0 and limite_credito<120000)
);

CREATE TABLE "pedidos" (
        "num_pedido" int4 NOT NULL,
        "fecha_pedido" date NOT NULL,
        "clie" int2 NOT NULL,
        "rep" int2,
        "fab" character(3) NOT NULL,
        "producto" character(5) NOT NULL,
        "cant" int2 NOT NULL,
        "importe" numeric(7,2) NOT NULL,
	constraint cp_pedidos primary key (num_pedido),
	constraint ca_pedidos_rep foreign key(rep) references repventas on delete set null on update cascade,
	constraint ca_pedidos_clie foreign key(clie) references clientes on delete restrict on update cascade,
	constraint ca_pedidos_fab_pro foreign key(fab,producto) references productos on delete restrict on update cascade,
	constraint chk_pedidos_cant check (cant<0 or cant>0),
	constraint chk_pedidos_importe check (importe<0 or importe>0),
	constraint chk_pedidos_fecha_pedido check(fecha_pedido<current_date)
	
);


