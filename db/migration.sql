Tables in the database: ['alembic_version', 'data1', 'data3']
Tables created successfully.
CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 60cfdc84664c

DROP TABLE data2;

ALTER TABLE data1 ADD COLUMN `Race_ethnicity` TEXT;

ALTER TABLE data1 DROP COLUMN `Race/ethnicity`;

ALTER TABLE data3 ADD COLUMN `Race_ethnicity` TEXT;

ALTER TABLE data3 MODIFY `SMM_Rate` FLOAT NULL;

ALTER TABLE data3 DROP COLUMN `Race/ethnicity`;

INSERT INTO alembic_version (version_num) VALUES ('60cfdc84664c');

-- Running upgrade 60cfdc84664c -> 2a913f679379

UPDATE alembic_version SET version_num='2a913f679379' WHERE alembic_version.version_num = '60cfdc84664c';

