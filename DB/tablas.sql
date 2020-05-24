CREATE TABLE usuario(
    usuario_id SERIAL PRIMARY KEY,
    nombre character varying(30) NOT NULL,
    apellido character varying(30) NOT NULL,
    correo_electronico character varying(30) NOT NULL,
    password bytea
);

CREATE TABLE clave(
	clave_id SERIAL PRIMARY KEY,
	usuario_id INTEGER,
	public_key bytea,
	private_key bytea,
	CONSTRAINT usuario_id_fkey FOREIGN KEY(usuario_id)
	REFERENCES usuario(usuario_id)
);