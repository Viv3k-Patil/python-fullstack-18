CREATE TABLE campus(
          campus_id serial PRIMARY key,
          name VARCHAR(200) not NULL,
          city VARCHAR(50),
          address VARCHAR(200),
          cabin_count INTEGER,
          is_active BOOLEAN,
          created_at date 
);