import os
import argparse


def main(database: str, url_file_list: str):
    print("We are working with " + database)
    print("We are going scan " + url_file_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-db", "--database", help="SQLite File Name")
    parser.add_argument("-i", "--input", help="File Containing urls to read")
    args = parser.parse_args()
    database_file = args.database
    input_file = args.input
    main(database=database_file, url_file_list=input_file)
