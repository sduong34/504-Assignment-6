#import packages
import pandas as pd 
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
import dbm 

load_dotenv()

MYSQL_HOSTNAME = os.getenv("MYSQL_HOSTNAME")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3306/{MYSQL_DATABASE}'
db = create_engine(connection_string)

#create patients, medications, treatments_procedures, conditions, and social determinants

tableNames = db.table_names()
tableNames = ['Patients', 'Medications', 'Treatments_Procedures', 'Conditions', 'Social_Determinants']

Patients_table = """
create table IF NOT EXISTS patients (
  id int auto_increment,
  mrn varchar(255) default null unique,
  first_name varchar(255) default null,
  last_name varchar(255) default null,
  gender varchar(255) default null,
  zip_code varchar(255) default null,
  dob varchar(255) default null,
  PRIMARY KEY (id)
);
"""
db.execute(Patients_table)

Medications_table = """
create table IF NOT EXISTS medications (
  id int auto_increment,
  medication_name varchar(255) default null,
  ndc_codes varchar(255) default null unique,
  PRIMARY KEY (id)
  );
  """
db.execute(Medications_table)

Treatments_procedures_table = """
create table IF NOT EXISTS treatments_procedures (
  id int auto_increment,
  treatments_procedures_desciption varchar(255),
  cpt_codes varchar(255) default null unique,
  PRIMARY KEY (id)
  );
  """
db.execute(Treatments_procedures_table)

Conditions_table = """
create table IF NOT EXISTS conditions (
  id int auto_increment,
  icd_10_codes varchar(255) default null unique,
  icd_description varchar(255) default null,
  PRIMARY KEY (id)
  );
  """
db.execute(Conditions_table)

Social_determinants_table = """
create table IF NOT EXISTS social_determinants (
  id int auto_increment,
  social_determinants_description varchar(255),
  loinc_codes varchar(255) default null unique,
  PRIMARY KEY (id)
  );
  """
db.execute(Social_determinants_table)

tableNames
