create table oficina
(
  id_oficina INTEGER       not null
    primary key,
  ciudad     VARCHAR(15)   not null,
  region     VARCHAR(10)   not null,
  director   INTEGER,
  objetivo   DECIMAL(9, 2),
  ventas     DECIMAL(9, 2) not null,
  check (objetivo >= 0),
  check (ventas >= 0)
);

create table producto
(
  id_fab      VARCHAR(3)    not null,
  id_producto VARCHAR(3)    not null,
  descripcion TEXT          not null,
  precio      DECIMAL(7, 2) not null,
  existencias INTEGER       not null,
  primary key (id_fab, id_producto),
  check (existencias >= 0),
  check (precio > 0)
);

create table repventa
(
  id_empleado INTEGER       not null
    primary key,
  nombre      VARCHAR(15)   not null,
  edad        INTEGER,
  id_oficina  INTEGER
    references oficina
      on update cascade
      on delete set null,
  titulo      VARCHAR(10),
  contrato    DATE          not null,
  id_director INTEGER
    references repventa
      on update cascade
      on delete restrict,
  cuota       DECIMAL(8, 2),
  ventas      DECIMAL(8, 2) not null,
  check (contrato <= current_timestamp),
  check (cuota >= 0),
  check (edad > 18),
  check (ventas >= 0)
);

create table cliente
(
  id_cliente     INTEGER     not null
    primary key,
  empresa        VARCHAR(20) not null,
  id_vendedor    INTEGER     not null
    references repventa
      on update cascade
      on delete restrict,
  limite_credito DECIMAL(8, 2),
  check (limite_credito > 0 and limite_credito < 120000)
);

create table pedido
(
  id_pedido    INTEGER       not null
    primary key,
  fecha_pedido DATE          not null,
  id_cliente   INTEGER       not null
    references cliente
      on update cascade
      on delete restrict,
  id_vendedor  INTEGER
    references repventa
      on update cascade
      on delete set null,
  id_fab       VARCHAR(3)    not null,
  id_producto  VARCHAR(3)    not null,
  cantidad     INTEGER       not null,
  importe      DECIMAL(7, 2) not null,
  foreign key (id_fab, id_producto) references producto
    on update cascade
    on delete restrict,
  check (cantidad < 0 or cantidad > 0),
  check (fecha_pedido <= current_timestamp),
  check (importe < 0 or importe > 0)
);

