import requests
import duckdb
import itertools

db = duckdb.connect(database="ffl.duckdb", read_only=False)


def get_url(month, year):
    return f"https://www.atf.gov/firearms/docs/undefined/{month:02}{year-2000 if year > 2000 else year}-ffl-list-completetxt/download"


def get_url2(month, year):
    return f"https://www.atf.gov/firearms/docs/undefined/{month:02}{year-2000 if year > 2000 else year}-ffl-listtxt/download"


def get_one(month, year):
    URL = get_url(month, year)
    response = requests.get(URL)

    if response.status_code == 200:
        db.execute(f"""
            set force_download=true;
            create or replace table ffl_{month}_{year} as (
                select
                    {year} as report_year,
                    {month} as report_month,
                    try_cast(lic_regn as integer) as license_region,
                    try_cast(lic_dist as integer) as license_district,
                    try_cast(lic_cnty as integer) as license_county,
                    lic_type as license_type,
                    lic_xprdte as license_expiration_date,
                    lic_seqn as license_sequence_number,
                    license_name as license_name,
                    business_name as business_name,
                    premise_street as premise_street,
                    premise_city as premise_city,
                    premise_state as premise_state,
                    premise_zip_code as premise_zip,
                    mail_street as mailing_street,
                    mail_city as mailing_city,
                    mail_state as mailing_state,
                    mail_zip_code as mailing_zip,
                    voice_phone as voice_phone


                from read_csv_auto('{URL}', sep='\t')
            )
        """)

        print(f"Successfully created table ffl_{month}_{year}")
    else:
        response = requests.get(get_url2(month, year))
        if response.status_code == 200:
            try:
                db.execute(f"""
                    set force_download=true;
                    create or replace table ffl_{month}_{year} as (
                        select
                            {year} as report_year,
                            {month} as report_month, 
                            try_cast("Lic Regn" as integer) as license_region,
                            try_cast("Lic Dist" as integer) as license_district,
                            try_cast("Lic Cnty" as integer) as license_county,
                            "Lic Type" as license_type,
                            "Lic Xprdte" as license_expiration_date,
                            "Lic Seqn" as license_sequence_number,
                            "License Name" as license_name,
                            "Business Name" as business_name,
                            "Premise Street" as premise_street,
                            "Premise City" as premise_city,
                            "Premise State" as premise_state,
                            "Premise Zip Code" as premise_zip,
                            "Mail Street" as mailing_street,
                            "Mail City" as mailing_city,
                            "Mail State" as mailing_state,
                            "Mail Zip Code" as mailing_zip,
                            "Voice Phone" as voice_phone

                        from read_csv_auto('{get_url2(month, year)}', sep='\t')
                    )
                """)

            except Exception as _:
                db.execute(f"""
                    set force_download=true;
                    create or replace table ffl_{month}_{year} as (
                        select
                            {year} as report_year,
                            {month} as report_month,
                            try_cast(lic_regn as integer) as license_region,
                            try_cast(lic_dist as integer) as license_district,
                            try_cast(lic_cnty as integer) as license_county,
                            lic_type as license_type,
                            lic_xprdte as license_expiration_date,
                            lic_seqn as license_sequence_number,
                            license_name as license_name,
                            business_name as business_name,
                            premise_street as premise_street,
                            premise_city as premise_city,
                            premise_state as premise_state,
                            premise_zip_code as premise_zip,
                            mail_street as mailing_street,
                            mail_city as mailing_city,
                            mail_state as mailing_state,
                            mail_zip_code as mailing_zip,
                            voice_phone as voice_phone


                        from read_csv_auto('{get_url2(month, year)}', sep='\t')
                    )
                """)

            print(f"Successfully created table ffl_{month}_{year}")
        else:
            print(f"Failed to create table ffl_{month}_{year}")


def get_ffl_list():
    for year, month in itertools.product(range(2020, 2023), range(1, 13)):
        get_one(month, year)

    for year, month in itertools.product([2024], range(1, 6)):
        get_one(month, year)

    list_of_tables = [
        t for t in db.sql("show tables").df().iloc[:, 0].tolist() if t != "ffl"
    ]

    db.sql(f"""
        create or replace table ffl as (
            select * from {list_of_tables[0]}
        );
    """)

    for table in list_of_tables[1:]:
        db.sql(f"""
            insert into ffl
            select * from {table}
        """)

    for table in list_of_tables:
        db.execute(f"""
            drop table {table}
        """)


if __name__ == "__main__":
    get_ffl_list()
